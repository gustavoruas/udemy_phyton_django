var x = 0;

console.log("12/2=" + 12/2);
console.log("12%5=" + 12%5);

console.log("While loop up until 5");
while (x < 5) {
    console.log("Current value: " + x);   
    x = x+1; 
}


x=0;
console.log("While loop break at 7, value 10");
while (x < 10) {

  console.log("Current value2:" + x);

  if (x = 7) {
    console.log("Current value2:" + x + " stop!");
    break;
  }  
  x=x+1;
}

x=0;
console.log("Even numbers from 1 to 20");
while (x<= 20) {
    
    if(x%2 == 0 ){
        console.log("Even number=" + x);
    }else{
        console.log("Odd number=" + x);
    }

    x = x +1;    
}

