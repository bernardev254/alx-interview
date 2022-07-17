#!/usr/bin/node
const process = require('process');
const request = require('request');

let characters = [];
const movieId = parseInt(process.argv[2]);

request(`https://swapi-api.hbtn.io/api/films/${movieId}/`, (error, response, body) => {
  if (!error && response) {
    characters = JSON.parse(body).characters;

    for (let idx = 0; idx < characters.length; idx++) {
      request(characters[idx], (error, response, body) => {
        if (!error && response) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
