# base image  
FROM python:3.10  

# set environment variables
ENV PYTHONUNBUFFERED 1 


WORKDIR  /app

COPY . /app

COPY requirements.txt app/

RUN pip install -r requirements.txt

EXPOSE 8000 
