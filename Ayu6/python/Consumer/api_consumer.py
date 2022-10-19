import json
from flask import Flask, render_template, redirect
from aiokafka import AIOKafkaConsumer
import asyncio

app = Flask(__name__)
message = ''
usuarios = {}
users_blocked = []

def is_blocked(msg):
    
    if msg['user'] in users_blocked:
        return
    elif msg['user'] not in usuarios:
        usuarios[msg['user']] = [msg['time_login'], 5, 0]
    else:
        if (msg['time_login'] - usuarios[msg['user']][0] <= 60) and (usuarios[msg['user']][1]-1 == 0):
            usuarios[msg['user']] = [msg['time_login'],0,1]
            get_blocked(msg['user'])
        else:
            if (msg['time_login'] - usuarios[msg['user']][0] <= 60):
                usuarios[msg['user']] = [usuarios[msg['user']][0],usuarios[msg['user']][1]-1,0]
            else:
                usuarios[msg['user']] = [msg['time_login'], 5, 0]
    return

def get_blocked(usuario):

    users_blocked.append(usuario)

def view_blocked():
    return users_blocked    

async def consume():
    consumer = AIOKafkaConsumer(
        'test',
        bootstrap_servers='kafka:9092')
    await consumer.start()
    try:
        async for msg in consumer:
            is_blocked(json.loads(msg.value))
            return json.loads(msg.value)
    finally:
        await consumer.stop()

@app.route('/')
def index():
    return redirect('blocked')

@app.route('/blocked')
def blocked():
    asyncio.run(consume())
    users_blocked = view_blocked()
    return render_template('blocked.html', values= users_blocked)
    
if __name__== "__main__":
    app.run(debug = True)
    
