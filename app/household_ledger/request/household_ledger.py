from pydantic import BaseModel
from typing import Optional, List

class CreateHouseholdLedgerRequest(BaseModel):
    memo: str
    price: float
    transfer: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "memo": "편의점 과자 구매",
                "price": 3000.00,
                "transfer": "출금",
            }
        }


class UpdateHouseholdLedgerRequest(BaseModel):
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
