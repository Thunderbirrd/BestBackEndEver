from app import app
from flask import request, session
from db import db
import json
from models import Parent, Pupil, Teacher

#сюда будем записывать импорты файлов нашего api
import api.auth
import api.timetable


db.create_all()

import init_database


if __name__ == '__main__':
    app.run()
