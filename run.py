from app import app
from db import db
import models

db.create_all()

if __name__ == '__main__':
    app.run(host='localhost')
