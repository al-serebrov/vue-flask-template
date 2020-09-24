FROM python:3

RUN pip install virtualenv

WORKDIR /backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
