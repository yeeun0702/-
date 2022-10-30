let modal = document.querySelector('#modal-b'),
    modalBtn = document.querySelector('#modal-btn'),
    modalClose = document.querySelector('#modal-close');

function activeModal() {
    console.log("open");
    modal.classList.add('active');
    document.querySelector('body').style.overflow = 'hidden';
}

function hideModal() {
    console.log("asdf");
    modal.classList.remove('active');
    document.querySelector('body').style.overflow = 'visible';
}

modalBtn.addEventListener('click', activeModal)
modalClose.addEventListener('click', hideModal)