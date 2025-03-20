from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database import Db

app = FastAPI()
db = Db()

from methods import *

app.mount("/", StaticFiles(directory="build", html=True), name="build")
