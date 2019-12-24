from app import app
from flask import request, session
from db import db
import json

from models import TimetableDay


@app.route("/timetableDay/set", methods=["POST"])
def set_lesson(id_lesson, number_lesson, new_lesson):
    if number_lesson == 1:
        timetable_day = TimetableDay.get_by_id(id_lesson)

        if number_lesson == 1:
            timetable_day.set_monday(new_lesson)
        elif number_lesson == 2:
            timetable_day.set_tuesday(new_lesson)
        elif number_lesson == 3:
            timetable_day.set_wednesday(new_lesson)
        elif number_lesson == 4:
            timetable_day.set_thursday(new_lesson)
        elif number_lesson == 5:
            timetable_day.set_friday(new_lesson)
