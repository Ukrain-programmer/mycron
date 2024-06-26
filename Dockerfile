FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY /src ./src
COPY /config ./config

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD cd src && python3 main.py