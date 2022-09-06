const grpc = require("@grpc/grpc-js");
const PROTO_PATH = "./searchInventory.proto"
var protoLoader = require("@grpc/proto-loader");
const { client } = require("./src/dbconnector");

const options = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
};

var packageDefinition = protoLoader.loadSync(PROTO_PATH, options);
const a = grpc.loadPackageDefinition(packageDefinition);

const server = new grpc.Server();

server.addService(a.InventorySearch.service, {
  GetServerResponse: (call, callback) => {
    const busqueda = call.request.message;

    client.connect((err, client, release) => {
      if (err) {
        return console.error('Error acquiring client', err.stack)
      }
      client.query(`select * from items where name like '%' || $1 || '%';`, [busqueda], (err, result) => {
        release()
        if (err) {
          return console.error('Error executing query', err.stack)
        }

        console.log("Resultados:")
        var string_total = ""
        for (i in result.rows) {
          var { id, name, price, category, count } = result.rows[i];
          var id = result.rows[i].id
          var name = result.rows[i].name
          var price = result.rows[i].price
          var category = result.rows[i].category
          var count = result.rows[i].count
          const stringsumar = 'id: ' + id + ' | name:' + name + ' | price:' + price + ' | category:' + category + ' | count:' + count
          string_total = string_total + stringsumar + '\n'
        }
        if (string_total == "") {
          string_total = "No hay resultados..."
          callback(null, null);
        }
        else {
          callback(null, { product: result.rows });
        }
        console.log(string_total)
        console.log("--------------------------------------------------------------------------------------------------------------------------------")


      })
    })
  },
});

server.bindAsync(
  "0.0.0.0:50051",
  grpc.ServerCredentials.createInsecure(),
  (error, port) => {
    console.log("Server running at http://127.0.0.1:50051");
    server.start();
  }
);