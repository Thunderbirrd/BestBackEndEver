from app import app
from flask import request, session
from db import db
import json

from models import Pupil, SchoolClass, Subject


@app.route("/timetable/timetableClass/<int:id_pupil>", methods=["GET"])
def get_timetable_pupil(id_pupil):
    pupil = db.session.query(Pupil).filter(id_pupil == Pupil.id).first()
    clas = db.session.query(SchoolClass).filter(pupil.clas == SchoolClass.name).first()
    return clas.get_timetable_class()


@app.route("/timetable/homework", methods=["PUT"])
def set_homework():
    new_homework = request.form.get("homework")
    name_subject = request.form.get("name_subject")
    class_number = str(request.form.get("class") + "a")
    subject = db.session.query(Subject).filter(name_subject == Subject.name and class_number == Subject.school_class_name).first()
    subject.set_homework(new_homework)

    return json.dumps(
        {
            'resultCode': 0,
            'data': {
                'homework': new_homework,
                'name_subject': name_subject,
                'class': class_number
            }
        }
    )

