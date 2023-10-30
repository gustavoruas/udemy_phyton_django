function get_random_color(){
    var letters = "0123456789ABCDEF";
    var color = "#"

    for(var i = 0; i < 6 ; i++){
        color += letters[Math.floor(Math.random()*16)]
    }

    return color;
}

function set_element_color_by_id(id){
    //Same as getElembyID, but need to refence # as CSS id identification
    var element_id = "#"+id;
    
    var element = document.querySelector(element_id);

    element.style.color = get_random_color();

}

function element_color_changer(id){
    setInterval(set_element_color_by_id(id), 500);
}



