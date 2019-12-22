from db import db
from flask import session
from datetime import datetime
from sqlalchemy import func, asc
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


class Teacher(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    permit = db.Column(db.Integer, unique=True)
    position = db.Column(db.String)
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
    students_list = db.Column(db.ARRAY)
    teacher = db.Column(db.Integer, key=Teacher.id)

    def __init__(self, name, students_list):
        self.name = name
        self.students_list = list(students_list)


class Pupil(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    permit = db.Column(db.Integer, unique=True)
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    school_class = db.Column(db.String, key=SchoolClass.name)

    def __init__(self, name, surname, clas):
        self.name = name
        self.surname = surname
        self.login = ""
        self.password = ""
        self.school_class = clas
        self.position = "Pupil"
        self.permit = int(str(self.id) + str(random.randint(1, 1000)))

    @staticmethod
    def auth(login, password):
        return db.session.query(Pupil).filter(Pupil.login == login).filter(Pupil.password == password).first()


class Parent(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    permit = db.Column(db.Integer, unique=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    child = db.Column(db.Integer, key=Pupil.id)
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    position = db.Column(db.String)

    def __init__(self, name, surname, child_id):
        self.name = name
        self.surname = surname
        self.login = ""
        self.password = ""
        self.child = child_id

    @staticmethod
    def auth(login, password):
        return db.session.query(Pupil).filter(Pupil.login == login).filter(Pupil.password == password).first()



