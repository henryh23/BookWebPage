FROM python:3.8

EXPOSE 5000

WORKDIR /henry_app

COPY requirements.txt /henry_app
RUN pip install -r requirements.txt

# Create env variables for database connection
ENV MM_DATABASE_HOST=db
ENV MM_DATABASE_NAME=test
ENV MM_DB_USER=root
ENV MM_DB_PASSWORD=root

COPY app.py /henry_app
CMD python app.py