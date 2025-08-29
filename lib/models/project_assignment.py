from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class ProjectAssignment(Base):
    __tablename__ = "project_assignments"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    worker_id = Column(Integer, ForeignKey("workers.id"))

    project = relationship("Project", backref="assignments")
    worker = relationship("Worker", backref="assignments")

    def __repr__(self):
        return f"<ProjectAssignment project_id={self.project_id} worker_id={self.worker_id}>"
