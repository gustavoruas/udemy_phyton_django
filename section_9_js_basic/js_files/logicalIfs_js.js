
console.log("is 2 < 3 ?")
if(2<3){
  console.log(true);
};

console.log("type validation: is text_type variable the same type as a number? '10' === 10")
if("text"===10){
  console.log(true);
}else{
  console.log(false);
}

console.log("Value validation: is 22 equals to '22' ?")
if(22 == "22"){
  console.log(true);
}else {
  console.log(false);
}

console.log("Value validation and Type: 22 == '22' && 22==='22' ?")
if(22 == "22" && 22==="22"){
  console.log(true);
}else {
  console.log(false);
}


function return_promt_html(paramId){
  var getprompt = prompt("Write a value");

  // changes the inner code of an ID fro mHTML page
  document.getElementById(paramId).innerHTML = getprompt;
}
