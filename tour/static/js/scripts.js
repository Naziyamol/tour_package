// const form = document.querySelector("form"),
//     nextBtn = form.querySelector(".nextBtn"),
//     backBtn = form.querySelector(".backBtn"),
//     firstForm = form.querySelector(".first"),
//     secondForm = form.querySelector(".second");

// nextBtn.addEventListener("click", () => {
//     // Check if all input fields in the first form are filled
//     const isFilled = Array.from(firstForm.querySelectorAll("input")).every(input => input.value.trim() !== "");
//     if (isFilled) {
//         form.classList.add("secActive");
//     } else {
//         // If any input field is empty, display an alert or provide visual feedback
//         alert("Please fill in all fields before proceeding.");
//     }
// });

// backBtn.addEventListener("click", () => form.classList.remove("secActive"));





// scripts.js

// scripts.js

// document.addEventListener('DOMContentLoaded', function() {
//     const userRadio = document.getElementById('user');
//     const vendorRadio = document.getElementById('vendor');
//     const sliderTab = document.querySelector('.slider-tab');
  
//     userRadio.addEventListener('click', function() {
//       sliderTab.style.left = '0';
//     });
  
//     vendorRadio.addEventListener('click', function() {
//       sliderTab.style.left = '50%';
//     });
//   });


  const loginText = document.querySelector(".title-text .user");
      const loginForm = document.querySelector("form.user");
      const loginBtn = document.querySelector("label.user");
      const signupBtn = document.querySelector("label.vendor");
      const signupLink = document.querySelector("form .signup-link a");
      signupBtn.onclick = (()=>{
        loginForm.style.marginLeft = "-50%";
        loginText.style.marginLeft = "-50%";
      });
      loginBtn.onclick = (()=>{
        loginForm.style.marginLeft = "0%";
        loginText.style.marginLeft = "0%";
      });
      signupLink.onclick = (()=>{
        signupBtn.click();
        return false;
      });

      document.getElementById('login-form').addEventListener('submit', function(event) {
        // Get the selected value of user_type
        var userType = document.querySelector('input[name="user_type"]:checked').value;
        // Set the value of hidden_user_type input field
        document.getElementById('user_type').value = userType;
    });