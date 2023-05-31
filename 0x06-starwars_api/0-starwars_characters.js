#!/usr/bin/node

const axios = require('request');

// Function to fetch movie details
async function fetchMovieCharacters(movieId) {
  try {
    // Fetch movie details using the Star Wars API
    const response = await request.get(`https://swapi.dev/api/films/${movieId}/`);

    // Extract the characters array from the response
    const characters = response.data.characters;

    // Fetch and print character names
    for (const characterUrl of characters) {
      const characterResponse = await request.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Call the function with the movie ID as the command-line argument
const movieId = process.argv[2];
fetchMovieCharacters(movieId);