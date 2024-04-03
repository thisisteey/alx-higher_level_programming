// Script that updates the text color of the header when user clicks on the tag
'use strict';
$(() => {
  $('DIV#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
