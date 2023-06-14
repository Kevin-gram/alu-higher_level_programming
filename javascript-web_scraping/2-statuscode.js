#!/usr/bin/node
<<<<<<< HEAD
// A script that display the status code of a GET requestconst url = process.argv[2];
=======
// A script that display the status code of a GET request

const url = process.argv[2];
>>>>>>> c4279b0f9d3752da5081829d0369eef225eac971
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else console.log('code:', response && response.statusCode);
});
