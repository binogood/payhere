from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from core.di import init_di
from core.exception.base import CustomException
from core.fastapi.middlewares.sqlalchemy import SQLAlchemyMiddleware
from core.fastapi.middlewares.authentication import (
    AuthenticationMiddleware,
    AuthBackend,
)
# from app.user import user_router


def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_routers(app: FastAPI) -> None:
    # app.include_router(user_router)
    pass


def init_listeners(app: FastAPI) -> None:
    @app.exception_handlers(CustomException)
    async def custom_exceoption_handler(exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def on_auth_error(exc: Exception):
    status_code, error_code, message = 401, None, str(exc)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        error_code = exc.error_code
        message = exc.message
    return JSONResponse(
        status_code=status_code, content={"error_code": error_code, "message": message}
    )


def init_middleware(app: FastAPI) -> None:
    app.add_middleware(SQLAlchemyMiddleware)
    app.add_middleware(
        AuthenticationMiddleware, backend=AuthBackend(), on_error=on_auth_error()
    )


DESCRIPTION = "Payhere"


def create_app() -> FastAPI:
    app = FastAPI(title="Payhere", description=DESCRIPTION,)
    init_routers(app=app)
    init_cors(app=app)
    init_listeners(app=app)
    init_middleware(app=app)
    init_di()
    return app

app = create_app()