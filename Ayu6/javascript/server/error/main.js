'use strict';
/* IMPORTS */
const express = require('express')
const cors = require('cors')
const dotenv = require('dotenv')
const bodyParser = require('body-parser')
const { Kafka } = require("kafkajs");

//-------------------------------------------

/* CONFIGS */
//server.server();
const app = express()
dotenv.config()
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json())
app.use(cors())

var port = process.env.PORT || 8000;
var host = process.env.PORT || '0.0.0.0';

var kafka = new Kafka({
  clientId: "my-app",
  brokers: ["kafka:9092"],
});
const consumer = kafka.consumer({ groupId: "test-group" });

app.get('/', (req, res) => {
  res.send('ola api-block')
})

var value = null
var json = {}
var registro = {};
var bloqueados = [];

const main = async () => {
  console.log("Entra main")
  await consumer.connect();
  await consumer.subscribe({ topic: "test-topic", fromBeginning: true });
  console.log("producer");

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      value = message.value
      console.log({
        value: message.value.toString(),
      })
      json = JSON.parse(value)
      //console.log(json["tiempo"])
      let find = json["username"]
      if(bloqueados.includes(json["username"]))
      {
        let word = json["username"]
        //res.json(word+" bloqueado")
        console.log("ta bloqueado sorry :(")
        //return
      }else{
        if(!(json["username"] in registro)){
          var array = []
          registro[json["username"]] = array
          registro[json["username"]].push(json["tiempo"])
        }else{
          registro[json["username"]].push(json["tiempo"])
        }
        //console.log(registro[json["username"]])
        //console.log(registro[json["username"]].length)
        if(registro[json["username"]].length >= 5 && registro[json["username"]][registro[json["username"]].length -1] - registro[json["username"]][registro[json["username"]].length -5] <60){
          //console.log(registro[json["username"]][registro[json["username"]].length -1] - registro[json["username"]][registro[json["username"]].length -5])
          console.log("Bloqueado")
          bloqueados.push(json["username"])
          console.log(bloqueados)
        }
      }
    },
  })
  .catch(console.error)
};

//asdlaskdj
app.get('/blocked', (req, res) => {
  res.send(bloqueados)
})
/* PORTS */

app.listen(port,host,()=>{
    console.log(`API-Blocked run in: http://localhost:${port}.`)
    main()
});