#!/usr/bin/node
const process = require('process');
const request = require('request');

let characters = [];
const movieId = parseInt(process.argv[2]);

request(`https://swapi-api.hbtn.io/api/films/${movieId}/`, async (error, response, body) => {
  if (!error && response) {
    characters = await JSON.parse(body).characters;

    for (const character of characters) {
      await new Promise(function (resolve, reject) {
        request(character, (error, response, body) => {
          if (!error && response) {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  }
});
