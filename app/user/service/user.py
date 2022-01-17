import bcrypt

from typing import Union, NoReturn
from fastapi.responses import RedirectResponse
from pythondi import inject

from app.user.models.user import User
from app.user.repository.user import UserRepo
from core.db.transaction import Transaction, Propagation
from core.utiles.token_helper import TokenHelper
from core.exceptions.user import(
    UserNotFoundException,
    DuplicateNameException,
    DuplicateEmailException,
)


class UserService:
    @inject()
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_user(
            self,
            email: str,
            name: str,
            password: str
    ) -> Union[User, NoReturn]:
        if await self.user_repo.get_by_email(email=email):
            raise DuplicateEmailException

        if await self.user_repo.get_by_name(name=name):
            raise DuplicateNameException

        user = User().create(email=email, name=name, password=password)
        user = await self.user_repo.save(user=user)
        return user

    @Transaction(propagation=Propagation.REQUIRED)
    async def login_user(self, email: str, password: str) -> str:
        user = await self.user_repo.get_by_email(email=email)
        if not user:
            raise UserNotFoundException

        if (
            await self._check_password(password1=password, password2=user.password)
            is False
        ):
            raise UserNotFoundException

        access_token = TokenHelper.create_token({'user': user.id})
        return access_token


    async def _check_password(self, password1: str, password2: str) -> bool:
        return bcrypt.checkpw(password1.encode("utf8"), password2.encode("utf-8"))

