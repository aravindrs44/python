from flask import render_template, request, session, redirect

from flask_app import app
from ..models.dojo import Dojo

@app.route(/ninjas)
def 