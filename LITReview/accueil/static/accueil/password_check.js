// var password = document.getElementById("id_password").value;
// var verify_password = document.getElementById("id_verify_password").value;

// document.body.style.backgroundColor = "red";


// if(password == verify_password){
//     button = document.getElementById("inscriptio-submit").disabled = true;
// }

function checkPassword(){
  if (document.getElementById('id_password').value == document.getElementById('id_verify_password').value) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'matching';
    document.getElementById('inscriptio-submit').disabled = false;
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'not matching';
    document.getElementById('inscriptio-submit').disabled = true;

  }
}


window.addEventListener('load', function() {
    console.log('All assets are loaded')
    let password = document.getElementById('id_password');
    password.addEventListener('keyup', checkPassword);

    let verify_password = document.getElementById('id_verify_password');
    verify_password.addEventListener('keyup', checkPassword);
})
