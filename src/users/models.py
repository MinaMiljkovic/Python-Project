from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data_base.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    projects = relationship("ProjectAccess", back_populates="user")
