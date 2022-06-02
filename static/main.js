let menu = document.querySelector(#mobile-nav-toggle);
let header = document.querySelector(#header);

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    header.classList.toggle('active');
}
  $document.getElementById("toggleVisibilityButton").addEventListener("click", function(button) {
   if (document.getElementById("displaytable").style.display == "block")
    document.getElementById("displaytable").style.display = "none";
   else document.getElementById("displaytable").style.display = "none";
});
$(document).ready(function () {
    $('#mobile-nav-toggle').on('click', function () {
        $(this).toggleClass('fa-times');
        $('header').toggleClass('toggle');
    });
});

$(".progress-bar").css("width", "0px")
$(function() {
    $(".progress-bar").each(function() {
        var finalWidth = parseInt($(this).attr("aria-valuenow"));
        $(this).css("width", "0px").animate({width: finalWidth+"%"}, 1000);
    });
});