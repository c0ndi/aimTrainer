const formLogin = document.querySelector('.login');
const formPassword = document.querySelector('.password');
const formNick = document.querySelector('.nick');

const validateForm = (event) => {
    if (formLogin.value == '' || formPassword.value == '' || formNick.value == '') {
        
        event.preventDefault();
        if (formLogin.value == '')
            formLogin.classList.add('invalid-input')
        else
            formLogin.classList.remove('invalid-input')
        if (formPassword.value == '')
            formPassword.classList.add('invalid-input')
        else
            formPassword.classList.remove('invalid-input')
        if (formNick.value == '')
            formNick.classList.add('invalid-input')
        else
            formNick.classList.remove('invalid-input')
        return false;
    }
}

document.querySelector('form').addEventListener('submit', validateForm)