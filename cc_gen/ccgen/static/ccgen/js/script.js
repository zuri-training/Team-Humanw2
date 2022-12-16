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

fetch('/update-download-field/', {
    method: 'POST',
    body: JSON.stringify({
      'id': {{ design.id }},
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
    // Do something with the response data here, if necessary
  });
  