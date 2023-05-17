"""Setup at app startup"""
from flask import Flask 
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7l2d269vf5qb8f1a0-a.oregon-postgres.render.com",
        database="todo_czzw",
        user="root",
        password="kO05nAzkDW4pVQ56Dyyh6K59BNevaYwr")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
