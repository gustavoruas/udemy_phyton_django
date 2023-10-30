$(document).ready(function () {
  
    //attach an event to see any link call with ID
    $('a[id^="delete_link"]').click(function(){

        var confirmation = confirm("Are you sure you want to delete this?");

        if(confirmation=== true){
            return true;
        }else{
            return false;
        }

    });
});