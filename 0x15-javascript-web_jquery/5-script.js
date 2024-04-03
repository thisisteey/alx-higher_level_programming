// Script that adds a <li> element to a list when the user clicks on the tag
'use strict';
$(() => {
  $('DIV#add_item').click(() => {
    const newItem = document.createElement('li');

    newItem.textContent = 'Item';
    $('UL.my_list').append(newItem);
  });
});
