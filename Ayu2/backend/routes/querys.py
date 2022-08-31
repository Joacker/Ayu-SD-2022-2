import string
import psycopg2
from psycopg2._psycopg import connection
from environs import Env


class Database:
    def __init__(self) -> None:
        self.conn = False
        pass

    def connectionDB(self) -> connection:
        env = Env()
        env.read_env()
        if self.conn:
            return self.conn
        else:
            self.conn = psycopg2.connect(
                dbname=env('POSTGRES_DB'),
                user=env('POSTGRES_USER'),
                password=env('POSTGRES_PASSWORD'),
                host=env('POSTGRES_HOST')
            )
            return self.conn

    def list_of_elements(self) -> list[tuple[str]]:
        cursor: psycopg2.cursor = self.connectionDB().cursor()
        cursor.execute("""SELECT * FROM items;""")
        fet = cursor.fetchall()
        return fet

    def list_by_name(self, name_product: str) -> list[tuple[str]]:

        cursor = self.connectionDB().cursor()
        cursor.execute(
            f"""SELECT * FROM items WHERE name ILIKE '%{name_product}%' ;""")
        fet = cursor.fetchall()
        return fet