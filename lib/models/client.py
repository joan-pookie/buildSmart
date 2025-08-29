from sqlalchemy import Column, Integer, String
from .base import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)

    def __repr__(self):
        return f"<Client id={self.id} name={self.name}>"
