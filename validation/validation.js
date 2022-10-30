let elInputUsername = document.querySelector('#username')
let elInputBirthday = document.querySelector('#birthday')
let elInputPassword = document.querySelector('#password')
let elInputPasswordretype = document.querySelector('#password-retype')
let elNumbertype = document.querySelector('#phonenumber')
let elJoinbutton = document.querySelector('#joinbutton')

let elFailmessage = document.querySelector('.fail-message')
let elFailuremessage = document.querySelector('.failure-message')
let elSuccessmessage = document.querySelector('.success-message')
let elMismatchmessage = document.querySelector('.mismatch-message')
let elMatchmessage = document.querySelector('.match-message')
let elMisnumbermessage = document.querySelector('.misnumber-message')
let elOvernumbermessage = document.querySelector('.overnumber-message')

elJoinbutton.disabled = true;

elInputUsername.onkeyup = function () {
    if (isMoreThan4Length(elInputUsername.value)) {
        elSuccessmessage.classList.remove('hide')
        elFailuremessage.classList.add('hide')
    }
    else {
        elSuccessmessage.classList.add('hide')
        elFailuremessage.classList.remove('hide')
    }
}

function isMoreThan4Length(value) {
    return value.length >= 4
}

elInputBirthday.onkeyup = function () {
    if (isMoreThan8Length(elInputBirthday.value)) {
        elFailmessage.classList.add('hide')
    }
    else {
        elFailmessage.classList.remove('hide')
    }
}

function isMoreThan8Length(value) {
    return value.length >= 8
}


elInputPasswordretype.onkeyup = function () {
    if ( isMatch(elInputPassword.value, elInputPasswordretype.value)) {
        elMismatchmessage.classList.add('hide')
        elMatchmessage.classList.remove('hide')
    }
    else {
        elMismatchmessage.classList.remove('hide')
        elMatchmessage.classList.add('hide')
    }
}

function isMatch (password1, password2) {
    if (password1 === password2) {
        return true;
    }
    else {
        return false;
    }
}

elNumbertype.onkeyup = function () {
    if (isNumbermatch(elNumbertype.value)) {
        elMisnumbermessage.classList.add('hide')
    }
    else {
        elMisnumbermessage.classList.remove('hide')
    }
}

function isNumbermatch(value) {
    let phonenumber = /^[0-9]*$/
    if(phonenumber.test(value) === true) {
        return true;
    }
    else {
        return false;
    }
}

elNumbertype.onkeyup = function () {
    if (isMoreThan11Length(elNumbertype.value)) {
        elOvernumbermessage.classList.add('hide')
    }
    else {
        elOvernumbermessage.classList.remove('hide')
    }
}

function isMoreThan11Length(value) {
    return value.length >= 11
}

elInputUsername.addEventListener('keyup', button)
elInputPassword.addEventListener('keyup', button)
elInputPasswordretype.addEventListener('keyup', button)
elNumbertype.addEventListener('keyup', button)

function button() {
    switch (!(elInputUsername.value && elInputPassword.value && elInputPasswordretype.value && elNumbertype.value && elInputPassword.value === elInputPasswordretype.value)) {
        case true : elJoinbutton.disabled = true; break;
        case false : elJoinbutton.disabled = false; break;
    }
}