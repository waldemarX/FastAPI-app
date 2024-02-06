from pydantic import BaseModel


class MessagesModel(BaseModel):
    message: str

    class Config:
        orm_mode = True
