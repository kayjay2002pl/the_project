from sqlalchemy import Column, Integer, String
from data.db_conf import Base

class Demo(Base):
    __tablename__ = "demo"
    id = Column(Integer, primary_key=True, index=True)
    school_name = Column(String)
    category = Column(String)
    year = Column(String)
    total_enrollment = Column(String)
    grade_k = Column(String)
    grade_1 = Column(String)
    grade_2 = Column(String)
    grade_3 = Column(String)
    grade_4 = Column(String)
    grade_5 = Column(String)
    grade_6 = Column(String)
    grade_7 = Column(String)
    grade_8 = Column(String)
    female = Column(String)
    female_percent = Column(String)
    male = Column(String)
    male_percent = Column(String)