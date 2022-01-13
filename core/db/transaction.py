from functools import wraps

from app.user.enums import BaseEnum
from core.db.session import session


class Propagation(BaseEnum):
    REQUIRED = "required"


class Transaction:
    def __init__(self, propagation: Propagation = Propagation.REQUIRED):
        self.propagation = propagation

    def __call__(self, function):
        @wraps(function)
        async def decorator(*args, **kwargs):
            try:
                result = await self.run_required(
                    function=function, args=args, kwargs=kwargs,
                )
            except Exception as e:
                session.rollback()
                raise e
            return result

        return decorator()

    async def run_required(self, function, args, kwargs):
        is_transaction_active = session().is_active

        if not is_transaction_active:
            session.begin(subtransactions=True)

        result = await function(*args, **kwargs)
        if not is_transaction_active:
            session.commit()

        return result

    def __enter__(self):
        session.begin(subtransactions=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e