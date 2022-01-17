from fastapi import APIRouter

from .household_ledger import household_ledger_router

sub_router = APIRouter()
sub_router.include_router(household_ledger_router, prefix="", tags=["Household Ledger"])

__all__ = ["sub_router"]