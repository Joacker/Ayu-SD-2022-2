cd /home/app/src/protobufs
python -m grpc_tools.protoc -I . --python_out=/home/app/src --grpc_python_out=/home/app/src ./search.proto