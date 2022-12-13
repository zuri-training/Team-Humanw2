const forgotPasswordModal = document.querySelector(".forgot-modal"),
forgotPasswordForm = document.querySelector(".forgot-form"),
loginVerifyModal = document.querySelector(".login-verify-modal");
backToForgotPassword = document.querySelector(".to-forgot-password");

// This function get the user mail then add it to the login verify modal
console.log(backToForgotPassword)

function showUserEmail() {
    let userEmail = document.querySelector("#recovery-email").value;
    document.querySelector('.user-mail').innerText = userEmail;
}

// This function displays the login verify modal after the user has submitted the form

forgotPasswordForm.addEventListener('submit', (event) => {
    event.preventDefault();
    loginVerifyModal.style.display = "flex";
    forgotPasswordModal.style.display = "none";

    showUserEmail();
})

backToForgotPassword.addEventListener('click', () => {
    loginVerifyModal.style.display = "none";
    forgotPasswordModal.style.display = "flex";
    console.log("It's working fine")
})
