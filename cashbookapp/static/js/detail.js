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

// 좋아요 버튼
const heart = document.querySelector(".heart");
const animationHeart = document.querySelector(".animation-heart");

heart.addEventListener('click', () => {
    animationHeart.classList.add('animation');
    heart.classList.add('fill-colot');
})

animationHeart.addEventListener('click', () => {
    animationHeart.classList.remove('animation');
    heart.classList.remove('fill-color');
})