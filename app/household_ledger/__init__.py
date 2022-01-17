from fastapi import APIRouter

from app.household_ledger.views import sub_router

household_ledger_router = APIRouter()
household_ledger_router.include_router(
                sub_router,
                prefix="/household_ledger",
                tags=["Household Ledger"]
)

__all__ = ["household_ledger_router"]