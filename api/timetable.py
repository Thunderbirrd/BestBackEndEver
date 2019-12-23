from app import app
from flask import request, session
from db import db
import json

from models import Pupil, SchoolClass


@app.route("/timetable/timetableClass/<id_pupil>", methods=["GET"])
def get_timetable_pupil(id_pupil):
    print(id_pupil)
    pupil = db.session.query(Pupil).filter(id_pupil == Pupil.id).first()
    clas = db.session.query(SchoolClass).filter(pupil.clas == SchoolClass.name).first()
    return clas.get_timetable_class()
