import redis, time
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

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