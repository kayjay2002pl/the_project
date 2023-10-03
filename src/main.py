from fastapi import FastAPI
from fastapi.responses import FileResponse

from celery_worker import create_chart
from data.db_conf import db_session 
import models.demo as demo, models.charts as charts

db = db_session.session_factory()
app = FastAPI()

@app.get("/query")
async def return_query(top: int = 10, category: str = "total_enrollment"):
    q = db.query(demo.Demo).filter(demo.Demo.category == "All Students").all()
    link = create_chart(limit=top, category=category)
    return {"table": q[0:top], "link":link}

@app.get("/chart")
async def return_chart(id: int = 1):
    q = db.query(charts.Charts).filter(charts.Charts.chart_id == id).first()
    print("data/charts/" + q.filename)
    return FileResponse("data/charts/" + q.filename, media_type="image/png")