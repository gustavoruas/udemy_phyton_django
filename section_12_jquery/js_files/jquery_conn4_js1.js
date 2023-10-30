$(document).ready(function () {
  var current_player = "red";
  var all_columns = $('div[id^="row"]');

  all_columns.click(function () {
    //array to hold all cells from col selected
    var all_cells_per_col = [];

    //iterates at each cell of the column, adding them to an array to manipulate
    $(this)
      .find('div[id^="cel"]')
      .each(function () {
        all_cells_per_col.push(this);
      });

    //Reverses the order from last to first
    all_cells_per_col = $(all_cells_per_col).get().reverse();

    //Iterates at the list of cells
    //if blue player is current, mark the last to first cell
    $(all_cells_per_col).each(function () {
      if (current_player === "blue") {
        //$(this).attr("class","cell_blue");

        if ($(this).hasClass("cell_blank")) {
          $(this).removeClass("cell_blank").addClass("cell_blue");

          //this exits LOOP iteration , so a single circle is coloroued
          return false;
        }
      } else {
        //$(this).attr("class","cell_red");

        if ($(this).hasClass("cell_blank")) {
          $(this).removeClass("cell_blank").addClass("cell_red");

          //this exits LOOP iteration , so a single circle is coloroued
          return false;
        }
      }
    });

    if (checkWinningCondition(all_columns)) {
      $(this).set_victorious_player(current_player);

      //removes click function from matrix
      all_columns.off("click");
    }

    current_player = $(this).change_player(current_player);
    $(this).get_player();

    // console.log($(this).attr("id") + " " + all_columns);
    // console.dir(all_cells_per_col);
  });

  function checkWinningCondition(all_columns) {
    //fucking AI generated, had to fix 1 or 2 things, but DAMN!
    // Define the winning patterns
    var winningPatterns = [
      // Horizontal connections
      [0, 1, 2, 3],
      [1, 2, 3, 4],
      [2, 3, 4, 5],
      [3, 4, 5, 6],
      [7, 8, 9, 10],
      [8, 9, 10, 11],
      [9, 10, 11, 12],
      [10, 11, 12, 13],
      [14, 15, 16, 17],
      [15, 16, 17, 18],
      [16, 17, 18, 19],
      [17, 18, 19, 20],
      [21, 22, 23, 24],
      [22, 23, 24, 25],
      [23, 24, 25, 26],
      [24, 25, 26, 27],
      [28, 29, 30, 31],
      [29, 30, 31, 32],
      [30, 31, 32, 33],
      [31, 32, 33, 34],
      [35, 36, 37, 38],
      [36, 37, 38, 39],
      [37, 38, 39, 40],
      [38, 39, 40, 41],

      // Vertical connections
      [0, 7, 14, 21],
      [7, 14, 21, 28],
      [14, 21, 28, 35],
      [1, 8, 15, 22],
      [8, 15, 22, 29],
      [15, 22, 29, 36],
      [2, 9, 16, 23],
      [9, 16, 23, 30],
      [16, 23, 30, 37],
      [3, 10, 17, 24],
      [10, 17, 24, 31],
      [17, 24, 31, 38],
      [4, 11, 18, 25],
      [11, 18, 25, 32],
      [18, 25, 32, 39],
      [5, 12, 19, 26],
      [12, 19, 26, 33],
      [19, 26, 33, 40],
      [6, 13, 20, 27],
      [13, 20, 27, 34],
      [20, 27, 34, 41],
    ];

    // Check all winning patterns for each player
    for (var i = 0; i < winningPatterns.length; i++) {
      var cells = [];
      for (var j = 0; j < winningPatterns[i].length; j++) {
        var cellIndex = winningPatterns[i][j];
        cells.push($(all_columns).find('div[id^="cel"]').eq(cellIndex));
      }

      //console.log("Current pattern" +  winningPatterns[i]);
      //console.dir(cells);

      // Check if all cells in the pattern have the same color
      var firstCellColor = cells[0].attr("class");
      if (firstCellColor != "cell_blank") {
        var hasWon = true;
        for (var j = 1; j < cells.length; j++) {
          var cellColor = cells[j].attr("class");
          console.log(" *2: " + cells[j].attr("class").split(" ")[1]);
          if (cellColor != firstCellColor) {
            hasWon = false;
            break;
          }
        }

        if (hasWon) {
          if (firstCellColor === "cell_red") {
            console.log("Red wins!");
          } else if (firstCellColor === "cell_blue") {
            console.log("Blue wins!");
          }
          return true;
        }
      }
    }

    return false;
  }

  $.fn.change_player = function (p_current_player) {
    var local_return;

    if (
      $.trim(p_current_player) === "" ||
      $.trim(p_current_player).length === 0
    ) {
      local_return = "blue";
    } else if (p_current_player === "blue") {
      local_return = "red";
    } else {
      local_return = "blue";
    }

    return local_return;
  };

  $.fn.get_player = function () {
    //console.log("current_player: " + current_player);

    if (current_player === "blue") {
      $("#player_turn_b").text(current_player);
      $("#player_turn_b").css("color", "rgb(16, 62, 148)");
    } else {
      $("#player_turn_b").text(current_player);
      $("#player_turn_b").css("color", "rgb(172, 11, 11)");
    }
  };

  $("div").get_player();

  $.fn.set_victorious_player = function (p_player) {
    $("#text_div_1").html(
      "Player <b>" +
        p_player +
        "</b> has won the match. <br>" +
        '<a id="redo_link" href="#">Redo Match</a>'
    );

    if (current_player === "blue") {
      $("#player_turn_b").text(current_player);
      $("#player_turn_b").css("color", "rgb(16, 62, 148)");
    } else {
      $("#player_turn_b").text(current_player);
      $("#player_turn_b").css("color", "rgb(172, 11, 11)");
    }

    //defines functionality to redo link
    $('a[id="redo_link"]').click(function () {
      location.reload();
    });
  };
});
