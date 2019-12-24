from db import db
from flask import session
from datetime import datetime
from sqlalchemy import func, asc, select
import json
import random


class Model:
    errors = []

    def validate(self):
        self.errors = []
        return len(self.errors) == 0

    def save(self):
        if self.validate():
            print(self.id)
            if self.id is None:
                db.session.add(self)
                print(2)
            db.session.commit()
            return True
        else:
            return False


class Pupil(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    permit = db.Column(db.String, unique=True)
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    position = ""
    marks = db.Column(db.JSON)
    clas = db.Column(db.String)

    def __init__(self, name, surname, login, password, clas):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.position = "Pupil"
        self.permit = self.login + str(random.randint(1, 10000000))
        self.marks = ""
        self.clas = clas

    @staticmethod
    def auth(login, password):
        return db.session.query(Pupil).filter(Pupil.login == login).filter(Pupil.password == password).first()


class Teacher(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    permit = db.Column(db.String, unique=True)
    position = ""
    qualification = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    phone = db.Column(db.Integer)
    email = db.Column(db.Integer)
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean)

    def __init__(self, login, password, name, surname, qualification, phone, email, is_admin):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.qualification = qualification
        self.phone = phone
        self.email = email
        self.position = "Teacher"
        self.permit = self.login + str(random.randint(1, 10000000))
        self.is_admin = is_admin

    def set_admin(self, is_ad):
        self.is_admin = is_ad
        self.save()

    @staticmethod
    def auth(login, password):
        return db.session.query(Teacher).filter(Teacher.login == login).filter(Teacher.password == password).first()


class Subject(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    type = db.Column(db.String)  #subject || section || elective
    students_list = db.Column(db.String, db.ForeignKey(Pupil.id))
    teacher_id = db.Column(db.Integer, db.ForeignKey(Teacher.id))
    homework = db.Column(db.String)
    name = db.Column(db.String)
    classroom = db.Column(db.String)

    def __init__(self, type_, name, students_list, teacher_id, room):
        self.type = type_
        self.name = name
        self.students_list = students_list
        self.homework = ""
        self.teacher_id = teacher_id
        self.classroom = str(room)

    teacher = db.relationship(Teacher)

    def get_students_list(self):
        return list(str(self.students_list).split(" "))

    def set_homework(self, new_homework):
        self.homework = new_homework
        self.save()

    def get_hw(self):
        return self.homework

    def get_class(self):
        return self.classroom

    def set_class(self, cl):
        self.classroom = cl
        self.save()

    @staticmethod
    def get_by_name_and_teacher(name, teacher_id):
        return db.session.query(Subject).filter(Subject.name == name).filter(Subject.teacher_id == teacher_id).first()


class Parent(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    child_id = db.Column(db.Integer, db.ForeignKey(Pupil.id))
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    position = db.Column(db.String)

    def __init__(self, name, surname, child_id, login, password):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.child_id = child_id

    child = db.relationship(Pupil)

    @staticmethod
    def auth(login, password):
        return db.session.query(Parent).filter(Parent.login == login).filter(Parent.password == password).first()


class TimetableDay(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    id_first_lesson = db.Column(db.Integer, db.ForeignKey(Subject.id))
    id_second_lesson = db.Column(db.Integer, db.ForeignKey(Subject.id))
    id_third_lesson = db.Column(db.Integer, db.ForeignKey(Subject.id))
    id_fourth_lesson = db.Column(db.Integer, db.ForeignKey(Subject.id))
    id_fifth_lesson = db.Column(db.Integer, db.ForeignKey(Subject.id))
    id_sixth_lesson = db.Column(db.Integer, db.ForeignKey(Subject.id))
    id_seventh_lesson = db.Column(db.Integer, db.ForeignKey(Subject.id))
    id_eighth_lesson = db.Column(db.Integer, db.ForeignKey(Subject.id))

    def __init__(self, id1, id2, id3, id4, id5, id6, id7, id8):
        self.id_first_lesson = id1
        self.id_second_lesson = id2
        self.id_third_lesson = id3
        self.id_fourth_lesson = id4
        self.id_fifth_lesson = id5
        self.id_sixth_lesson = id6
        self.id_seventh_lesson = id7
        self.id_eighth_lesson = id8

    def get_first_lesson(self):
        return db.session.query(Subject).filter(Subject.id == self.id_first_lesson).first()

    def get_second_lesson(self):
        return db.session.query(Subject).filter(Subject.id == self.id_second_lesson).first()

    def get_third_lesson(self):
        return db.session.query(Subject).filter(Subject.id == self.id_third_lesson).first()

    def get_fourth_lesson(self):
        return db.session.query(Subject).filter(Subject.id == self.id_fourth_lesson).first()

    def get_fifth_lesson(self):
        return db.session.query(Subject).filter(Subject.id == self.id_fifth_lesson).first()

    def get_sixth_lesson(self):
        return db.session.query(Subject).filter(Subject.id == self.id_sixth_lesson).first()

    def get_seventh_lesson(self):
        return db.session.query(Subject).filter(Subject.id == self.id_seventh_lesson).first()

    def get_eighth_lesson(self):
        return db.session.query(Subject).filter(Subject.id == self.id_eighth_lesson).first()

    def set_first(self, f):
        self.id_first_lesson = f
        self.save()

    def set_second(self, s):
        self.id_second_lesson = s
        self.save()

    def set_third(self, t):
        self.id_third_lesson = t
        self.save()

    def set_fourth(self, f):
        self.id_fourth_lesson = f
        self.save()

    def set_fifth(self, f):
        self.id_fifth_lesson = f
        self.save()

    def set_sixth(self, s):
        self.id_sixth_lesson = s
        self.save()

    def set_seventh(self, s):
        self.id_seventh_lesson = s
        self.save()

    def set_eighth(self, e):
        self.id_eighth_lesson = e
        self.save()

    def get_all_lesson(self):
        first_lesson = self.get_first_lesson()
        second_lesson = self.get_second_lesson()
        third_lesson = self.get_third_lesson()
        fourth_lesson = self.get_fourth_lesson()
        fifth_lesson = self.get_fifth_lesson()
        sixth_lesson = self.get_sixth_lesson()
        seventh_lesson = self.get_seventh_lesson()
        eighth_lesson = self.get_eighth_lesson()

        return {
            first_lesson,
            second_lesson,
            third_lesson,
            fourth_lesson,
            fifth_lesson,
            sixth_lesson,
            seventh_lesson,
            eighth_lesson
        }

    @staticmethod
    def get_by_id(id_day):
        return db.session.query(TimetableDay).filter(TimetableDay.id == id_day).first()


class TimetableClass(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    id_monday = db.Column(db.Integer, db.ForeignKey(TimetableDay.id))
    id_tuesday = db.Column(db.Integer, db.ForeignKey(TimetableDay.id))
    id_wednesday = db.Column(db.Integer, db.ForeignKey(TimetableDay.id))
    id_thursday = db.Column(db.Integer, db.ForeignKey(TimetableDay.id))
    id_friday = db.Column(db.Integer, db.ForeignKey(TimetableDay.id))

    def __int__(self, id1, id2, id3, id4, id5):
        self.id_monday = id1
        self.id_tuesday = id2
        self.id_wednesday = id3
        self.id_thursday = id4
        self.id_friday = id5

    def get_monday_timetable(self):
        return (db.session.query(TimetableDay).filter(TimetableDay.id == self.id_monday).first()).get_all_lesson()

    def get_tuesday_timetable(self):
        return db.session.query(TimetableDay).filter(TimetableDay.id == self.id_tuesday).first().get_all_lesson()

    def get_wednesday_timetable(self):
        return db.session.query(TimetableDay).filter(TimetableDay.id == self.id_wednesday).first().get_all_lesson()

    def get_thursday_timetable(self):
        return db.session.query(TimetableDay).filter(TimetableDay.id == self.id_thursday).first().get_all_lesson()

    def get_friday_timetable(self):
        return db.session.query(TimetableDay).filter(TimetableDay.id == self.id_friday).first().get_all_lesson()

    def set_monday(self, new):
        self.id_monday = new
        self.save()

    def set_tuesday(self, new):
        self.id_tuesday = new
        self.save()

    def set_wednesday(self, new):
        self.id_wednesday = new
        self.save()

    def set_thursday(self, new):
        self.id_thursday = new
        self.save()

    def set_friday(self, new):
        self.id_friday = new
        self.save()

    def get_all_day_timetable(self):
        return {
            'monday': self.get_monday_timetable(),
            'tuesday': self.get_tuesday_timetable(),
            'wednesday': self.get_wednesday_timetable(),
            'thursday': self.get_thursday_timetable(),
            'friday': self.get_friday_timetable()
        }

    @staticmethod
    def get_by_id(id_timetable_class):
        return db.session.query(TimetableClass).filter(TimetableClass.id == id_timetable_class).first()


class SchoolClass(db.Model, Model):
    name = db.Column(db.String, primary_key=True, unique=True)
    students_list = db.Column(db.String)
    teacher_id = db.Column(db.Integer, db.ForeignKey(Teacher.id))
    id_timetable_class = db.Column(db.Integer, db.ForeignKey(TimetableClass.id))

    def __init__(self, name, students_list, teacher_id):
        self.name = name
        self.students_list = students_list
        self.teacher_id = teacher_id

    teacher = db.relationship(Teacher)

    def get_students_list(self):
        return list(str(self.students_list).split(" "))

    def get_list_parents(self):
        list_parents = []

        for student in list(str(self.students_list).split(" ")):
            list_parents.append(db.session.query(Parent).filter(Parent.child_id == int(student)).first())

        return list_parents

    def get_timetable_class(self):
        timetable_class = db.session.query(TimetableClass).filter(self.id_timetable_class == TimetableClass.id).first()
        return timetable_class.get_all_day_timetable()

    def set_timetable_class(self, new):
        self.id_timetable_class = new
        self.save()


class HomeworkClassBySubject(db.Model, Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    name_of_class = db.Column(db.String, db.ForeignKey(SchoolClass.name))
    id_of_teacher = db.Column(db.String, db.ForeignKey(Subject.teacher_id))
    name_of_subject = db.Column(db.String, db.ForeignKey(Subject.name))
    text_homework = db.Column(db.String)

    def __init__(self, name_of_class, id_of_teacher, name_of_subject, text_homework):
        self.name_of_class = name_of_class
        self.id_of_teacher = id_of_teacher
        self.name_of_subject = name_of_subject
        self.text_homework = text_homework

    def get_homework(self):
        return self.text_homework

    def set_homework(self, new_homework):
        self.text_homework = new_homework
        self.save()


class School(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String)
    classes = db.Column(db.String, db.ForeignKey(SchoolClass.name))
    pupils = db.Column(db.String)
    teachers = db.Column(db.String)

    def __init__(self, name, address, classes, teachers, pupils):
        self.name = name
        self.address = address
        self.classes = classes
        self.teachers = teachers
        self.pupils = pupils

    def get_list_teachers(self):
        return list(str(self.teachers).split(" "))

    def get_list_classes(self):
        return list(str(self.classes).split(" "))

    def get_list_pupils(self):
        return list(str(self.pupils).split(" "))
