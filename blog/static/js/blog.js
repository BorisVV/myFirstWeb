
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
  $('#pTags:nth-child(1)').css("font-style", "italic")
  $('#pTags:nth-child(3)').css("font-style", "italic")
}

// redClass in the blog.css file
function myFunction() {
  $('#addClasses').addClass("redClass");
}

function showText() {
  $(".divMsgShow").show();
}
function hideText() {
  $(".divMsgHide").hide();
}
//hide/show
function toggleEffect() {
  $(".divMsgToggle").toggle();
}
function toggleEffectFunction(){
  $("#hideShowContent").toggle(function(){});
};

function slideUp() {
  $(".divMsgSlideUp").slideUp();
}
function slideDown() {
  $(".divMsgSlideDown").slideDown();
}

function insertBeforeHtml() {
  $("<div style='color:green;'>This text is inserted by insertBefore() method.</div>").insertBefore($("#divinsertBefore"));
}

function checkGenger() {
  if($("#inputChkMale").is(":checked")) {
    alert("Male is selected");
  }
  else if ($("#inputChkFemale").is(":checked")) {
    alert("Female is selected");
  }
}

  // .replaceWith()
function replaceWith() {
  $('#replaceWith').replaceWith("<p style='color:green;'>Hello, this is a new text!</p>")
}

  // number of boxes checked.
function getChkdCount() {
  alert($("input:checked").length);
}

  // get the selected value.
function getSelectedValue(){
  alert($("select option:selected").text());
}

  // event(function(){})
$(document).ready(function(){
  $("#btnClick").click(function(){
    alert("I am a click event");
  });
  // $("#btnMouseOver").mouseover(function(){
  //   alert("I am a mouse over event");
  // });
  // $("#btnMouseLeave").mouseleave(function(){
  //   alert("I am a mouse leave event");
  // });
});

  // event.keyCode (get the key of a char)
// function getChar(event) {
//   alert("key code is :" + event.keyCode);
// }

 //mouseout
$(function(){
  $("#mouseOutText").mouseout(function(){
    $("#mouseOutText").css("color","orange");
  });
});
