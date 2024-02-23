var url ="http://127.0.0.1:8000"

function other_settings() {
    let top="25%";
    let left="50%";
    let height="50vh";
    let width="50vw";
    let html=`<div><a href="{url}/login"
      class="text-decoration-none"
    >
      <span class="txt-2"><i class="fa-solid fa-house"></i></span>
      <span class="txt-2">Home</span>
    </a>
  </div>

  <div>
    <a
      href="{%url 'publicapp:profile'%}"
      class="text-decoration-none"
    >
      <span class="txt-2"><i class="fa-solid fa-house"></i></span>
      <span class="txt-2">Profile</span>
    </a>
  </div>

  <div>
    <a href="{%url 'publicapp:donation'%}" class="text-decoration-none">
      <span class="txt-2"
        ><i class="fa-solid fa-hand-holding-dollar"></i
      ></span>
      <span class="txt-2">Donation</span>
    </a>
  </div>`;
   popup(top,left,height,width,html);
    
}

function popup(top, left, height, width,html){
    var popup = document.createElement("div");
    popup.classList.add("popup"); 
    popup.innerHTML=html;// Use classList.add() to add a class
    document.body.appendChild(popup); // Use document.body to select the body element
    popup.style.backdropFilter="blur(9px)"; // Use document.body to select the body element
    popup.style.height = height;
    popup.style.width = width;
    popup.style.backgroundColor = "var(--white)"; // Use backgroundColor instead of backgroundcolor
    popup.style.borderRadius = "var(--border-radius)"; // Use backgroundColor instead of backgroundcolor
    popup.style.position = "fixed";
    popup.style.top = top;
    popup.style.left = left;
    popup.style.zIndex = "10";
}

