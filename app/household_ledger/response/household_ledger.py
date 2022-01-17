from pydantic import BaseModel
from datetime import datetime


class CreateHouseholdLedgerResponse(BaseModel):
    id: int
    user_id: int
    memo: str
    transfer: str
    price: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "user_id": 1,
                "memo": "편의점 과자 구매",
                "transfer": "지출",
                "price": 3000.00,
                "created_at": "2021-11-11T07:50:54.289Z",
                "updated_at": "2021-11-11T07:50:54.289Z",
            }
        }


class UpdateHouseholdLedgerResponse(BaseModel):
    memo: str
    price: float
    transfer: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "memo": "편의점 과자 환불",
                "price": 3000.00,
                "transfer": "입금",
            }
        }


class DeleteHouseholdLedgerResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
            }
        }


class RestorationHouseholdLedgerResponse(BaseModel):
    id: int
    is_delete: bool

    class Config:
        class Config:
            orm_mode = True
            schema_extra = {
                "example": {
                    "id": 1,
                    "is_delete": True,
                }
            }


class DetailGetHouseholdLedgerResponse(BaseModel):
    id: int
    user_id: int
    memo: str
    transfer: str
    price: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "user_id": 1,
                "memo": "편의점 과자 구매",
                "transfer": "지출",
                "price": 3000.00,
                "created_at": "2021-11-11T07:50:54.289Z",
                "updated_at": "2021-11-11T07:50:54.289Z",
            }
        }
