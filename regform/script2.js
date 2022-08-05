const form = document.getElementById('form');
const fullname = document.getElementById('username');
const email = document.getElementById('email');
const phone = document.getElementById('phone');
const password = document.getElementById('password');
const password1 = document.getElementById('password1');

function showError(input,message){
    const formControl = input.parentElement;
    formControl.className = 'form-control error';
    const small = formControl.querySelector('small');
    small.innerText = message;
}

function showSuccess(input){
    const formControl = input.parentElement;
    formControl.className = 'form-control success';
    
}


function checkPasswordMatch(input1, input2){
    if(input1.value !== input2.value){
        showError(input2,'Password doesn\'t Matched ')
    }
}

function isValidEmail(email){
   if(re.test(String(email.value).toLowerCase())){
       showSuccess(email);
    }else{
        showError(email,'Email is not valid');
    }
    
}


function checkRequired(inputArr){
  inputArr.forEach(input => {
       if(input.value.trim() === ''){
           showError(input,`${getFieldName(input)} is required`)
       }else{
           showSuccess(input);
       }
  });
}


 function getFieldName(input){
  return input.id
 }


 function checkLength(input,min,max){
     if(input.value.length<min){
         showError(input,`${getFieldName(input)} must be atleast ${min} characters`)
     }else if(input.value.length>max){
        showError(input,`${getFieldName(input)} must not exceed ${max} characters`)
     }else{
         showSuccess(input);
     }
 }


form.addEventListener('submit',(e)=>{
    e.preventDefault();
   
    
    checkLength(phone,10,12);
     checkLength(username,3, 50);
     checkLength(password,6, 15);
     checkRequired([username,email,password,password1]);
     isValidEmail(email);
     checkPasswordMatch(password,password1);
});
