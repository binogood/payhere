from abc import ABCMeta, abstractmethod
from typing import Optional

from app.household_ledger.models.household_ledger import HouseholdLedger
from core.db.session import session


class HouseholdLedgerRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def update_household_ledger(
            self,
            user_id: int,
            household_ledger_id: int,
            request: dict,
    ) -> Optional[HouseholdLedger]:
        pass

    async def delete_household_ledger(
            self,
            user_id: int,
            household_ledger_id: int
    ) -> Optional[HouseholdLedger]:
        pass

    @abstractmethod
    async def list_household_ledger(self, user_id: int) -> Optional[HouseholdLedger]:
        pass

    @abstractmethod
    async def detail_household_ledger(
            self,
            user_id: int,
            household_ledger_id: int
    ) -> Optional[HouseholdLedger]:
        pass

    async def restoration_household_ledger(
            self,
            user_id: int,
            household_ledger_id: int
    ) -> Optional[HouseholdLedger]:
        pass

    @abstractmethod
    async def delete_list_household_ledger(self, user_id: int) -> Optional[HouseholdLedger]:
        pass

    @abstractmethod
    async def save(self, household_ledger: HouseholdLedger):
        pass


class HouseHoldLedgerMySQLRepo(HouseholdLedgerRepo):
    async def update_household_ledger(
            self,
            user_id: int,
            household_ledger_id: int,
            request: dict,
    ) -> Optional[HouseholdLedger]:
        household_ledger = session.query(HouseholdLedger).filter(
            HouseholdLedger.user_id == user_id,
            HouseholdLedger.id == household_ledger_id,
            HouseholdLedger.is_delete == 0,
        ).first()
        if not household_ledger:
            return None

        for key, value in request.items():
            setattr(household_ledger, key, value)

        session.add(household_ledger)

        return household_ledger

    async def delete_household_ledger(
            self,
            user_id: int,
            household_ledger_id: int
    ) -> Optional[HouseholdLedger]:
        household_ledger = session.query(HouseholdLedger).filter(
            HouseholdLedger.user_id == user_id,
            HouseholdLedger.id == household_ledger_id,
            HouseholdLedger.is_delete == 0,
        ).first()
        if not household_ledger:
            return None

        household_ledger.is_delete = True
        session.add(household_ledger)

        return household_ledger

    async def list_household_ledger(self, user_id: int) -> Optional[HouseholdLedger]:
        return session.query(HouseholdLedger).filter(
            HouseholdLedger.user_id == user_id,
            HouseholdLedger.is_delete == 0,
        ).all()

    async def detail_household_ledger(
            self,
            user_id: int,
            household_ledger_id: int
    ) -> Optional[HouseholdLedger]:
        return session.query(HouseholdLedger).filter(
            HouseholdLedger.user_id == user_id,
            HouseholdLedger.id == household_ledger_id,
            HouseholdLedger.is_delete == 0,
        ).first()

    async def restoration_household_ledger(
            self,
            user_id: int,
            household_ledger_id: int
    ) -> Optional[HouseholdLedger]:
        household_ledger = session.query(HouseholdLedger).filter(
            HouseholdLedger.user_id == user_id,
            HouseholdLedger.id == household_ledger_id,
            HouseholdLedger.is_delete == 1,
        ).first()
        if not household_ledger:
            return None

        household_ledger.is_delete = False
        session.add(household_ledger)

        return household_ledger

    @abstractmethod
    async def delete_list_household_ledger(self, user_id: int) -> Optional[HouseholdLedger]:
        return session.query(HouseholdLedger).filter(
            HouseholdLedger.user_id == user_id,
            HouseholdLedger.is_delete == 1,
        ).all()

    async def save(self, household_ledger: HouseholdLedger):
        session.add(household_ledger)

        return household_ledger
