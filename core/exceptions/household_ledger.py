from core.exceptions.base import CustomException


class HouseholdLedgerNotFoundException(CustomException):
    code = 404
    error_code = 30000
    message = "Household Ledger not found"