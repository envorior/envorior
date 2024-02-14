function other_settings() {
    
   popup();
    
}

function popup(){
    var popup = document.createElement("div");
    popup.classList.add("popup"); // Use classList.add() to add a class
    document.body.appendChild(popup); // Use document.body to select the body element
    popup.style.backdropFilter="blur(9px)"; // Use document.body to select the body element
    popup.style.height = "50vh";
    popup.style.width = "50vw";
    popup.style.backgroundColor = "var(--white)"; // Use backgroundColor instead of backgroundcolor
    popup.style.borderRadius = "var(--border-radius)"; // Use backgroundColor instead of backgroundcolor
    popup.style.position = "fixed";
    popup.style.top = "25%";
    popup.style.left = "25%";
    popup.style.zIndex = "10";
}

