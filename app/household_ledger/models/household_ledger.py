from typing import Union, NoReturn

from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Boolean, func, Date

from core.db.session import Base
from core.db.timestamp_mixin import TimestampMixin


class HouseholdLedger(Base, TimestampMixin):
    __tablename__ = "household_ledger"

    id = Column(Integer, primary_key=True, autoincrement=True)
    memo = Column(String(length=100), nullable=False)
    price = Column(Numeric(14, 2), nullable=False)
    transfer = Column(String(length=20), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    is_delete = Column(Boolean, default=False)
    created_at = Column(
                        DateTime,
                        nullable=False,
                        default=func.utc_timestamp(),
                        onupdate=func.utc_timestamp(),
    )
    updated_at = Column(
                        DateTime,
                        nullable=False,
                        default=func.utc_timestamp(),
                        onupdate=func.utc_timestamp(),
    )

    def create(
            self,
            memo: str,
            price: float,
            user_id: int,
            transfer: str,
    ) -> Union["HouseholdLedger", NoReturn]:
        return HouseholdLedger(
            memo=memo,
            price=price,
            transfer=transfer,
            user_id=user_id,
        )