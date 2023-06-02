#!/usr/bin/node

const request = require('request');

function printCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;
      let characterCount = 0;

      function fetchCharacterData(characterUrl) {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            const characterName = characterData.name;
            console.log(characterName);

            characterCount++;
            if (characterCount === characters.length) {
              // All characters printed, script execution complete
              process.exit();
            }
          } else {
            console.log(`Failed to fetch character data: ${response.statusCode}`);
          }
        });
      }

      characters.forEach(fetchCharacterData);
    } else {
      console.log(`Failed to fetch film data: ${response.statusCode}`);
    }
  });
}

if (process.argv.length < 3) {
  console.log("Please provide a movie ID as a command line argument.");
} else {
  const movieId = process.argv[2];
  printCharacters(movieId);
}