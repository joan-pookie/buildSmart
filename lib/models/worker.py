from sqlalchemy import Column, Integer, String
from .base import Base


class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String)

    def __repr__(self):
        return f"<Worker id={self.id} name={self.name}>"
