from fastapi import APIRouter, Depends, Response, Request
from fastapi.responses import HTMLResponse
from typing import Optional

from app.user.request.user import CreateUserRequest, LoginUserRequest
from app.user.response.user import CreateUserResponse, LoginUserResponse
from app.user.service.user import UserService

from core.fastapi.schemas.response import ExceptionResponseSchema
from core.fastapi.dependencies.permission import PermissionDependency, IsAuthenticated

user_router = APIRouter()


@user_router.post(
    "/create",
    response_model=CreateUserResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create User",
)
async def create_user(request: CreateUserRequest):
    return await UserService().create_user(**request.dict())


@user_router.post(
    "/login",
    response_model=LoginUserResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Login User",
)
async def login_user(request: LoginUserRequest):
    access_token = await UserService().login_user(**request.dict())
    return {"access_token": access_token, "token_type": "bearer"}


# @user_router.get(
#     "/logout",
#     responses={"400": {"model": ExceptionResponseSchema}},
#     dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
#     summary="Logout User",
# )
# async def logout_user(request: Request, response: Response):
#     return await UserService().logout_user(response)