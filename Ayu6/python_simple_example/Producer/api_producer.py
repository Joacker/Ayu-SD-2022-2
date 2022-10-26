import json
from time import time
from flask import Flask, render_template, request
from aiokafka import AIOKafkaProducer
import asyncio

app = Flask(__name__)
topic_list = []


async def send_one(message):
    producer = AIOKafkaProducer(
        bootstrap_servers='kafka:9092')
    await producer.start()
    try:
        await producer.send_and_wait("test", message)
    finally:
        await producer.stop()

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        message={'user': user, 'time_login': time()}
        message = json.dumps(message).encode('utf-8')
        asyncio.run(send_one(message))
    return render_template('index.html')
    

if __name__== "__main__":
    app.run(debug = True)
    
