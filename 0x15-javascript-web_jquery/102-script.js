// Script that fetches and prints how to say “Hello” depending on the language
'use strict';
$(() => {
  $('INPUT#btn_translate').click(() => {
    const API_URL = 'https://fourtonfish.com';
    const languageCode = $('INPUT#language_code').val();
    $.get(`${API_URL}/hellosalut/?lang=${languageCode}`, (langdata, status) => {
      $('DIV#hello').html(langdata.hello);
    });
  });
});
