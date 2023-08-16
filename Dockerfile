#
# FROM python:3.8-slim-buster
#
# WORKDIR /app
#
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
#
# COPY . .
#
# CMD ["python", "app/app.py"]
FROM python:3.9-slim

COPY . /app

WORKDIR /app

RUN python3 -m venv myenv

RUN myenv/bin/pip install flask bcrypt PyMongo Flask-PyMongo Flask-RESTful

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["myenv/bin/python", "-m", "flask", "run", "--host=0.0.0.0"]