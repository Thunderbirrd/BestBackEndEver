from app import app
from flask import request, session
from db import db
import json

from models import Parent, Pupil, Teacher, SchoolClass


def auth():
    return session.get('auth') is not None


@app.route("/auth/logout", methods=["POST"])
def logout():
    session['auth'] = None
    return "somebody"


@app.route("/auth/pupil_login", methods=["GET"])
def pupil_login():

    if request.form:
        login = request.form.get("login")
        password = request.form.get("password")

        if len(login) < 8 or len(password) < 8:
            return json.dumps({'resultCode': 1})

        pupil = Pupil.auth(login, password)

        if pupil:
            session["auth"] = pupil.id
            return {
                "id": pupil.id,
                "name": pupil.name,
                "surname": pupil.surname,
                "clas": pupil.clas,
                "permit": pupil.permit,
                "login": pupil.login,
                "password": pupil.password,
                "position": pupil.position
            }
        else:
            return "Неправильный логин или пароль"


@app.route("/auth/teacher_login", methods=["GET"])
def teacher_login():
    if request.form:
        login = request.form.get("login")
        password = request.form.get("password")
        teacher = Teacher.auth(login, password)

        if teacher:
            session["auth"] = teacher.id
            return {
                "id": teacher.id,
                "name": teacher.name,
                "surname": teacher.surname,
                "permit": teacher.permit,
                "login": teacher.login,
                "password": teacher.password,
                "position": teacher.position,
                "qualification": teacher.qualification,
                "email": teacher.email,
                "phone": teacher.phone,
                "is_admin": teacher.is_admin
            }
        else:
            return "Неправильный логин или пароль"


@app.route("/auth/parent_login", methods=["GET"])
def parent_login():
    if request.form:
        login = request.form.get("login")
        password = request.form.get("password")
        parent = Parent.auth(login, password)

        if parent:
            session["auth"] = parent.id
            return {
                "id": parent.id,
                "name": parent.name,
                "surname": parent.surname,
                "login": parent.login,
                "password": parent.password,
                "position": parent.position,
                "child_id": parent.child__id
            }
        else:
            return "Неправильный логин или пароль"


@app.route("/auth/register", methods=["POST"])
def register():
    if request.form:
        login = request.form.get("login")
        password = request.form.get("password")
        name = request.form.get("name")
        surname = request.form.get("surname")
        position = request.form.get("position")

        if position == "Teacher":
            teacher = Teacher.auth(login, password)

            if teacher:
                return json.dumps({'resultCode': 1})

            email = request.form.get("email")
            phone = request.form.get("phone")
            qualification = request.form.get("qualification")

            teacher = Teacher(login, password, name, surname, qualification, phone, email, False)
            teacher.save()

            session["auth"] = teacher.id

            return json.dumps(
                {
                    'resultCode': 0,
                    'data': {
                        'userId': teacher.id,
                        'login': login,
                        'password': password,
                        'position': position,
                        'name': name,
                        'surname': surname,
                        'email ': email,
                        'phone ': phone,
                        'qualification ': qualification
                    }
                }
            )

        elif position == "Pupil":
            pupil = Pupil.auth(login, password)

            print(pupil)

            if pupil:
                return json.dumps({'resultCode': 1})

            clas = request.form.get('clas')
            pupil = Pupil(name, surname, login, password, clas)
            pupil.save()

            school_class = SchoolClass.get_class_by_name(clas)
            school_class.add_student(pupil.id)

            session["auth"] = pupil.id

            return json.dumps(
                {
                    'resultCode': 0,
                    'data': {
                        'userId': pupil.id,
                        'login': login,
                        'password': password,
                        'position': position,
                        'name': name,
                        'surname': surname,
                        'clas': clas
                    }
                }
            )

        elif position == "Parent":
            parent = Parent.auth(login, password)

            if parent:
                return json.dumps({'resultCode': 1})

            child_id = request.form.get("child_id")
            parent = Parent(name, surname, child_id, login, password)
            parent.save()

            session["auth"] = parent.id

            return json.dumps(
                {
                    'resultCode': 0,
                    'data': {
                        'userId': parent.id,
                        'login': login,
                        'password': password,
                        'position': position,
                        'name': name,
                        'surname': surname,
                        'child_id': child_id
                    }
                }
            )

        else:
            return json.dumps({'resultCode': 1})


