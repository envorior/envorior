let url = "http://127.0.0.1:8000"; // Base URL of the Django app

function other_settings() {
  let top = "8%";
  let left = "75%";
  let height = "80vh";
  let width = "15vw";
  let html = `
  <div class="navleftmiddle">

  <div><a href="${url}/login" class="text-decoration-none">
      <span class="txt-2"><i class="fa-solid fa-house"></i></span>
      <span class="txt-2">Home</span>
      </a>
  </div>

  <div>
      <a href="${url}/notifications" class="text-decoration-none">
      <span class="txt-2"><i class="fa-solid fa-house"></i></span>
      <span class="txt-2">notifications</span>
      </a>
  </div>

  <div>
      <a href="${url}/followers" class="text-decoration-none">
      <span class="txt-2"><i class="fa-solid fa-hand-holding-dollar"></i></span>
      <span class="txt-2">followers</span>
      </a>
  </div>
  <div>
      <a href="${url}/followings" class="text-decoration-none">
      <span class="txt-2"><i class="fa-solid fa-hand-holding-dollar"></i></span>
      <span class="txt-2">followings</span>
      </a>
  </div>
  <div>
      <a href="${url}/complain" class="text-decoration-none">
      <span class="txt-2"><i class="fa-solid fa-hand-holding-dollar"></i></span>
      <span class="txt-2">complain</span>
      </a>
  </div>
  <div>
      <a href="#" class="text-decoration-none" onclick="logout()">
      <span class="txt-2"><i class="fa-solid fa-hand-holding-dollar"></i></span>
      <span class="txt-2">Logout</span>
      </a>
  </div>
  </div>
  `;
  popup(top, left, height, width, html);
}
function settings() {
  let top = "8%";
  let left = "10%";
  let height = "80vh";
  let width = "15vw";
  let html = `
  <div class="navleftmiddle">

  <div><a href="${url}/login" class="text-decoration-none">
      <span class="txt-2"><i class="fa-solid fa-house"></i></span>
      <span class="txt-2">Home</span>
      </a>
  </div>

  <div>
      <a href="${url}/notifications" class="text-decoration-none">
      <span class="txt-2"><i class="fa-solid fa-house"></i></span>
      <span class="txt-2">notifications</span>
      </a>
  </div>

  <div>
      <a href="${url}/followers" class="text-decoration-none">
      <span class="txt-2"><i class="fa-solid fa-hand-holding-dollar"></i></span>
      <span class="txt-2">followers</span>
      </a>
  </div>
  <div>
      <a href="${url}/followings" class="text-decoration-none">
      <span class="txt-2"><i class="fa-solid fa-hand-holding-dollar"></i></span>
      <span class="txt-2">followings</span>
      </a>
  </div>
  <div>
      <a href="${url}/complain" class="text-decoration-none">
      <span class="txt-2"><i class="fa-solid fa-hand-holding-dollar"></i></span>
      <span class="txt-2">complain</span>
      </a>
  </div>
  <div>
      <a href="#" class="text-decoration-none" onclick="logout()">
      <span class="txt-2"><i class="fa-solid fa-hand-holding-dollar"></i></span>
      <span class="txt-2">Logout</span>
      </a>
  </div>
  </div>
  `;
  popup(top, left, height, width, html);
}

function logout() {
  let top = "25%";
  let left = "25%";
  let height = "50vh";
  let width = "50vw";
  
  let html = `
  <div id="form-layout">
<form >
  <div class="btn"><button type="submit">Yes</button></div>
  <div class="btn"><button type="submit">No</button></div>
</form>
</div>`;
  popup(top, left, height, width, html);
}
function post() {
  let top = "25%";
  let left = "25%";
  let height = "50vh";
  let width = "50vw";
  
  let html = `
  <div class="feed-post">
  <div class="feed-header">
     <div class="user-profile">
        <a><img class="profile-img" src="{% static 'img/user.jpeg' %}" alt=""></a>
        <div class="profile-txt">
         <a href="" class="txt-2"><p>{{post.postedby.full_name}}</p></a>
         <a href="" class="txt-3"><p>{{post.posteddate}}</p></a>
         
      </div>     
            </div>
  </div>

  <form >
  <div class="txt-box"><textarea type="text" rows="20" placeholder=" Message "></textarea></div>

   <div class="search"><input type="file" placeholder=" Upload Media (Image) "><div class="btn"><button type="submit">Post</button></div></div>
   
   
</form>


   
  
  </div>
</div> 
  `;
  popup(top, left, height, width, html);
}



function popup(top, left, height, width, html) {
  var popupBackground=document.createElement("div");
  popupBackground.classList.add("popupBackground");
  document.body.appendChild(popupBackground);
  var popup = document.createElement("div");
  popup.classList.add("popup");
  popup.innerHTML = html;
  document.body.appendChild(popup);
  popup.style.height = height;
  popup.style.width = width;
  popup.style.top = top;
  popup.style.left = left;
}
