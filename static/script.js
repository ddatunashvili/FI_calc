$(function () {
  $(".toggle-btn").click(function () {
    $(".filter-btn").toggleClass("open");
  });

  $(".filter-btn a").click(function () {
    $(".filter-btn").removeClass("open");
  });
});

$("#all").click(function () {
  $("ul.tasks li").slideDown(300);
});

$("#one").click(function () {
  $(".tasks li:not(.one)").slideUp(300, function () {
    $(".one").slideDown(300);
  });
});

$("#two").click(function () {
  $(".tasks li:not(.two)").slideUp(300, function () {
    $(".two").slideDown(300);
  });
});
$("#three").click(function () {
  $(".tasks li:not(.three)").slideUp(300, function () {
    $(".three").slideDown(300);
  });
});
$("#four").click(function () {
  $(".tasks li:not(.four)").slideUp(300, function () {
    $(".four").slideDown(300);
  });
});


// events

var plus = document.querySelector(".plus")
var minus = document.querySelector(".minus")

function move(){
  document.querySelector('.muck-up').classList.add("main")
  document.querySelector('.content').classList.add("active")
  document.querySelector('.content').classList.add("muck-up")

}
