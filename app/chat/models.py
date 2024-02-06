from sqlalchemy import Column, Integer, String

from base_class import Base


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    message = Column(String)
