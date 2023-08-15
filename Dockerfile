FROM python:3.9-slim

COPY . /app

WORKDIR /app

RUN python3 -m venv myenv

RUN myenv/bin/pip install flask bcrypt PyMongo Flask-PyMongo

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["myenv/bin/python", "-m", "flask", "run", "--host=0.0.0.0"]