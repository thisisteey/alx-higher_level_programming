// Script that fetches and lists the title for all movies by using an API url
'use strict';
$(() => {
  const API_URL = 'https://swapi-api.hbtn.io/api';

  $.get(`${API_URL}/films/?format=json`, (moviedata, status) => {
    moviedata.results.forEach(movie => {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    });
  });
});
