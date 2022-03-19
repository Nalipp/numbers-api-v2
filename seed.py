from app import app
from database import db

# import all models - necessary for create_all()

db.drop_all(app=app)
db.create_all(app=app)
