from app import app
from repositories.courses import courses
import exercises
from flask import render_template, redirect, request, session


@app.route('/')
def index():
    return render_template("index.html", username=users.username())