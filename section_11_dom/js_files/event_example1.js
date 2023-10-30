//need to define which attribute to fetch naming from
//# is id, . is for class, h1 is for tag H1 

//fetches only the first button tags
//var button1 = document.querySelector("button");

//fetches all the first button tags, returns into an array
//var buttonsAll = document.querySelectorAll("button");

//Fetchesl all buttons which id="regular_button"
var buttonsAll = document.querySelectorAll("button[id='regular_button']");

var buttonsAllCancel = document.querySelectorAll("button[id='cancel_button']");

//Iterates per all elements, and per each element, it defines an EVENT.
for(var i = 0; i < buttonsAll.length; i++){
    buttonsAll[i].addEventListener("mouseover", function(){
        this.className = "div_but_over";
    })

    buttonsAll[i].addEventListener("mouseout", function(){
        this.className = "div_but_normal";
    })

}

for(var i = 0; i < buttonsAllCancel.length; i++){
    buttonsAllCancel[i].addEventListener("mouseover", function(){
        this.className = "div_but_cancel_over";
    })

    buttonsAllCancel[i].addEventListener("mouseout", function(){
        this.className = "div_but_cancel_normal";
    })

}

