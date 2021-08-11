const registerDiv = document.querySelector('.login-reg')
const backToLogin = document.getElementById('blogin')
const loginDiv = document.querySelector('.login-div')
const accId = document.getElementById('account')
const containerRight = document.querySelector('.container-right')
const loginBtn = document.getElementById('on-login')

//default value or functions
registerDiv.remove()


accId.addEventListener('click',function(){
    loginDiv.remove()
    containerRight.appendChild(registerDiv)
});



const goBack = () => {
  registerDiv.remove()
  loginDiv.classList.add('appear')
  containerRight.appendChild(loginDiv)
  
  
}

const moveToToDo = () => {
  location.href = "../pages/todo.html"

}


backToLogin.addEventListener('click',goBack)
loginBtn.addEventListener('click', moveToToDo)