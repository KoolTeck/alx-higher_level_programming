#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  const res = JSON.parse(body).results;
  let count = 0;
  res.forEach(episode => {
    episode.characters.forEach(chars => {
      if (chars.endsWith('18/')) {
        count++;
      }
    });
  });
  console.log(count);
});
