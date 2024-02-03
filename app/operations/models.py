from datetime import datetime
from sqlalchemy import TIMESTAMP, String
from sqlalchemy.orm import Mapped, mapped_column
from base_class import Base


class Operation(Base):
    __tablename__ = "operation"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[str] = mapped_column(String(length=240))
    figi: Mapped[str] = mapped_column(String(length=240))
    instrument_type: Mapped[str] = mapped_column(
        String(length=240), nullable=True
    )
    date: Mapped[str] = mapped_column(
        TIMESTAMP, default=datetime.utcnow(), nullable=False
    )
    type: Mapped[str] = mapped_column(String(length=240))
