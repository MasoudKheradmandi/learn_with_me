/*****************

custom.js
=============
Template Name: Tutspress - Multipurpose Education HTML Template
Template URI: http://me-design.ir
Author:  ME-Design
Version: 1.0.0

*******************/

$(document).ready(function(){

  //Responsive function
  function tutspress_responsive(tutspress_lg_screen_width) {
    if (tutspress_lg_screen_width.matches) {

      // add custom icon to submenu
      $('.tutspress-dropdown-toggle').append('<i class="far fa-plus-square tutspress-submenu-icon tutspress-text-color"></i>');

      //border of submenu
      $('.dropdown-menu.show').addClass("tutspress-border-color");

      //remove border-right from contact-box in footer
      $('.contatct-box > .col-lg-3').removeClass("right-widget-border").addClass("bottom-widget-border");
      $('.contatct-box > .col-12').removeClass("address-row").addClass("bottom-widget-border");

      //remove widgets border from footer
      $('.widget-box.middle-widget').addClass("middle-widget-2").removeClass("middle-widget");

    } else {

      // add default icon to submenu and remove our custom icon
      $('.nav-item.dropdown > .nav-link').addClass("dropdown-toggle");
      $('.nav-item.dropdown > .nav-link').removeClass("tutspress-dropdown-toggle");
    }
  }
  // If you want to set a new boundary to apply the changes:
  var tutspress_lg_screen_width = window.matchMedia("(max-width:992px)");
  tutspress_responsive(tutspress_lg_screen_width);
  tutspress_lg_screen_width.addListener(tutspress_responsive);



  //Course Categories sliding carousel - Owlcarousel
  $('.cat-box-section > .owl-carousel').owlCarousel({

    loop:true,//if you want loop
    center: true,//alignment center
    lazyLoad: true,//lazy load is enable
    autoplay:true,//autoplay is enable
    autoplayTimeout:3500,//set autoplay time
    autoplayHoverPause:true,//pause with mouse hever is enable
    margin:15,//margin of items
    dots:true,//dots controller is enable
    dotsEach:2,//each dot control how many items?
    nav:false,//navigator is disable
    responsive:{
        0:{
            items:2
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
  });



  //our partner sliding carousel - Owlcarousel
  $('#our-partner').owlCarousel({

    loop:true,//if you want loop
    center: true,//alignment center
    lazyLoad: true,//lazy load is enable
    autoplay:true,//autoplay is enable
    autoplayTimeout:3500,//set autoplay time
    autoplayHoverPause:true,//pause with mouse hever is enable
    margin:15,//margin of items
    nav:false,//navigator is disable
    dots:false,//dots controller is disable
    responsive:{
        0:{
            items:2
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
  });



  //simple counter
  $('.counter-item .counter-numb').each(function () {
    $(this).prop('Counter',0).animate({
        Counter: $(this).text()
    }, {
        duration: 4000,//set duration
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
  });



  // filter buttons of Courses
  $('#latest-course-section .filter-button').on('click',function() {

    // get ID of buttons
    var btn_filter_id = $(this).attr('id');
    // get data-filter of button
    var btn_filter_attr = $(this).attr('data-filter');

    // show all & filter
    if (btn_filter_attr == 'all') {
      $('#latest-course-section .filter').fadeIn('1000');
    } else {
      $("#latest-course-section .filter").not('.' + btn_filter_attr).fadeOut('1000');
      $('#latest-course-section .filter').filter('.' + btn_filter_attr).fadeIn('1000');
    }

    //active class for clicked button
    if ($("#"+btn_filter_id).hasClass("active") == false) {

      $('.filter-button').removeClass("active");
      $('#'+btn_filter_id).addClass("active");

    }
  });


  //Add categories widget icon
  if ($('.side-widget-box .cat-list-widget > .cat-item').length != 0) {
    $('.side-widget-box .cat-list-widget > .cat-item').prepend('<i class="far fa-bookmark tutspress-text mx-2"></i>');
  }



  //Add tags widget icon
  if ($('.side-widget-box .tag-list-widget > .tag-item').length != 0) {
    $('.side-widget-box .tag-list-widget > .tag-item').prepend('<i class="fas fa-hashtag tutspress-text mx-1"></i>');
  }



  //Add post-list widget icon
  if ($('.side-widget-box .post-list-widget > .post-item').length != 0) {
    $('.side-widget-box .post-list-widget > .post-item').prepend('<i class="fas fa-caret-right tutspress-text mx-2"></i>');
  }



  //Sticky course information sidebar
  if ($("#course-sidebar").length != 0) {


    $(window).scroll(function() {

      // get sidebar offset to top
      var sidebar_position = $("#course-sidebar").offset().top;
      //get footer offset to top
      var footer_position_top = $("footer").offset().top;



      if ($(document).scrollTop() > sidebar_position) {

        $("#course-sidebar > .side-widget-box").addClass("sticky-sidebar");


        if ($(document).scrollTop() > footer_position_top) {

          $("#course-sidebar > .side-widget-box").removeClass("sticky-sidebar");

        }


      }else {

        $("#course-sidebar > .side-widget-box").removeClass("sticky-sidebar");
      }
    });

  }



  //Animation for search-box
  if ($("#course-category").length != 0) {
    // get offset
    var search_box_position = $("#course-category").offset().top;

    $(window).scroll(function() {

      if ($(document).scrollTop() < search_box_position) {

        $('.search-row .main-title-search').addClass("animate__animated animate__fadeInLeft");
        $('.search-row .secondry-title-search').addClass("animate__animated animate__bounceInDown");

      } else {

        $('.search-row .main-title-search').removeClass("animate__animated animate__fadeInLeft");
        $('.search-row .secondry-title-search').removeClass("animate__animated animate__bounceInDown");
      }

    });

  }

});
