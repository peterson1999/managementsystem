$(function () {
  $(document).scroll(function () {
    var $nav = $(".navContainer");
    var $navlogo = $(".navLogo");
    var $navlogoalt = $(".navLogoAlt");
    var $navlink = $(".nav-link");
    var $navbtn = $(".custom-toggler");
    $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
    if ($(this).scrollTop() > $nav.height()) {
      $navlogoalt.css("display", "none");
      $navlogo.css("display", "block");
    } else {
      $navlogoalt.css("display", "block");
      $navlogo.css("display", "none");
    }
    $navlogo.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
    $navlink.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
    $navbtn.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
  });
});
