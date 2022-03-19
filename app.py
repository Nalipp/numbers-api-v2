import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from database import connect_db
from trivia.routes import trivia
from maths.routes import math
from dates.routes import dates
from years.routes import years

# load .env environment variables
load_dotenv()

# create app and add configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# register blueprints
app.register_blueprint(trivia, url_prefix='/api/trivia')
app.register_blueprint(math, url_prefix='/api/math')
app.register_blueprint(dates, url_prefix='/api/date')
app.register_blueprint(years, url_prefix='/api/year')

# allow CORS and connect app to database
CORS(app)
connect_db(app)
