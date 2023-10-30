

function toggle_div_class(id, on_off) {
    var div_state = document.getElementById(id).getAttribute("class");

    if (div_state.search(/invisible/i) > -1) {

        if (on_off == "on") {
            div_state = div_state.replace(/invisible/i, "");
            document.getElementById(id).setAttribute("class", div_state);
        }

        //no inv tag found
    } else {
        if (on_off == "off") {
            div_state = div_state + " invisible";
            document.getElementById(id).setAttribute("class", div_state);
        }
    }

    // console.log("class tag:" + div_state.search(/invisible/i));
}

function write_html(id, text) {
    document.getElementById(id).innerHTML = text;
}


function check_form(id) {
    
    var return_text = "";
    var empty_field = false;
    var form = document.getElementById(id);

    var spy_condition = 0;

    var formData = new FormData(form);

    //Validate if all fields have been populated
    for (var [key, value] of formData.entries()) {
        if (value == "" || value.length == 0) {
            return_text = return_text + "Field " + key + " Must be populated. <br>";
            
            console.log("IF empty_field:" + empty_field);
            
            empty_field = true;
        }
    }
    

    if (empty_field == true) {
        write_html("return_text_div", return_text);

        toggle_div_class("return_text_div", "on");

        //halts the script as well
        throw new Error("Empty fields present");
    }

    //validation
    for (var [key, value] of formData.entries()) {        

        //  console.log("forloop key:" + key.toLowerCase());

        //the spy message
        if ( key.toLowerCase() == "first_name" && value.toLowerCase() == "jose") {            
            spy_condition = spy_condition + 1;            
        }else if( key.toLowerCase() == "first_name"){
            console.log("first_name non spy:" + value);
            return_text = value;
        }

        if ( key.toLowerCase() == "last_name" && value.toLowerCase() == "johnson" ) {
            
            spy_condition = spy_condition + 1;
        }else if(key.toLowerCase() == "last_name"){
            return_text = return_text + " " + value;
        }

        if (key.toLowerCase() == "age" && value.toLowerCase() == 26) {
            spy_condition = spy_condition + 1;            
        }

        if (key.toLowerCase() == "height" && value.toLowerCase() == 175 ) {
            spy_condition = spy_condition + 1; 
        }

        if (key.toLowerCase() == "pet_name" && value.toLowerCase() == "sammy") {
            spy_condition = spy_condition + 1;            
        }

    }

    // console.log("spy_condition:" + spy_condition);

    if (spy_condition == 5) {
        return_text = "Welcome JAMENSON BONDIS, your AK47 is ready!"        
    }else{
        return_text = "Hello " + return_text;
    }

    //print welcome message
    write_html("return_text_div", return_text);

    toggle_div_class("return_text_div", "on");
}

