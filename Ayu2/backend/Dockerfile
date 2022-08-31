FROM python:3.8.10

WORKDIR /backend

ENV FLASK_APP main.py

ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt /backend

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["flask", "run"]