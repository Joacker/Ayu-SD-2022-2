from flask import Flask, jsonify, request
from db.config import Config
from threading import Event
import signal
import json
import time 
import os

from flask_kafka.consumer import FlaskKafka
app = Flask(__name__)

INTERRUPT_EVENT = Event()

bus = FlaskKafka(INTERRUPT_EVENT,
                 bootstrap_servers=",".join(["kafka:9092"]),
                 group_id="consumer-grp-id"
                 )

# Register termination listener
def listen_kill_server():
    signal.signal(signal.SIGTERM, bus.interrupted_process)
    signal.signal(signal.SIGINT, bus.interrupted_process)
    signal.signal(signal.SIGQUIT, bus.interrupted_process)
    signal.signal(signal.SIGHUP, bus.interrupted_process)

counter = {}

def checkJSON():
    createJSONFile = False
    if os.path.isfile('/tmp/storage/blocked.json'):
        with open("/tmp/storage/blocked.json", "r") as jsonFile:
            temp = json.load(jsonFile)
        if not (type(temp) is dict):
            createJSONFile = True
        elif "users-blocked" not in list(temp.keys()):
            createJSONFile = True
        elif not (type(temp["users-blocked"]) is list):
            createJSONFile = True
    else:
        createJSONFile = True

    if createJSONFile:
        with open("/tmp/storage/blocked.json", "w") as jsonFile:
            json.dump({"users-blocked": []}, jsonFile)


# Handle message received from a Kafka topic
@bus.handle('login')
def process_real_time(msg):

    #print("consumed {} from test-topic".format(msg))
    val = msg.value.decode("ascii")
    temp = {"user": val, "date": msg.timestamp}
    
    if val in counter:
        current = int(time.time() * 1000)
        for item in counter[val]:
            print(item, current, current - item)
        x = [a for a in counter[val] if current - a < 60*1000]
        x.append(msg.timestamp)
        counter[val] = x
        if len(x) >=5:
            
            checkJSON()
            with open("/tmp/storage/blocked.json", "r") as jsonFile:
                temp = json.load(jsonFile)

            banned = set(temp["users-blocked"])
            
            banned.add(val)
            file_banned = list(banned)
            temp["users-blocked"] = file_banned
            with open("/tmp/storage/blocked.json", "w") as jsonFile:
                json.dump(temp, jsonFile)
    else:
        counter[val] = [msg.timestamp]
    



@app.route('/blocked', methods=['GET'])
def blocked():
    checkJSON()
    with open("/tmp/storage/blocked.json", "r") as jsonFile:
        temp = json.load(jsonFile)
    banned = temp["users-blocked"]
    return jsonify({"users-blocked": banned})   

if __name__ == '__main__':
    checkJSON()
    # Start consuming from the Kafka server
    bus.run()
    # Termination listener
    listen_kill_server()
    # Start Flask server
    app.run(host='0.0.0.0', debug=True, port=5000, threaded=True)