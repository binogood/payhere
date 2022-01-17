from fastapi import APIRouter, Depends, Request
from typing import List

from app.household_ledger.service.household_ledger import HouseholdLedgerService
from app.household_ledger.request.household_ledger import (
    CreateHouseholdLedgerRequest,
    UpdateHouseholdLedgerRequest,
)
from app.household_ledger.response.household_ledger import (
    CreateHouseholdLedgerResponse,
    UpdateHouseholdLedgerResponse,
    DeleteHouseholdLedgerResponse,
    DetailGetHouseholdLedgerResponse,
    RestorationHouseholdLedgerResponse,
)
from core.fastapi.dependencies.permission import PermissionDependency, IsAuthenticated
from core.fastapi.schemas.response import ExceptionResponseSchema

household_ledger_router = APIRouter()


@household_ledger_router.post(
    "/create",
    response_model=CreateHouseholdLedgerResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
    summary="Create Household Ledger",
)
async def create_household_ledger(user_info: Request, request: CreateHouseholdLedgerRequest):
    return await HouseholdLedgerService().create_household_ledger(user_info, **request.dict())


@household_ledger_router.patch(
    "/delete/{ledger_id}",
    response_model=DeleteHouseholdLedgerResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
    summary="Delete Household Ledger",
)
async def delete_household_ledger(user_info: Request, ledger_id: int):
    return await HouseholdLedgerService().delete_household_ledger(user_info, ledger_id)


@household_ledger_router.patch(
    "/delete/restoration/{ledger_id}",
    response_model=RestorationHouseholdLedgerResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
    summary="Restoration Household Ledger",
)
async def delete_household_ledger(user_info: Request, ledger_id: int):
    return await HouseholdLedgerService().restoration_household_ledger(user_info, ledger_id)


@household_ledger_router.patch(
    "/update/{ledger_id}",
    response_model=UpdateHouseholdLedgerResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
    summary="Update Household Ledger",
)
async def update_household_ledger(
        user_info: Request,
        request: UpdateHouseholdLedgerRequest,
        ledger_id: int,
):
    return await HouseholdLedgerService().update_household_ledger(
        user_info,
        ledger_id,
        request.dict()
    )


@household_ledger_router.get(
    "/list",
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
    summary="List Household Ledger"
)
async def list_household_ledger(user_info: Request):
    return await HouseholdLedgerService().list_household_ledger(user_info)


@household_ledger_router.get(
    "/{ledger_id}",
    response_model=DetailGetHouseholdLedgerResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
    summary="Detail Household Ledger"
)
async def list_household_ledger(user_info: Request, ledger_id: int):
    return await HouseholdLedgerService().detail_household_ledger(user_info, ledger_id)


@household_ledger_router.get(
    "/delete/list",
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
    summary="Delete List Household Ledger"
)
async def list_household_ledger(user_info: Request):
    return await HouseholdLedgerService().delete_list_household_ledger(user_info)
