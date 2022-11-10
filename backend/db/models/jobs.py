from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    company = Column(String(100), nullable=False)
    company_url = Column(String(25))
    location = Column(String(25), nullable=False)
    description = Column(String(255), nullable=False)
    date_posted = Column(Date)
    is_active = Column(Boolean(), default=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="jobs")
