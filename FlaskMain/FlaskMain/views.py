"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FlaskMain import app
import requests


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        size = request.form["size"]
        clusters = request.form["clusters"]
        print(size)
        URL = "http://flask-clustering:9000/home"
        PARAMS = {'size':size,'clusters':clusters} 
        r = requests.get(url = URL, params = PARAMS) 
        return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        plot = r.content.decode('utf-8').replace('\n', '')
    )
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        plot = ''
    )
