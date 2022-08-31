import redis, time, json, psycopg2, sys, grpc
from flask import Flask, jsonify, request
from psycopg2.extras import RealDictCursor
from concurrent import futures

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

class ItemService(pb2_grpc.ItemServiceServicer):
    
    def __init__(self, *args, **kwargs):
        pass

    def queryDatabase(nombre): 
        
        largo=len(nombre)

        conn = psycopg2.connect(
            host="database",
            database="tiendita",
            user='postgres',
            password='marihuana'
        )

        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM items WHERE name LIKE '%"+nombre+"%'")
        
        row = cur.fetchall()

        val = json.dumps(row)

        conn.commit()

        cur.close()
        conn.close()

        return row


    def GetInventory(self, request, context):
        
        return pb2.Response(items=ItemService.queryDatabase(request.name))

def get_his_count():
    retries = 6
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_his_count()
    return ('Hello World! I have been seen {} times.\n'.format(count))

@app.route('/about')
def about():
    return '<h1>About</h1>'