from typing import Union, NoReturn, List
from fastapi import Request
from pythondi import inject

from app.household_ledger.models.household_ledger import HouseholdLedger
from app.household_ledger.repository.household_ledger import HouseholdLedgerRepo
from core.db.transaction import Transaction, Propagation


from core.exceptions.household_ledger import(
    HouseholdLedgerNotFoundException
)


class HouseholdLedgerService:
    @inject()
    def __init__(self, household_ledger_repo: HouseholdLedgerRepo):
        self.household_ledger_repo = household_ledger_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_household_ledger(
            self,
            user_info: Request,
            memo: str,
            price: float,
            transfer: str,
    ) -> Union[HouseholdLedger, NoReturn]:
        user_id = user_info.user.id
        household_ledger = HouseholdLedger().create(
            memo=memo,
            price=price,
            transfer=transfer,
            user_id=user_id,
        )
        household_ledger = await self.household_ledger_repo.save(
            household_ledger=household_ledger,
        )
        return household_ledger

    @Transaction(propagation=Propagation.REQUIRED)
    async def delete_household_ledger(
            self,
            user_info: Request,
            household_ledger_id: int,
    ) -> Union[HouseholdLedger, NoReturn]:
        user_id = user_info.user.id
        household_ledger = await self.household_ledger_repo.delete_household_ledger(
            user_id=user_id,
            household_ledger_id=household_ledger_id,
        )
        if not household_ledger:
            raise HouseholdLedgerNotFoundException

        return household_ledger

    @Transaction(propagation=Propagation.REQUIRED)
    async def update_household_ledger(
            self,
            user_info: Request,
            household_ledger_id: int,
            request: dict,
    ) -> Union[HouseholdLedger, NoReturn]:
        user_id = user_info.user.id
        household_ledger = await self.household_ledger_repo.update_household_ledger(
            user_id=user_id,
            household_ledger_id=household_ledger_id,
            request=request,
        )
        if not household_ledger:
            raise HouseholdLedgerNotFoundException

        return household_ledger

    @Transaction(propagation=Propagation.REQUIRED)
    async def list_household_ledger(self, user_info: Request) -> Union[List, NoReturn]:
        user_id = user_info.user.id
        household_ledger_query = await self.household_ledger_repo.list_household_ledger(user_id=user_id)

        household_ledger_list = []
        for item in household_ledger_query:
            ledger_dict = {
                "id": item.id,
                "memo": item.memo,
                "transfer": item.transfer,
                "price": item.price,
                "created_at": item.created_at,
            }
            household_ledger_list.append(ledger_dict)

        return household_ledger_list

    @Transaction(propagation=Propagation.REQUIRED)
    async def detail_household_ledger(
            self,
            user_info: Request,
            household_ledger_id: int
    ) -> Union[HouseholdLedger, NoReturn]:
        user_id = user_info.user.id
        household_ledger = await self.household_ledger_repo.detail_household_ledger(
            user_id=user_id,
            household_ledger_id=household_ledger_id
        )
        if not household_ledger:
            raise HouseholdLedgerNotFoundException

        return household_ledger

    @Transaction(propagation=Propagation.REQUIRED)
    async def delete_list_household_ledger(self, user_info: Request) -> Union[List, NoReturn]:
        user_id = user_info.user.id
        household_ledger = await self.household_ledger_repo.delete_list_household_ledger(user_id=user_id)

        household_ledger_list = []
        for item in household_ledger:
            ledger_dict = {
                "id": item.id,
                "memo": item.memo,
                "transfer": item.transfer,
                "price": item.price,
                "created_at": item.created_at,
            }
            household_ledger_list.append(ledger_dict)

        return household_ledger_list

    @Transaction(propagation=Propagation.REQUIRED)
    async def restoration_household_ledger(
                self,
                user_info: Request,
                household_ledger_id: int,
    ) -> Union[HouseholdLedger, NoReturn]:
        user_id = user_info.user.id
        household_ledger = await self.household_ledger_repo.restoration_household_ledger(
            user_id=user_id,
            household_ledger_id=household_ledger_id,
        )
        if not household_ledger:
            raise HouseholdLedgerNotFoundException

        return household_ledger

