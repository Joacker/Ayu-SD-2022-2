import redis, time, json, psycopg2, sys, grpc
from flask import Flask, jsonify, request
from psycopg2.extras import RealDictCursor
from concurrent import futures
from routes.querys import Database
import search_pb2_grpc
import search_pb2

app = Flask(__name__)

class Inventory(search_pb2_grpc.ItemService):
    
    def __init__(self, *args, **kwargs):
        pass
    
    def GetItem(self, request, context):
        print("[request]", request)
        name = request.name
        if name:
            list_of_elements = db.list_by_name(name)
        else:
            list_of_elements = db.list_of_elements()

        list_of_elements = [{
            "id": elem[0],
            "name":elem[1].strip(),
            "price": elem[2],
            "category": elem[3].strip(),
            "count": elem[4]
        }
            for elem in list_of_elements
        ]
        return search_pb2.Response(items=list_of_elements)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    search_pb2_grpc.add_ItemServiceServicer_to_server(Inventory(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    db = Database()
    print("listening...")
    serve()

''' def get_his_count():
    retries = 6
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
'''

''' @app.route('/')
def hello():
    count = get_his_count()
    return ('Hello World! I have been seen {} times.\n'.format(count))

@app.route('/about')
def about():
    return '<h1>About</h1>' '''