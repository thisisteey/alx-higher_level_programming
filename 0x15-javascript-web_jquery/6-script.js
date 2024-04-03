// Script that updates the text of the header to New Header when the user clicks on the tag
'use strict';
$(() => {
  $('DIV#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});
