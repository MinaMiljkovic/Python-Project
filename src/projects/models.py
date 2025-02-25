from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from data_base.database import Base

class ProjectAccess(Base):
    __tablename__ = "project_access"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    role = Column(Enum("owner", "participant", name="access_role"), nullable=False)

    user = relationship("User", back_populates="projects")
    project = relationship("Project", back_populates="access")
