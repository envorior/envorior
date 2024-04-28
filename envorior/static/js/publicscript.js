let url = "http://127.0.0.1:8000"; // Base URL of the Django app



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
  

  <form action="{% url 'publicapp:uploadpost' %}" method='POST' enctype="multipart/form-data">
  {% csrf_token %}
  <div class="txt-box"><textarea type="text" name="caption" rows="8" placeholder=" Message "></textarea></div>
 <div class="search"><input type="file" name="pimg" placeholder=" Upload Media (Image) "></div>
  <button type="submit" class="btn btn-primary">Post Now</button>
</form>
  
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
