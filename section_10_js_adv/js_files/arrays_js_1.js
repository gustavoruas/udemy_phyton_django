
var var_array = [];

//alert("test file");


function fill_array(param) {
    var_array.push(param)
}

function remove_from_array(id){
    var_array.pop();

    //refreshes array
    print_array(id);
}


function get_field_text(id) {

    field_text = document.getElementById(id).value;
    fill_array(field_text);

    if (field_text !== "" || field_text !== null) {
        document.getElementById(id).value = "";
    }

}

function print_array(id) {

    var return_text = "Array Elements: ";

    //  multiple wasy to iterate JS 

      for (var_elem of var_array) {
        return_text = return_text + " [" + var_elem + "]";
      }

    // var_array.forEach(
    //     function(return_element) {
    //         return_text = return_text + " " + return_element;
    //     }
    // );
    
    // for(var i = 0; i < var_array.length; i++){
    //     console.log("display array element: " + var_array[i]);
    //     return_text = return_text + " [" + var_array[i] + "]"; 
    // }


    document.getElementById(id).innerHTML = return_text;
}

function clear_array(id){
    var_array = [];
    document.getElementById(id).innerHTML = "";
}

