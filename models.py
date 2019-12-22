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
            if self.id is None:
                db.session.add(self)
            db.session.commit()
            return True
        else:
            return False


class Pupil(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    permit = db.Column(db.Integer, unique=True)
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    position = ""
    marks = db.Column(db.JSON)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.login = ""
        self.password = ""
        self.position = "Pupil"
        self.permit = int(str(self.id) + str(random.randint(1, 1000)))
        self.marks = ""

    @staticmethod
    def auth(login, password):
        return db.session.query(Pupil).filter(Pupil.login == login).filter(Pupil.password == password).first()


class Teacher(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    permit = db.Column(db.Integer, unique=True)
    position = ""
    qualification = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    phone = db.Column(db.Integer)
    email = db.Column(db.Integer)
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean)

    def __init__(self, name, surname, qualification, phone, email, is_admin):
        self.name = name
        self.surname = surname
        self.login = ""
        self.password = ""
        self.qualification = qualification
        self.phone = phone
        self.email = email
        self.is_admin = is_admin
        self.position = "Teacher"
        self.permit = int(str(self.id) + str(random.randint(1, 1000)))

    @staticmethod
    def auth(login, password):
        return db.session.query(Pupil).filter(Pupil.login == login).filter(Pupil.password == password).first()


class SchoolClass(db.Model, Model):
    name = db.Column(db.String, primary_key=True, unique=True)
    students_list = db.Column(db.ARRAY, db.ForeignKey(Pupil.id))
    teacher_id = db.Column(Teacher, db.ForeignKey(Teacher.id))

    def __init__(self, name, students_list, teacher_id):
        self.name = name
        self.students_list = list(students_list)
        self.teacher_id = teacher_id

    teacher = db.relationship(Teacher)

    def get_students_list(self):
        return self.students_list

    def get_list_parents(self):
        list_parents = []

        for student in self.students_list:
            list_parents.append(db.session.query(Parent).filter(Parent.child == student.id).first())

        return list_parents


class Subject(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    type = db.Column(db.String)  #subject || section || elective
    students_list = db.Column(db.ARRAY)
    teacher_id = db.Column(Teacher, db.ForeignKey(Teacher.id))
    homework = db.Column(db.String)

    def __init__(self, type,  name, students_list, teacher_id):
        self.type = type
        self.name = name
        self.students_list = list(students_list)
        self.homework = ""
        self.teacher_id = teacher_id

    teacher = db.relationship(Teacher)

    def get_students_list(self):
        return self.students_list


class Parent(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    child__id = db.Column(db.Integer, db.ForeignKey(Pupil.id))
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    position = db.Column(db.String)

    def __init__(self, name, surname, child_id):
        self.name = name
        self.surname = surname
        self.login = ""
        self.password = ""
        self.child = child_id

        child = db.relationship(Pupil)

    @staticmethod
    def auth(login, password):
        return db.session.query(Pupil).filter(Pupil.login == login).filter(Pupil.password == password).first()


class School:
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String)
    classes = db.Column(db.ARRAY, db.ForeignKey(SchoolClass.name))
    pupils = db.Column(db.ARRAY, db.ForeignKey(Pupil.id))
    teachers = db.Column(db.ARRAY, db.ForeignKey(Teacher.id))

    def __init__(self, name, address, classes, teachers, pupils):
        self.name = name
        self.address = address
        self.classes = classes
        self.teachers = teachers
        self.pupils = pupils

    def get_list_teachers(self):
        return self.teachers

    def get_list_classes(self):
        return self.classes

    def get_list_pupils(self):
        return self.pupils
