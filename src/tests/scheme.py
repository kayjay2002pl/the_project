from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DemoScheme(BaseModel):
    school_name: str
    category:str
    year: str
    total_enrollment: str
    grade_k: str
    grade_1: str
    grade_2: str
    grade_3: str
    grade_4: str
    grade_5: str
    grade_6: str
    grade_7: str
    grade_8: str
    female: str
    female_percent: str
    male: str
    male_percent: str