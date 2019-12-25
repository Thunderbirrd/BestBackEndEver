from app import app
from flask import request, session
from db import db
import json

from models import Pupil


@app.route("/marks/add", methods=["PUT"])
def add_marks():
    id_pupil = request.form.get("id_pupil")
    name_subject = request.form.get("name_subject")
    new_mark = request.form.get("new_mark")

    pupil = db.session.query(Pupil).filter(Pupil.id == id_pupil).first()

    pupil.add_marks(name_subject, new_mark)

    return json.dumps({"resultCode": 0})


@app.route("/marks/<int:id_pupil>", methods=["GET"])
def get_marks(id_pupil):
    pupil = db.session.query(Pupil).filter(Pupil.id == id_pupil).first()

    return pupil.get_marks()
