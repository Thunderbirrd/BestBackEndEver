from app import app
from flask import request, session
import json

from models import Parent, Pupil, Teacher


@app.route("/auth/logout", methods=["POST"])
def logout():
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


@app.route("/auth/register", methods=["POST"])
def register():
    if request.form:
        login = request.form.get("login")
        password = request.form.get("password")
        name = request.form.get("name")
        surname = request.form.get("surname")
        type = request.form.get("type")

        if type == "Teacher":
            email = request.form.get("email")
            phone = request.form.get("phone")
            qualification = request.form.get("qualification")
            teacher = Teacher(name, surname, qualification, phone, email, False)
            teacher.save()

        elif type == "Pupil":
            clas = request.form.get("clas")
            pupil = Pupil(name, surname, login, password)
            pupil.save()

        elif type == "Parent":
            child_id = request.form.get("child_id")
            parent = Parent(name, surname, child_id, login, password)
            parent.save()

    return "somebody"
