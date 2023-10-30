// $(document).ready(function() waits for the whole HTML to render first
$(document).ready(function () {
  $("#clicable_header").click(function () {
    try {
      // console.log($(this));
      // console.log($(this).text());
      $(this).toggleClass("div_but_normal");
      var current_text = $(this).text();
      var clicked_text = "This element has been clicked";

      if ($(this).text() === clicked_text) {
        $(this).text("Clicable header information");
      } else {
        $(this).text(clicked_text);
      }
    } catch (error) {
      console.error(
        "  -* Error found: ",
        error.lineNumber + " : " + error.message
      );
    }
  });

  //adding events with the ON method
  $("#clicable_header").on("mouseenter", function () {
    try {
      $(this).addClass("div_but_cancel_over");
    } catch (error) {
      console.error(
        "  -* Error found: ",
        error.lineNumber + " : " + error.message
      );
    }
  });

  $("#clicable_header").on("mouseleave", function () {
    try {
      $(this).removeClass("div_but_cancel_over");

      //Retrieves an attribute value of specific element selected
      console.log($(this).attr("class"));
    } catch (error) {
      console.error(
        "  -* Error found: ",
        error.lineNumber + " : " + error.message
      );
    }
  });
});
