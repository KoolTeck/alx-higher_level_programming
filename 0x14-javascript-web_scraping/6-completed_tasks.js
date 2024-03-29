#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  const resp = JSON.parse(body);
  let count = 0;
  const userCompleted = {};
  resp.forEach(user => {
    const id = user.userId;
    userCompleted[id] = computeTask(id);
    count = 0;
  });
  function computeTask (id) {
    resp.forEach(user => {
      if (user.userId === id && user.completed) {
        count++;
      }
    });
    return count;
  }
  console.log(userCompleted);
});
