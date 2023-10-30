var i = 0;
var return_html;

function write_html(id, html_text) {
    document.getElementById(id).innerHTML = html_text;
}

function forloop_1(tag_id) {
    
    if(return_html==undefined || return_html.length != 0){
        return_html = "";
    }

    for (var i = 1; i <= 5; i++) {
        return_html = return_html + "<li class='list-group-item'>Value: " + i + "</li><br> ";
    }

    write_html(tag_id, return_html);
}

function stringloop(id, param_string){
    var return_text="";

    for(var i = 0; i < param_string.length; i++){
        return_text = return_text + "<li class='list-group-item'>Value: "+ param_string[i]  + "</li><br> ";
    }
    
    write_html(id, return_text);
}










