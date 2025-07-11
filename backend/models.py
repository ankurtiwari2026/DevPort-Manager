from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    github_url = Column(String)
    stars = Column(Integer)
    language = Column(String)
    featured = Column(Boolean, default=False)
