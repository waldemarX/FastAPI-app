from pydantic import BaseModel


class OperationCreate(BaseModel):
    quantity: str
    figi: str
    instrument_type: str
    type: str
