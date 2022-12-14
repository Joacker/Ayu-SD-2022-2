const grpc = require("@grpc/grpc-js");
const PROTO_PATH = "./src/controllers/searchInventory.proto"
var redis = require('redis')
var protoLoader = require("@grpc/proto-loader");

const options = {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
};

// -------CONFIGURACION DE REDIS EN 3 CLIENTES-------
const redis_client = redis.createClient({
    url:"redis://redis1"
});

const redis_client2 = redis.createClient({
    url:"redis://redis2"
});

const redis_client3 = redis.createClient({
    url:"redis://redis3"
});

// -------VALIDACIÓN DE CONEXIÓN DE REDIS EN 3 CLIENTES-------
redis_client.on('ready',()=>{
    console.log("Redis1 listo")
    console.log("-------------------------------------------------------------------------------------------------------------")
})

redis_client2.on('ready',()=>{
    console.log("Redis2 listo")
    console.log("-------------------------------------------------------------------------------------------------------------")
})

redis_client3.on('ready',()=>{
    console.log("Redis3 listo")
    console.log("-------------------------------------------------------------------------------------------------------------")
})

// -------CONEXIÓN MICROSERVICIOS CLIENTES DE REDIS-------
redis_client.connect()
redis_client2.connect()
redis_client3.connect()



console.log('Redis conection: '+redis_client.isOpen);
console.log('Redis conection: '+redis_client2.isOpen);
console.log('Redis conection: '+redis_client3.isOpen);


var packageDefinition = protoLoader.loadSync(PROTO_PATH, options);

const InventorySearch= grpc.loadPackageDefinition(packageDefinition).InventorySearch;

const client = new InventorySearch(
    "grpc_server:50051",
    grpc.credentials.createInsecure()
  );

const searchitems=(req,res)=>{
    const busqueda=req.query.q
    let cache = null;
    (async () => {
        let reply = await redis_client.get(busqueda);
            if(reply){
                cache = JSON.parse(reply);
                console.log("Busqueda: "+busqueda)
                console.log("Encontrado en Caché!")
                console.log("Resultados:")
                var string_total=""
                for (i in cache['product']){
                var id=cache['product'][i].id
                var name=cache['product'][i].name
                var price=cache['product'].price
                var category=cache['product'][i].category
                var count=cache['product'][i].count
                const stringsumar='id: '+id+' | name:'+name+' | price:'+price+' | category:'+category+' | count:'+count
                string_total=string_total+stringsumar+'\n'
                }
                console.log(string_total)
                console.log("--------------------------------------------------------------------------------------------------------------------------------")


                res.status(200).json(cache)
            }
            else{
                console.log("Busqueda: "+busqueda)
                console.log("No se ha encontrado en Caché, Buscando en Postgres...")
                client.GetServerResponse({message:busqueda}, (error,items) =>{
                    if(error){
                        
                        res.status(400).json(error);
                    }
                    else{
                        data = JSON.stringify(items)
                        if (data['product']!==null){
                        redis_client.set(busqueda,data)
                        res.status(200).json(items);}
                        

                        
            
                    }
                });
            } 
    })();
}





module.exports={
 searchitems
}