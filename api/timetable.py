from app import app
from flask import request, session
from db import db
import json

from models import Pupil, SchoolClass, Subject


@app.route("/timetable/timetableClass/<int:c>", methods=["GET"])
def get_timetable_pupil(id_pupil):
    pupil = db.session.query(Pupil).filter(id_pupil == Pupil.id).first()
    clas = db.session.query(SchoolClass).filter(pupil.clas == SchoolClass.name).first()
    return clas.get_timetable_class()


@app.route("/timetable/set_homework", methods=["PUT"])
def set_homework():
    new_homework = request.form.get("homework")
    name_subject = request.form.get("name_subject")
    class_number = str(request.form.get("class"))
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


@app.route("/timetable/get_homework", methods=["GET"])
def get_homework():
    name_subject = request.form.get("subject")
    class_ = str(request.form.get("class"))
    subject = db.session.query(Subject).filter(name_subject == Subject.name and class_ == Subject.school_class_name).first()
    return subject.get_hw()


@app.route("/timetable/get_students_list", methods=["GET"])
def get_students_list():
    name_subject = request.form.get("subject")
    class_ = str(request.form.get("class"))
    subject = db.session.query(Subject).filter(name_subject == Subject.name and class_ == Subject.school_class_name).first()
    return subject.get_students_list()


@app.route("/timetable/get_room", methods=["GET"])
def get_room():
    name_subject = request.form.get("subject")
    class_ = str(request.form.get("class"))
    subject = db.session.query(Subject).filter(name_subject == Subject.name and class_ == Subject.school_class_name).first()
    return subject.get_class()


@app.route("/timetable/set_room", methods=["GET"])
def set_room():
    name_subject = request.form.get("subject")
    class_ = str(request.form.get("class"))
    new_room = str(request.form.get("new room"))
    subject = db.session.query(Subject).filter(name_subject == Subject.name and class_ == Subject.school_class_name).first()
    subject.set_class(new_room)
    return json.dumps(
        {
            'resultCode': 0,
            'data': {
                'new room': new_room,
                'name_subject': name_subject,
                'class': class_
            }
        }
    )
