
$(document).ready(function() {
  $("#divID").html("Hello World!");
});

// $(document).ready(function() {
//   alert("Test jQuery path");
// });

  //This will display 'Hello World!' only, overwriting the rest of the divs'
// $(document).ready(function() {
//   $("div").html("<h1> Hello World! </h1>");
// });
  // If the .html is changed to .text then the the html tags are also included.

// css
function changeColor() {
  $("#divTest").css("background-color", "red");
}

function setCSS() {
  $('p:nth-child(1)').css("font-style", "italic")
  $('p:nth-child(3)').css("font-style", "italic")
}
