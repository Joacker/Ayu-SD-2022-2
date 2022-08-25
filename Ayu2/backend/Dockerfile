FROM python:3.8.2-alpine

WORKDIR /backend

ENV FLASK_APP server.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache python3-pip gcc musl-dev linux-headers

COPY requirements.txt /server

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]