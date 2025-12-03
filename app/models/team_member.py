from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class TeamMember(Base):
    __tablename__ = "teammember"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)

    tasks = relationship("Task", back_populates="assignee")
