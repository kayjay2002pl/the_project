from fastapi import FastAPI, Body
from data.db_conf import db_session 

db = db_session.session_factory()
app = FastAPI()