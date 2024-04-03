// Script that fetches the character name from an API url
'use strict';
$(() => {
  const API_URL = 'https://swapi-api.hbtn.io/api';

  $.get(`${API_URL}/people/5/?format=json`, (charName, status) => {
    $('DIV#character').html(charName.name);
  });
});
