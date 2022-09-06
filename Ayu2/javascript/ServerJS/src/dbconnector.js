const {Pool} = require('pg');

const connectionData = {
    user:'postgres',
    host:'postgres',
    database:'tiendita',
    password:'marihuana',
    port:5432
}

const client = new Pool(connectionData)

module.exports = {client};