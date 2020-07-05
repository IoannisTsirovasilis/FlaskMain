FROM python:3.7

WORKDIR /opt/FlaskMain
COPY . .
RUN pip install -r /opt/FlaskMain/FlaskMain/requirements.txt

EXPOSE 8000

CMD ["python", "/opt/FlaskMain/FlaskMain/runserver.py"]
