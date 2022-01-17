from pythondi import Provider, configure
from app.user.repository.user import UserRepo, UserMySQLRepo
from app.household_ledger.repository.household_ledger import (
    HouseholdLedgerRepo,
    HouseHoldLedgerMySQLRepo
)



def init_di():
    provider = Provider()
    provider.bind(UserRepo, UserMySQLRepo)
    provider.bind(HouseholdLedgerRepo, HouseHoldLedgerMySQLRepo)
    configure(provider=provider)