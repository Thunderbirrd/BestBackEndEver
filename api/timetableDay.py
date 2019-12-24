from app import app
from flask import request, session
from db import db
import json

@app.route("/timetableDay/set", methods=["POST"])
def setLesson(number_lesson, new_lesson):
