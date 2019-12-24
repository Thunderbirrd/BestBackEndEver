from app import app
from flask import request, session
from db import db
import json

from models import SchoolClass


@app.route("/school_class/get_students_list", methods=["PUT"])
def get_students_list():
    class_name = request.form.get("name")
    subject = db.session.query(SchoolClass).filter(class_name == SchoolClass.name).first()
    return subject.get_students_list()


@app.route("/school_class/get_list_parents", methods=["PUT"])
def get_list_parents():
    class_name = request.form.get("name")
    subject = db.session.query(SchoolClass).filter(class_name == SchoolClass.name).first()
    return subject.get_list_parents()


@app.route("/school_class/get_timetable_class", methods=["PUT"])
def get_timetable_class():
    class_name = request.form.get("name")
    subject = db.session.query(SchoolClass).filter(class_name == SchoolClass.name).first()
    return subject.get_timetable_class()


@app.route("/school_class/set_timetable_class", methods=["PUT"])
def set_timetable_class():
    class_name = request.form.get("name")
    new_id = request.form.get("new timetable")
    subject = db.session.query(SchoolClass).filter(class_name == SchoolClass.name).first()
    subject.set_timetable_class(new_id)
    return json.dumps(
        {
            'resultCode': 0,
            'data': {
                'name': class_name,
                'new timetable_id': new_id
            }
        }
    )


@app.route("/school_class/set_students_list", methods=["PUT"])
def set_students_list():
    class_name = request.form.get("name")
    new_list = request.form.get("new list")
    subject = db.session.query(SchoolClass).filter(class_name == SchoolClass.name).first()
    subject.set_students_list(new_list)
    return json.dumps(
        {
            'resultCode': 0,
            'data': {
                'name': class_name,
                'new timetable_id': new_list
            }
        }
    )


@app.route("/school_class/add_student", methods=["PUT"])
def add_student():
    class_name = request.form.get("name")
    new_student = request.form.get("new student")
    subject = db.session.query(SchoolClass).filter(class_name == SchoolClass.name).first()
    subject.add_student(new_student)
    return json.dumps(
        {
            'resultCode': 0,
            'data': {
                'name': class_name,
                'new timetable_id': add_student
            }
        }
    )
