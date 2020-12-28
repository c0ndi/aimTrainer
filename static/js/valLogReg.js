const formLogin = document.querySelector('.login');
const formPassword = document.querySelector('.password');
const inputs = [formLogin, formPassword]
const validateForm = (event) => { 
    
    if(formLogin.value == '' || formPassword.value == '')
    {
        event.preventDefault();
        if(formLogin.value == '')
        {
            formLogin.style.border = "2px solid #ff405c";
            formLogin.style.borderRadius = "25px";
        }
        if(formPassword.value == '')
        {
            formPassword.style.border = "2px solid #ff405c";
            formPassword.style.borderRadius = "10px";
        }
        return false;
    }
}

document.querySelector('form').addEventListener('submit', validateForm)
