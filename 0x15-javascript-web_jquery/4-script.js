// Script that toggles the class of the header when the user clicks on the tag
'use strict';
$(() => {
  $('DIV#toggle_header').click(() => {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      if (!$('header').hasClass('green')) {
        $('header').addClass('green');
      }
    } else if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      if (!$('header').hasClass('red')) {
        $('header').addClass('red');
      }
    } else {
      $('header').addClass('red');
    }
  });
});
