from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data_base.models import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    projects = relationship("ProjectAccess", back_populates="user")
