
//Scann all cells of the table
tictac_table = document.querySelectorAll("div[id='tictac_cell']");


//iterate per each cell and attribute behaviour
for(var i=0; i < tictac_table.length; i++ ){

    //set behaviour for when single click, set circle
    tictac_table[i].addEventListener("click",function(){
        // this.className = "text_for_o";
        // this.innerHTML="O";

        if(this.innerHTML === ""){
            this.className = "text_for_x";
            this.innerHTML="X";

        }else if(this.innerHTML ==="X"){
            this.className = "text_for_o";
            this.innerHTML= "O";
        }else{
            this.className = "text_initial";
            this.innerHTML= "";
        }



    });

    //sent behaviour for when double click, set X
    // tictac_table[i].addEventListener("dblclick",function(){
    //     this.className = "text_for_x";
    //     this.innerHTML = "X";
    // });    

}

function reset_all_cells(){
    for(var i = 0; i < tictac_table.length ; i++){
        tictac_table[i].innerHTML = " ";
    }
}


