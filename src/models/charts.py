from sqlalchemy import Column, Integer, String
from data.db_conf import Base

class Charts(Base):
    __tablename__ = "charts"
    chart_id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)