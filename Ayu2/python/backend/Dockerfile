FROM python:3.8.10

WORKDIR /backend

COPY requirements.txt /backend

RUN pip3 install -r requirements.txt

COPY . .

RUN python3 -m grpc_tools.protoc -I config --python_out=. --grpc_python_out=. config/proto_message.proto

EXPOSE 3000

CMD ["python3", "-u", "main.py"]