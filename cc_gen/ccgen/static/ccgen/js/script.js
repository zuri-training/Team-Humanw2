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

function downloaded(design){
  let designid=document.getElementById("designid-"+ design)
  let design_id=designid.innerHTML;
  designid.style.display="none";

  let url1=document.getElementById("url-"+ design)
  let url=url1.innerHTML;
  url1.style.display="none";
  console.log(document.getElementById("download-"+ design))
fetch(url, {
    method: 'POST',
    credentials: "same-origin",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Accept": "application/json",
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'id': design_id}),
  
  }
)
    .then(function(response) {
    return response.json();
  }).then(function(data) {
    // Do something with the response data here, if necessary
    if (data.success=true){
      console.log(true);
      document.getElementById("download-"+ design).innerHTML="Downloaded✅";
    }


  });
}

function save_download(design){
  let designid=document.getElementById("designid-"+ design)
  let design_id=designid.innerHTML;
  designid.style.display="none";

  let url1=document.getElementById("save-url-"+ design)
  let url=url1.innerHTML;
  url1.style.display="none";
  console.log(document.getElementById("download-"+ design))
fetch(url, {
    method: 'POST',
    credentials: "same-origin",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Accept": "application/json",
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'id': design_id}),
  
  }
)
    .then(function(response) {
    return response.json();
  }).then(function(data) {
    // Do something with the response data here, if necessary
    if (data.success=true){
      console.log(true);
      document.getElementById("download-"+ design).innerHTML="saved for later download✅";
    }


  });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}