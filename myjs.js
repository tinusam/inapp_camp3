

// let mytext = "Hello and Welcome";
// //let parttext = mytext.slice(4,10);
// //let parttext = mytext.slice(-11,-4);
// //let parttext = mytext.slice(5);
// let parttext = mytext.substring(5);
// //alert(parttext);

// //string replacement with replace()
// mytext = "Hi There! How are you. ";
// let newtext = mytext.replace("How", "Who");
// //alert(newtext);

// //joining tw strings using javascript
// mytext2 = "Hope you are doing fine";
// let myjoinedtext = mytext.concat(mytext);
// //alert(myjoinedtext);

// //changing case
// //alert(mytext2.toUpperCase());
// //alert(mytext2.toLowerCase());

// //trim space
// //var mytext3 = "  hi   ";
// //alert(mytext3.trim());

// //select char/ascii from the string
// let text4 = "Hello World";
// //alert(text4.charAt(3));
// //alert(text4.charCodeAt(3));

// //basic arithymetic operations in js
// var a = 3, b = 2;
// var result = a + b;
// //alert(result);


// //evaluate math expresiion using js
// var result = eval("a*b+b+2+3");
// //alert(result);
// var result = a !==b;

// //comditional operators
// var a = 5 ;
// var b=10;
// if(a<b) {
//     //alert(a+'is greater than '+b);
// }else{
//     //alert(a+' is less or equal to '+b);
// }

// //switch case
// switch (new Date().getDay()){
//     case 1:
//         day ="Monday"
//         break;
//     case 2:
//         day ="Tuesday"
//         break;
//     case 3:
//         day ="wednesday"
//         break;
//     case 4:
//         day ="Thursday"
//         break;
                              
//    case 5:
//         day ="Friday"
//         break;
//     default:
//         day ="weekend";
        
                         
// }
// //alert(day);

// //loops in javascript
// //while loop
// var  a = 5;
// while (a<10){
//     //alert(a);
//     a= a+1;
// }
// //for loop
// for(var i =1; i<10; i++){
//     alert(i)
// }

// //simple function declaration in js

// function add(a,b){
//     return a+b;

// }
// add = function add(a,b){
//     return a+b;
// }
// var result=add(3,4);
//  //alert(result);

//  //arrow function declaration in javascript
//  var square = a =>{
//     console.log("The number is "+a);
//     return a*a;
//  };

//  var result = square(4);
//  console.log(result);

//  //a single line arrow function (if only one statement)
//  var square = a =>a*a;

//  var result = square(25);
//  console.log(result);

//  //mapping an array to an arrow function
//  var myarray = [2,4,6];
//  var square_array = myarray.map(a => a*a)
// //consolw.log(square_array);
// //arrays in javascript
// var myarray =['apple','orange','grapes'];
// alert(myarray);
// alert(myarray)


// console.log(myarray.length);
// myarray.push("strawberry");
// console.log(myarray);

// //for and foreach loop to traverse through the array
// for(var i=0; i<myarray.length; i++){
//     console.log(myarray[i]);

// }
// //myarray.forEach(i => {console.log(i)});

// //concat for immutable arrays
// var myarray = ['tinu','tintu','feby'];
// var myarray2 = myarray.concat('alby');
// //alert(myarray2);

// //destructing a js array
// //assigning each value of array to a variable
// t=[1,2,3,4,5,6,7,8];
// [first,second,third,...fourth]=t;
// console.log(first);
// console.log(second);
// console.log(third);
// console.log(fourth);

// //javascript object (collection of vars and functions)
// var student  = {
//     studname: 'tinu',
//     age :21,
//     talk:function(){
//         alert("Hello Tinu");
//     }
// }

// alert(student.studname);
// student.student = "Tintu";
// alert(student.studname);
// student.talk();
//  //include a nested object in an existing obj
//  student.address = {
//     door_no :10,
//     distrist : "Delhi"
//  }

// alert(student.address.door_no);

// //declaring an empty object
// var car ={};
// car.model = 'swift';
// car.stop = function(){
//     //alert(this.model+"car stopped");

// }
// //alert(car.model);
// car. stop();

// //creating object for the class to acces var and fns
// //var tom = new personalbar('tom, 30');
// //tom.greet();

//JSON object 
//Creating a JSON object using the stringify() method
// var jsonstring = JSON.stringify({
//     name:"Tinu",
//     age:21,
//     Address:{
//         district:"TVM",
//         location:"TechnoPark"
//     }
// });
// //console.log(jsonstring)

// //Parsing the JSON string
// var parsedjson = JSON.parse(jsonstring)
//alert(parsedjson.name)
//alert(parsedjson.age)
//alert(parsedjson.Address.district)

//select html element using javascript
var mypelements = document.getElementsByTagName('p');
var myh2withid = document.getElementById('myh2elemid');
var myh3withcls = document.getElementsByClassName('myh3')
//using css selectors
//selecting a single/first occurence 
var myheaderwithid = document.querySelector('#header');
var myallbtns = document.querySelectorAll('.btn');

//fetching values/data inside the html element after seleting it
//getting the text content inside an element
//alert(mypelements[0].textcontent)
//alert(mypelement[1].textcontent)
//get the valu from the html elements like in textbox


var mytxtname = document.getElementsByName("txtcustname");
//alert(mytxtname[0].value);
//getting the inner html content of an element
//alert(myheaderwithid.innerHTML)
var handleClick = function(event){
    alert(document.getElementById("mytxtbox").value);
    document.getElementById("mytxtbox").value =" The new value";

}
var mybtn = document.getElementById('btn1');
mybtn.addEventListener('click',handleclick);

