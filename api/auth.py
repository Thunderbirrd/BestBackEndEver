from app import app
import json


@app.route("/auth/logout")
def logout():
    return "somebody"


@app.route("/auth/login")
def login():
    return "somebody"


@app.route("/auth/register")
def register():
    return "somebody"
