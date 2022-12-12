const forgotPasswordModal = document.querySelector(".forgot-modal"),
forgotPasswordForm = document.querySelector(".forgot-form");

// This function get the user mail then add it to the login verify modal

function showUserEmail() {
    let userEmail = document.querySelector("#recovery-email").value;
    document.querySelector('.user-mail').innerText = userEmail;
}

// This function displays the login verify modal after the user has submitted the form

forgotPasswordForm.addEventListener('submit', (event) => {
    event.preventDefault();
    document.querySelector('.login-verify-modal').style.display = "flex";
    forgotPasswordModal.style.display = "none";

    showUserEmail();
})
