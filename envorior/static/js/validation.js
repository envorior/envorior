// fpr registration page
function registration(){
    let email = document.getElementById("email");
    let contact = document.getElementById('contact');
    let name = document.getElementById('name').value;
    let dob = document.getElementById('dob').value;
    let state = document.getElementById('state').value;
    let city = document.getElementById('city').value;
    let pin = document.getElementById('pin').value;
    let password1 = document.getElementById('password1').value;
    let password2 = document.getElementById('password2').value;

    // if (email.value==null || email.value==""){
    //     text="Email is Required";
    // } 
    // else if (contact.value==null || contact.value==""){
    //     text="Contact Number is Required";
    // }
    // else if(contact.value.toString().length < 10 || contact.value.toString().length > 10 ){
    //     text="Please Enter Correct Contact Number";
    // }
    // else if(name==null || name==""){
    //     text="Name is Required";
    // }
    // else if(name.toString().length>50  ){
    //     text="Name is greater then 50 character";
    // }
    // else if(password1 != password2){
    //     text="Password Mismatch";
    // }
    // document.getElementById("validationresult").innerHTML = text;

    if (email.value==null || email.value==""){
        alert("Email is Required");
        email.focus();
    } 
    else if (contact.value==null || contact.value==""){
        alert("Contact Number is Required")
        contact.focus()
    }
    else if(contact.value.toString().length < 10 || contact.value.toString().length > 10 ){
        alert("Please Enter Correct Contact Number")
        contact.focus()
    }
    else if(name==null || name==""){
        alert("Name is Required")
        name.focus()
    }
    else if(name.toString().length>50  ){
        alert("Name is greater then 50 character")
        name.focus()
    }
    else if(password1 != password2){
        alert("Password Mismatch")
        password2.focus()
    }
    document.getElementById("validationresult").innerHTML = text;
    
}