import os, json
from celery import Celery
from dotenv import load_dotenv
import models.demo as demo
import schemes.demo_scheme as demo_scheme
from data.db_conf import db_session 


db = db_session.session_factory()
load_dotenv(".env")

celery2 = Celery(__name__)
celery2.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery2.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


@celery2.task(name="fill_database")
def fill_database():

    f = open("data/rows.json")
    rows = json.loads(f.read())
    f.close()
    for item in rows["data"]:
        post = demo_scheme.DemoScheme(school_name = str(item[9] or "No Data"),
            category = str(item[10] or "No Data"),
            year = str(item[11] or "No Data"),
            total_enrollment = str(item[12] or "No Data"),
            grade_k = str(item[13] or "No Data"),
            grade_1 = str(item[14] or "No Data"),
            grade_2 = str(item[15] or "No Data"),
            grade_3 = str(item[16] or "No Data"),
            grade_4 = str(item[17] or "No Data"),
            grade_5 = str(item[18] or "No Data"),
            grade_6 = str(item[19] or "No Data"),
            grade_7 = str(item[20] or "No Data"),
            grade_8 = str(item[21] or "No Data"),
            female = str(item[22] or "No Data"),
            female_percent = str(item[23] or "No Data"),
            male = str(item[24] or "No Data"),
            male_percent = str(item[25] or "No Data"))
        db_post = demo.Demo(
            school_name = post.school_name,
            category = post.category,
            year = post.year,
            total_enrollment = post.total_enrollment,
            grade_k = post.grade_k,
            grade_1 = post.grade_1,
            grade_2 = post.grade_2,
            grade_3 = post.grade_3,
            grade_4 = post.grade_4,
            grade_5 = post.grade_5,
            grade_6 = post.grade_6,
            grade_7 = post.grade_7,
            grade_8 = post.grade_8,
            female = post.female,
            female_percent = post.female_percent,
            male = post.male,
            male_percent = post.male_percent)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)

if not os.path.isfile("data/controlfile.txt"):
    fill_database()
    open("data/controlfile.txt", "w").close()