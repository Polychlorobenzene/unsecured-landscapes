$(document).ready(function() {
  $('#fullpage1').fullpage({
    sectionsColor: ['#ffffff', '#F3F3F3', '#ffffff', '#F3F3F3', '#ffffff'],
  });

  document.querySelector('.about-btn').addEventListener('click', function () {
    if (this.classList.contains('show')) {
     this.classList.remove('show');
     document.getElementById("about").classList.add("hidden");
     document.querySelector('.about-btn').innerHTML = "ABOUT";
     document.querySelector('.about-btn').style.color = "white";

     document.getElementById("title-right").style.color = "white";


    } else {
      // The user obviously can't follow instructions so let's alert them of what is supposed to happen next
      this.classList.add('show');
      document.getElementById("about").classList.remove("hidden");
      document.getElementById("title-right-bottom").style.color = "#212121"
      document.getElementById("title-right").style.color = "#212121"
      document.querySelector('.about-btn').innerHTML = "CLOSE"



    }
  });
});
