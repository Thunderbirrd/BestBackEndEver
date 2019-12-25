from app import app
from flask import request, session
from db import db
import json
from models import Parent, Pupil, Teacher, SchoolClass

db.create_all()

#сюда будем записывать импорты файлов нашего api
import api.auth
import api.timetable
import api.marks
import init_database_timetable.class_1a
import init_database_timetable.class_2a
import init_database_timetable.class_3a
import init_database_timetable.class_4a
import init_database_timetable.class_5a
import init_database_timetable.class_6a
import init_database_timetable.class_7a
import init_database_timetable.class_8a
import init_database_timetable.class_9a
import init_database_timetable.class_10a
import init_database_timetable.class_11a


import init_database


if __name__ == '__main__':
    app.run()
