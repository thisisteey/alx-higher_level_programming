// Script that fetches from an API url and displays the value of hello from that fetch in the HTML tag
'use strict';
$(() => {
  const API_URL = 'https://fourtonfish.com';

  $.get(`${API_URL}/hellosalut/?lang=fr`, (hellodata, status) => {
    $('DIV#hello').html(hellodata.hello);
  });
});
