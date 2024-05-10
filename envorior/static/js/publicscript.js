let url = "http://127.0.0.1:8000"; // Base URL of the Django app

// javascript for handling profile page

document.addEventListener("DOMContentLoaded",function(){
 
let postbtn=document.querySelector(".profile-post-btn");
let posts=document.querySelectorAll(".profile-post");
let jobbtn=document.querySelector(".profile-job-btn");
let jobs=document.querySelectorAll(".profile-job");
let donationbtn=document.querySelector(".profile-donation-btn");
let donations=document.querySelectorAll(".profile-donation");
let complainbtn=document.querySelector(".profile-complain-btn");
let complains=document.querySelectorAll(".profile-complain");


postbtn.addEventListener("click",function(){
  
  posts.forEach(function(post){
    post.style.display="block";
  });
  jobs.forEach(function(job){
    job.style.display="none";
  });
  donations.forEach(function(donation){
    donation.style.display="none";
  });
  complains.forEach(function(complain){
    complain.style.display="none";
  });

});

jobbtn.addEventListener("click",function(){

  jobs.forEach(function(job){
    job.style.display="block";
  });
  posts.forEach(function(post){
    post.style.display="none";
  });
  donations.forEach(function(donation){
    donation.style.display="none";
  });
  complains.forEach(function(complain){
    complain.style.display="none";
  });

});

donationbtn.addEventListener("click",function(){

  donations.forEach(function(donation){
    donation.style.display="block";
  });
  jobs.forEach(function(job){
    job.style.display="none";
  });
  posts.forEach(function(post){
    post.style.display="none";
  });
  complains.forEach(function(complain){
    complain.style.display="none";
  });

});

complainbtn.addEventListener("click",function(){

  complains.forEach(function(complain){
    complain.style.display="block";
  });
  jobs.forEach(function(job){
    job.style.display="none";
  });
  donations.forEach(function(donation){
    donation.style.display="none";
  });
  posts.forEach(function(post){
    post.style.display="none";
  });
  
});

});


// // JavaScript to handle form submission
// document.addEventListener("DOMContentLoaded", function() {
//     var form = document.getElementById("myForm");

//     form.addEventListener("submit", function(event) {
//         event.preventDefault(); // Prevent default form submission behavior

//         var formData = new FormData(form); // Get form data
//         var xhr = new XMLHttpRequest();

//         xhr.open("POST", `${url}/uploadpost`, true); // Replace 'your_view_name' with the name of your Django view
//         xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); // Set CSRF token

//         xhr.onreadystatechange = function() {
//             if (xhr.readyState === XMLHttpRequest.DONE) {
//                 if (xhr.status === 200) {
//                     // Handle successful response
//                     console.log(xhr.responseText);
//                 } else {
//                     // Handle error
//                     console.error("Error:", xhr.status);
//                 }
//             }
//         };

//         xhr.send(formData); // Send form data
//     });
// });


// JavaScript to toggle the popup
// document.addEventListener("DOMContentLoaded", function() {
//   var popup = document.getElementById("popup");
//   var closeButton = document.querySelector(".close");
//   var postButton = document.querySelector(".postbutton");
 
 
//   // Close the popup when the close button is clicked
//   closeButton.addEventListener("click", function(){
//     popup.style.display = "none";
//   });
  
//   // Show the popup initially (you can trigger this based on certain events)
//   postButton.addEventListener("click", function(){
//     popup.style.display = "block";
//   });
// });



// // logout
// const myModal = document.getElementById('exampleModalLabel')
// const myInput = document.getElementById('myInput')

// myModal.addEventListener('shown.bs.modal', () => {
//   myInput.focus()
// })