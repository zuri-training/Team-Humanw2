<<<<<<< HEAD
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
=======
const forgotPasswordModal = document.querySelector(".forgot-modal"),
forgotPasswordForm = document.querySelector(".forgot-form");

// This function get the user mail then add it to the login verify modal

function showUserEmail() {
    let userEmail = document.querySelector(".recover").value;
    console.log(userEmail)
    document.querySelector('.user.mail').write("my message");
}

// This function displays the login verify modal after the user has submitted the form

forgotPasswordForm.addEventListener('submit', () => {
    event.preventDefault();
    document.querySelector('.login-verify-modal').style.display = "flex";
    forgotPasswordModal.style.display = "none";
    showUserEmail;
})
>>>>>>> ccffc4621495f1159bf2d85e8331919aca963d71
