function alert_hello(text){
    alert(text);
    console.log(text);
}

function write_char_loop(char,id, amount){

    var car_printout = char;   

    for (var i = 0; i < amount; i++) {
        car_printout = (car_printout * i) + "<br>";
            
    }

    document.getElementById(id).innerHTML = car_printout;

}
