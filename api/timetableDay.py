from app import app
from flask import request, session
from db import db
import json

from models import TimetableDay


@app.route("/timetableDay/set", methods=["POST"])
def set_lesson():
    id_lesson = request.form.get("id_lesson")
    number_lesson = request.form.get("number_lesson")
    new_lesson = request.form.get("new_lesson")

    timetable_day = TimetableDay.get_by_id(id_lesson)

    if number_lesson == 1:
        timetable_day.set_first(new_lesson)
    elif number_lesson == 2:
        timetable_day.set_second(new_lesson)
    elif number_lesson == 3:
        timetable_day.set_third(new_lesson)
    elif number_lesson == 4:
        timetable_day.set_fourth(new_lesson)
    elif number_lesson == 5:
        timetable_day.set_fifth(new_lesson)
    elif number_lesson == 6:
        timetable_day.set_sixth(new_lesson)
    elif number_lesson == 7:
        timetable_day.set_seventh(new_lesson)
    elif number_lesson == 8:
        timetable_day.set_eighth(new_lesson)
    else:
        return json.dumps({"resultCode": 1})

    return json.dumps({"resultCode": 0})
