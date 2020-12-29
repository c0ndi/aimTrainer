const formLogin = document.querySelector('.login');
const formPassword = document.querySelector('.password');
const validateForm = (event) => {

    if (formLogin.value == '' || formPassword.value == '') {
        event.preventDefault();

        if (formLogin.value == '')
            formLogin.classList.add('invalid-input-login')
        else
            formLogin.classList.remove('invalid-input-login')

        if (formPassword.value == '')
            formPassword.classList.add('invalid-input-login')
        else
            formPassword.classList.remove('invalid-input-login')

        return false;
    }
}

document.querySelector('form').addEventListener('submit', validateForm)