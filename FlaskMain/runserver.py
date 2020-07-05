"""
This script runs the BreastCancerMain application using a development server.
"""

from os import environ
from FlaskMain import app

if __name__ == '__main__':
    app.run("0.0.0.0", 8000)
