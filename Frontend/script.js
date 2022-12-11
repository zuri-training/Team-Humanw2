const mainContent = document.querySelector(".main-content");
const closeModal = document.querySelector(".btn-close")
const forgotPasswordBtn = document.querySelector(".forgot-btn");
const forgotPasswordModal = document.querySelector(".forgot-modal");
const forgotPasswordForm = document.querySelector(".forgot-form");
const backToSignin = document.querySelector(".to-signin");

forgotPasswordBtn.addEventListener("click", function(){
    forgotPasswordModal.style.display = "flex";
    mainContent.style.display = "none";
})

backToSignin.addEventListener('click', () => {
    forgotPasswordModal.style.display = "none";
    mainContent.style.display = "flex";
})