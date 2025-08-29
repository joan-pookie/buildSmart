#equipments assigned to projects
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String)
    status = Column(String, default="Available")

    # Optional link to a project
    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="equipment")

    def __repr__(self):
        return f"<Equipment(id={self.id}, name='{self.name}', type='{self.type}', status='{self.status}')>"
