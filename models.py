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
    permit = db.Column(db.Integer, unique=True)
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

        #if self.id is None: self.id = 1

        #self.permit = int(str(self.id) + str(random.randint(1, 1000)))
        self.marks = ""
        self.clas = clas

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

    def __init__(self, name, surname, qualification, phone, email):
        self.name = name
        self.surname = surname
        self.login = ""
        self.password = ""
        self.qualification = qualification
        self.phone = phone
        self.email = email
        self.position = "Teacher"
        #self.permit = int(str(self.id) + str(random.randint(1, 1000)))

    @staticmethod
    def auth(login, password):
        return db.session.query(Teacher).filter(Teacher.login == login).filter(Teacher.password == password).first()


class SchoolClass(db.Model, Model):
    name = db.Column(db.String, primary_key=True, unique=True)
    students_list = db.Column(db.String, db.ForeignKey(Pupil.id))
    teacher_id = db.Column(db.Integer, db.ForeignKey(Teacher.id))

    def __init__(self, name, students_list, teacher_id):
        self.name = name
        self.students_list = list(students_list)
        self.teacher_id = teacher_id

    teacher = db.relationship(Teacher)

    def get_students_list(self):
        return list(str(self.students_list).split(" "))

    def get_list_parents(self):
        list_parents = []

        for student in self.students_list:
            list_parents.append(db.session.query(Parent).filter(Parent.child == student.id).first())

        return list_parents


class Subject(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    type = db.Column(db.String)  #subject || section || elective
    students_list = db.Column(db.String, db.ForeignKey(Pupil.id))
    teacher_id = db.Column(db.Integer, db.ForeignKey(Teacher.id))
    homework = db.Column(db.String)

    def __init__(self, group, name, students_list, teacher_id):
        self.type = group
        self.name = name
        self.students_list = list(students_list)
        self.homework = ""
        self.teacher_id = teacher_id

    teacher = db.relationship(Teacher)

    def get_students_list(self):
        return list(str(self.students_list).split(" "))


class Parent(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    child__id = db.Column(db.Integer, db.ForeignKey(Pupil.id))
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    position = db.Column(db.String)

    def __init__(self, name, surname, child_id, login, password):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.child = child_id

    child = db.relationship(Pupil)

    @staticmethod
    def auth(login, password):
        return db.session.query(Parent).filter(Parent.login == login).filter(Parent.password == password).first()


class School:
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String)
    classes = db.Column(db.String, db.ForeignKey(SchoolClass.name))
    pupils = db.Column(db.String, db.ForeignKey(Pupil.id))
    teachers = db.Column(db.String, db.ForeignKey(Teacher.id))

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
