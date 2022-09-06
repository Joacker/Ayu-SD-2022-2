cd /backend/config
python -m grpc_tools.protoc -I config --python_out=. --grpc_python_out=. config/search.proto