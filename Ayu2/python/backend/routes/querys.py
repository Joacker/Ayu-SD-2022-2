from psycopg2 import connect
from environs import Env

def init_db():
    env = Env()
    conn = connect(
        dbname=env('POSTGRES_DB'),
        user=env('POSTGRES_USER'),
        password=env('POSTGRES_PASSWORD'),
        host=env('POSTGRES_HOST')
    )
    return conn
