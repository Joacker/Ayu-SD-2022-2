import redis, time, json, psycopg2, sys, grpc
from flask import Flask, jsonify, request
from psycopg2.extras import RealDictCursor
from concurrent import futures
from backend import search_pb2_grpc as pb2_grpc
from backend import search_pb2 as pb2


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