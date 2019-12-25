from app import app
from flask import request, session
from db import db
import json

from models import Pupil, SchoolClass, Subject, Teacher, TimetableDay


@app.route("/timetable/timetableClass/<int:id_pupil>", methods=["GET"])
def get_timetable_pupil(id_pupil):
    pupil = db.session.query(Pupil).filter(id_pupil == Pupil.id).first()
    clas = db.session.query(SchoolClass).filter(pupil.clas == SchoolClass.name).first()

    timetable = clas.get_timetable_class_list()

    return json.dumps(timetable)


@app.route("/timetable/timetableClass/teacher", methods=["PUT"])
def get_timetable_teacher():
    id_teacher = request.form.get("teacher_id")
    teacher = db.session.query(Teacher).filter(id_teacher == Teacher.id).first()
    subjects = list(db.session.query(Subject).filter(id_teacher == Subject.teacher_id).all())
    schedule = {}
    for subject in subjects:
        day1 = list(db.session.query(TimetableDay).filter(subject.id == TimetableDay.id_first_lesson).all())
        for day in day1:
            day_id = day.id
            s = f"{day_id % 5}"
            a = list(schedule.keys())
            if a.count(s) == 0:
                schedule[s] = "1"
            else:
                schedule[s] += " 1"

        day2 = list(db.session.query(TimetableDay).filter(subject.id == TimetableDay.id_second_lesson).all())
        for day in day2:
            day_id = day.id
            s = f"{day_id % 5}"
            a = list(schedule.keys())
            if a.count(s) == 0:
                schedule[s] = "2"
            else:
                schedule[s] += " 2"

        day3 = list(db.session.query(TimetableDay).filter(subject.id == TimetableDay.id_third_lesson).all())
        for day in day3:
            day_id = day.id
            s = f"{day_id % 5}"
            a = list(schedule.keys())
            if a.count(s) == 0:
                schedule[s] = "3"
            else:
                schedule[s] += " 3"

        day4 = list(db.session.query(TimetableDay).filter(subject.id == TimetableDay.id_fourth_lesson).all())
        for day in day4:
            day_id = day.id
            s = f"{day_id % 5}"
            a = list(schedule.keys())
            if a.count(s) == 0:
                schedule[s] = "4"
            else:
                schedule[s] += " 4"

        day5 = list(db.session.query(TimetableDay).filter(subject.id == TimetableDay.id_fifth_lesson).all())
        for day in day5:
            day_id = day.id
            s = f"{day_id % 5}"
            a = list(schedule.keys())
            if a.count(s) == 0:
                schedule[s] = "5"
            else:
                schedule[s] = " 5"

        day6 = list(db.session.query(TimetableDay).filter(subject.id == TimetableDay.id_sixth_lesson).all())
        for day in day6:
            day_id = day.id
            s = f"{day_id % 5}"
            a = list(schedule.keys())
            if a.count(s) == 0:
                schedule[s] = "6"
            else:
                schedule[s] += " 6"

        day7 = list(db.session.query(TimetableDay).filter(subject.id == TimetableDay.id_seventh_lesson).all())
        for day in day7:
            day_id = day.id
            s = f"{day_id % 5}"
            a = list(schedule.keys())
            if a.count(s) == 0:
                schedule[s] = "7"
            else:
                schedule[s] += " 7"

        day8 = list(db.session.query(TimetableDay).filter(subject.id == TimetableDay.id_eighth_lesson).all())
        for day in day8:
            day_id = day.id
            s = f"{day_id % 5}"
            a = list(schedule.keys())
            if a.count(s) == 0:
                schedule[s] = "8"
            else:
                schedule[s] += " 8"

    return json.dumps(
        {
            'teacher id': id_teacher,
            'timetable': schedule
        }
    )


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


@app.route("/timetable/get_homework", methods=["PUT"])
def get_homework():
    name_subject = request.form.get("subject")
    class_ = str(request.form.get("class"))
    subject = db.session.query(Subject).filter(name_subject == Subject.name and class_ == Subject.school_class_name).first()
    return subject.get_hw()


@app.route("/timetable/get_students_list", methods=["PUT"])
def get_students_list():
    name_subject = request.form.get("subject")
    class_ = str(request.form.get("class"))
    subject = db.session.query(Subject).filter(name_subject == Subject.name and class_ == Subject.school_class_name).first()
    return subject.get_students_list()


@app.route("/timetable/get_room", methods=["PUT"])
def get_room():
    name_subject = request.form.get("subject")
    class_ = str(request.form.get("class"))
    subject = db.session.query(Subject).filter(name_subject == Subject.name and class_ == Subject.school_class_name).first()
    return subject.get_class()


@app.route("/timetable/set_room", methods=["PUT"])
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
