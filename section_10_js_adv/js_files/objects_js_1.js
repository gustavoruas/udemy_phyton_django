

var var_object = [];
var user = {};

function fill_object_list(keyparam, value) {
    
    //to define an object, best approach is to create an empty obj with {}
    var new_object = {};
    //then define its index and value
    new_object[keyparam] = value;

    var_object.push(new_object);
}

function remove_from_object(id){
    var_object.pop();

    //refreshes array
    print_object_array(id);
}


function add_js_object(key_id, value_id) {

    var field_key   = document.getElementById(key_id).value;
    var field_value = document.getElementById(value_id).value;


    fill_object_list(field_key, field_value);

    //empties fields for next value
    if (field_value !== "" || field_value !== null) {
        document.getElementById(key_id).value = "";
        document.getElementById(value_id).value = "";
    }

}


function print_object_array(id) {

    var return_text = "Array Elements: ";

    // First iterate within keys to fetch their index    
    for(var i = 0; i < var_object.length; i++){

        var keys = Object.keys(var_object[i]);

        console.log("keys: " + keys);
        
        //for every index, we fetch its value
        for(var j =0 ; j < keys.length; j++ ){
            var current_key = keys[j];
            console.log(current_key );
            console.log(var_object[i][keys[j]]);
            return_text = return_text + "[" + keys[j] + ":" + var_object[i][keys[j]] + "]";

        }      
    
    }

    document.getElementById(id).innerHTML = return_text;
}

function clear_object_list(id){
    var_object = [];
    document.getElementById(id).innerHTML = "";
}

function create_user_obj(name_id, surname_id){

    var_object = [];
    var name_in = document.getElementById(name_id).value;
    var surname_in = document.getElementById(surname_id).value;


    user = {
        name : name_in,
        surname : surname_in,
        firstname_lenght : function(){ return "First name leght :" + this.name.length}
    }
}

function print_user_obj(id){
    //Parses JSON object structure into string
    document.getElementById(id).innerHTML = JSON.stringify(user);   

}

