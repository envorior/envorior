let url = "http://127.0.0.1:8000"; // Base URL of the Django app



// function logout() {
//   let top = "25%";
//   let left = "25%";
//   let height = "50vh";
//   let width = "50vw";
  
//   let html = `
//   <div id="form-layout">
// <form >
//   <div class="btn"><button type="submit">Yes</button></div>
//   <div class="btn"><button type="submit">No</button></div>
// </form>
// </div>`;
//   popup(top, left, height, width, html);
// }

// function post() {
//   let top = "25%";
//   let left = "25%";
//   let height = "50vh";
//   let width = "50vw";
  
//   let html = `

//   <div class="feed-post">
//    <div class="feed-header">
//       <div class="user-profile">
//          <!-- get profile picture of postby -->
//                {% if post.postby.profile_picture %}
//                <a href="{%url 'publicapp:profile'%}">
//                <img class="profile-img" src="{{ post.postby.profile_picture.url }}" alt=""/>
//                </a>
//                {% else %}
//                <a href="{%url 'publicapp:profile'%}">
//                <img class="profile-img" src="{% static 'img/profile.png' %}" alt=""/>
//                </a>
//                {% endif %}
//          <div class="profile-txt">
//           <a href="" class="txt-2"><p>{{post.postby.full_name}}</p></a>
//           <a href="" class="txt-3"><p>{{post.posteddate}}</p></a>
          
//        </div>     
//              </div>
//    </div>
//    <div class="feed-content">
//    <form action="{% url 'publicapp:uploadpost' %}" method='POST' enctype="multipart/form-data">
//    {% csrf_token %}
//    <div class="txt-box"><textarea type="text" name="caption" rows="8" placeholder=" Message "></textarea></div>
//   <div class="search"><input type="file" name="pimg" placeholder=" Upload Media (Image) "></div>
//    <button type="submit" class="btn btn-primary">Post Now</button>
//  </form>
           
//    </div>
 
// </div>

  
//   `;
//   popup(top, left, height, width, html);
// }



// function popup(top, left, height, width, html) {
//   var popupBackground=document.createElement("div");
//   popupBackground.classList.add("popupBackground");
//   document.body.appendChild(popupBackground);
//   var popup = document.createElement("div");
//   popup.classList.add("popup");
//   popup.innerHTML = html;
//   document.body.appendChild(popup);
//   popup.style.height = height;
//   popup.style.width = width;
//   popup.style.top = top;
//   popup.style.left = left;
// }


// JavaScript to handle form submission
document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("myForm");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission behavior

        var formData = new FormData(form); // Get form data
        var xhr = new XMLHttpRequest();

        xhr.open("POST", `${url}/uploadpost`, true); // Replace 'your_view_name' with the name of your Django view
        xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}"); // Set CSRF token

        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Handle successful response
                    console.log(xhr.responseText);
                } else {
                    // Handle error
                    console.error("Error:", xhr.status);
                }
            }
        };

        xhr.send(formData); // Send form data
    });
});


// JavaScript to toggle the popup
document.addEventListener("DOMContentLoaded", function() {
  var popup = document.getElementById("popup");
  var closeButton = document.querySelector(".close");
  var postButton = document.querySelector(".postbutton");
 
 
  // Close the popup when the close button is clicked
  closeButton.addEventListener("click", function(){
    popup.style.display = "none";
  });
  
  // Show the popup initially (you can trigger this based on certain events)
  postButton.addEventListener("click", function(){
    popup.style.display = "block";
  });
});



// logout
const myModal = document.getElementById('exampleModalLabel')
const myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})