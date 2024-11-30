
function hide_element_by_id(id){
    
    $(`#${id}`).hide();
    //alert(id);
}


function check_close_window(){
    text="Are you sure you want to close the assessment? All questions will be lost and not submitted!";

    if(confirm(text) == true){
        window.close();

    }else{
        null;
    };
    
}


function open_custom_popup_window(url, width, height){
    console.log(`open_custom_popup_window:width=${width},height=${height}`);

    const windows_features = `width=${width},height=${height},menubar=no,toolbar=no,location=no,status=no,scrollbars=yes`;    window.open(url,"_blank", windows_features);
    window.open(url, "_blank", windows_features);
}


//changes the colour of question header class
function update_header_answer_color(element_id,group_set, class_name){
    const radio_buttons = document.querySelectorAll(`input[type="radio"][name="${group_set}"]`);

    radio_buttons.forEach(radio => {
        
        //on INIT of page, if reloaded apply same class change
        if(radio.checked){
            const target_element = document.getElementById(element_id);

            if (target_element){
                target_element.className = class_name;
            }else{
                console.error(`Element with id "${element_id}" not found.`)
            }
        }

        //addEventListener validates functionality on radio change.
        radio.addEventListener('change', function(){
            if(radio.checked){
                const target_element = document.getElementById(element_id);

                if (target_element){
                    target_element.className = class_name;
                }else{
                    console.error(`Element with id "${element_id}" not found.`)
                }
            }
        });
    });

}

