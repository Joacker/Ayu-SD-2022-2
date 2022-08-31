FROM bitnami/python:3.8.13

WORKDIR /client

COPY proto_message.proto ./

RUN python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./search.proto

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
COPY . .
CMD ["flask", "run"]