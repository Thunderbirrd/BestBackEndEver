from db import db
from flask import session
from datetime import datetime
from sqlalchemy import func, asc
import json


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
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    permit = db.Column(db.Integer, unique=True)


class Parent(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    children = db.Column(db.ARRAY)

