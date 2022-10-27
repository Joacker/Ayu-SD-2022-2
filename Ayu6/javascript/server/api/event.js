"use strict";
const avro = require("avsc");

const schema = avro.Type.forSchema({
  type: "record",
  fields: [
    {
      name: "username",
      type: "string",
    },
    {
      name: "password",
      type: "string",
    },
    {
      name: "date",
      type: "string",
    },
  ],
});

module.exports = {
  schema,
};
