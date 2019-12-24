from app import app
from flask import request, session
from db import db
import json

from models import TimetableClass


@app.route("/timetable_class/get_all_day_timetable", methods=["PUT"])
def get_all_day_timetable():
    timetable_class_id = request.form.get("timetableClass_id")
    subject = db.session.query(TimetableClass).filter(timetable_class_id == TimetableClass.id).first()
    return json.dumps(subject.get_all_day_timetable())


@app.route("/timetable_class/set", methods=["PUT"])
def set_day():
    timetable_class_id = request.form.get("timetableClass_id")
    number_day = request.form.get("day number")
    new_day_id = request.form.get("new day id")
    subject = db.session.query(TimetableClass).filter(timetable_class_id == TimetableClass.id).first()

    if number_day == 1:
        subject.set_monday(new_day_id)
    elif number_day == 2:
        subject.set_tuesday(new_day_id)
    elif number_day == 3:
        subject.set_wednesday(new_day_id)
    elif number_day == 4:
        subject.set_thursday(new_day_id)
    elif number_day == 5:
        subject.set_friday(new_day_id)

    return json.dumps(
        {
            'resultCode': 0,
            'data': {
                'timetable_class_id': timetable_class_id,
                'changed day number': number_day,
                'new_day_id': new_day_id
            }
        }
    )
