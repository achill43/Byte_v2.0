const hamburger_menu = document.querySelector(".hamburger-menu");
const content = document.querySelector(".content");

// Event for menu
hamburger_menu.addEventListener("click", function () {
  content.classList.toggle("active");
  hamburger_menu.classList.toggle("active");
  var logo = document.querySelectorAll(".logo");
  logo.forEach(function (item) {
    item.classList.toggle("active");
  })
});





// Logic for tabs
// const tabs_btn = document.querySelectorAll(".js-tabs-btn");
// const tabs_item = document.querySelectorAll(".js-tabs-item");
// if (tabs_btn) {
//   tabs_btn.forEach(function (item) {
//     item.addEventListener("click", function () {
//       let current_btn = item;
//       let tab_id = "#" + current_btn.getAttribute("data-tab");
//       let current_tab = document.querySelector(tab_id);

//       tabs_btn.forEach(function (btn) {
//         btn.classList.remove("active");
//       });

//       tabs_item.forEach(function (item) {
//         item.classList.remove("active");  
//       });

//       current_tab.classList.add("active");

//       current_btn.classList.add("active");
//     });
//   });
// }

// Logic for acordion
const accordin_items = document.querySelectorAll(".js-acordion-item");
if (accordin_items) {
  accordin_items.forEach(function (item) {
    item.addEventListener("click", function () {
      var cur_item = item;
      accordin_items.forEach(function (acc_i) {
        acc_i.classList.remove("active");
      });
      cur_item.classList.add("active");
    });
  });
}

// Logic for search
var search_btn = document.querySelector(".js-search-btn");
var search_cancel = document.querySelector(".js-search-cancel");
var search_form = document.querySelector(".js-search-form");
search_btn.onclick = () => {
  if(search_form.classList.contains('active')) {
    search_form.submit();
  }
  search_form.classList.add("active");
}
search_cancel.onclick = () => {
  search_form.classList.remove("active");
  document.querySelector(".js-search-result").classList.remove("show");
}

jQuery(document).ready(function () {
  jQuery('body').on('click', '.js-autocomplite-item', function () {
    jQuery(this).parent(".js-search-result").siblings("input").val(
      jQuery(this).text());
    jQuery(".js-search-result").removeClass("show");
    jQuery(".js-search-form").submit();
  });

  jQuery(".js-search-form").hover(function () {}, function () {
    console.log("Unhover")
    jQuery(".js-search-result").removeClass("show");
  })

  jQuery('body').on("keyup", ".js-search-input", function () {
    var search_str = jQuery(this).val();
    var result_block = jQuery(this).siblings('.js-search-result');
    jQuery.ajax({
      url: jQuery('.js-search-ajax-url').attr('data-url'),
      type: 'get',
      data: {
        "search_str": search_str
      },
      success: function (data) {
        result_block.addClass("show");
        result_block.html(data.html);
      },
      error: function () {
        console.log("Missing some error look Network");
      }
    });
  });
});

const select_lang = document.querySelector(".js-select-lang");
select_lang.addEventListener("change", function () {
  const lang_form = document.querySelector(".js-lang-form");
  lang_form.submit();
});
