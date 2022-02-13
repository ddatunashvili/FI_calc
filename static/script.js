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
var mockup = document.querySelector('.muck-up')
var content = document.querySelector('.content')

function move(){
  if ("muck-up" == mockup.getAttribute("class")){
    mockup.classList.add("main")
    content.classList.add("active")
    content.classList.add('muck-up')
  }else{
    mockup.classList.remove("main")
    content.classList.remove("active")
    content.classList.remove('muck-up')
  }
}



// add debit
var change = document.querySelector(".change")
var changedb = document.querySelector(".change .db ")
var changecr = document.querySelector(".change .cr ")
var content = document.querySelector(".content")

function addD(){
  mockup.classList.add("main")
  changecr.classList.add("main")
  content.classList.remove("active")
  change.classList.add("active")
}
function addC(){
  mockup.classList.add("main")
  changedb.classList.add("main")
  content.classList.remove("active")
  change.classList.add("active")
}



// edit
function Cname(){

var edit = document.querySelector(".edit")
var accName = document.querySelector(".account-name")
var user= document.querySelector(".user-details")

  uname = accName.innerHTML
  edit.classList.remove("fa-pen-to-square") 
  edit.classList.remove("edit")
  document.querySelector(".user-details i ").removeAttribute("onclick")
  user.innerHTML += `<form action='#' method='post'> <input type='text' value='${uname}'name='totalb'></form>`
}


