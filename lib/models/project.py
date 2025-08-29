from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    client_id = Column(Integer, ForeignKey("clients.id"))

    client = relationship("Client", backref="projects")

    def __repr__(self):
        return f"<Project id={self.id} name={self.name}>"
