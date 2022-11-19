#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  console.log('code:', response.statusCode);
});
