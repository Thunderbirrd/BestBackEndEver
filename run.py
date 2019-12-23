from app import app
from flask import request, session
from db import db
import json
from models import Parent, Pupil, Teacher

#сюда будем записывать импорты файлов нашего api
import api.auth


db.create_all()


if __name__ == '__main__':
    app.run()
