var password= document.querySelector(".password") 
var password_conf = document.querySelector(".passwordconf") 
var numtel = document.querySelector(".numtel")
var error_num = document.querySelector('.error-num')
var error_password = document.querySelector(".error-password")
function error_num_add(){
    var num = numtel.value
    if(num.length != 10 && num.length != 0){
        error_num.innerHTML="le numéro de téléphone doit contenir 10 chiffres"
    }
    else{
        error_num.innerHTML=""   
    }
}
function error_password_add(){
    if(password.value !==password_conf.value && password_conf.value != ""){
        error_password.innerHTML="les deux mot de passes sont différents"
    }
    else{
        error_password.innerHTML=""
    }
}
password_conf.addEventListener("keyup",()=>{
    setTimeout(error_password_add,500)
})
numtel.addEventListener('keyup',()=>{
    setTimeout(error_num_add,500)
})