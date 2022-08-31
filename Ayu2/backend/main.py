import grpc
from concurrent import futures
import proto_message_pb2 as pb2
import proto_message_pb2_grpc as pb2_grpc
from time import sleep
from routes import querys

class SearchService(pb2_grpc.SearchServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        item = []
        response = []
        message = request.message
        result = f'"{message}" '
        cursor.execute("SELECT * FROM Items;")
        query_res = cursor.fetchall()
        for row in query_res:
            if message in row[1]:
                item.append(row)
        for i in item:
            result = dict()
            result['name'] = i[1]
            result['price']= i[2]
            result['category'] = i[3]
            result['count']= i[4]
            response.append(result)
        
        print(pb2.SearchResults(product=response))
        return pb2.SearchResults(product=response)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SearchServicer_to_server(SearchService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    sleep(20)
    conn = querys.init_db()
    cursor = conn.cursor()
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