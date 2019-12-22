from app import app
from flask import request, session
from db import db
import json

from models import Parent, Pupil, Teacher


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
        pupil = Pupil.auth(login, password)

        if pupil:
            session["auth"] = pupil.id
            return {
                "id": pupil.id,
                "name": pupil.name,
                "surname": pupil.surname
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
                "surname": teacher.surname
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
                "surname": parent.surname
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
        position = request.form.get("type")

        if position == "Teacher":
            teacher = Teacher.auth(login, password)

            if not teacher:
                return json.dumps({'resultCode': '1'})

            email = request.form.get("email")
            phone = request.form.get("phone")
            qualification = request.form.get("qualification")

            teacher = Teacher(name, surname, qualification, phone, email, False)
            teacher.save()

            session["auth"] = teacher.id

            return json.dumps(
                {
                    'resultCode': 1,
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
            pupil = Pupil(login, password)

            if not pupil:
                return json.dumps({'resultCode': '1'})

            clas = request.form.get("clas")
            pupil = Pupil(name, surname, login, password)
            pupil.save()

            session["auth"] = pupil.id

            return json.dumps(
                {
                    'resultCode': 1,
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
            parent = Parent(login, password)

            if not parent:
                return json.dumps({'resultCode': '1'})

            child_id = request.form.get("child_id")
            parent = Parent(name, surname, child_id, login, password)
            parent.save()

            session["auth"] = parent.id

            return json.dumps(
                {
                    'resultCode': 1,
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
