FROM bitnami/python:3.8.13

RUN pip install flask
RUN pip install kafka-python
RUN pip install aiokafka
ENV FLASK_APP=api_producer.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

EXPOSE 8000
COPY . .
CMD ["flask", "run"]