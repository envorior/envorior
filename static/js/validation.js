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

    if (email.value==null || email.value==""){
        text="Email is Required";
        document.getElementById("validationresult").innerHTML = text;
    } 
    else if (contact.value==null || contact.value==""){
        text="Contact Number is Required";
        document.getElementById("validationresult").innerHTML = text;
    }
    else if(contact.value.toString().length < 10 || contact.value.toString().length > 10 ){
        text="Please Enter Correct Contact Number";
        document.getElementById("validationresult").innerHTML = text;
    }
    else if(name==null || name==""){
        text="Name is Required";
        document.getElementById("validationresult").innerHTML = text;
    }
    else if(name.toString().length>50  ){
        text="Name is greater then 50 character";
        document.getElementById("validationresult").innerHTML = text;
    }
    else if(password1 != password2){
        text="Password Mismatch";
        document.getElementById("validationresult").innerHTML = text;
    }
    else if(dob==null || dob==""){
        text="DOB is Required";
        document.getElementById("validationresult").innerHTML = text;
    }
    else if(state==null || state==""){
        text="State is Required";
        document.getElementById("validationresult").innerHTML = text;
    }
    else if(city==null || city==""){
        text="City is Required";
        document.getElementById("validationresult").innerHTML = text;
    }
    else if(pin==null || pin==""){
        text="Pin code is Required";
        document.getElementById("validationresult").innerHTML = text;
    }
    else
        {
          document.getElementById('registrationform').submit();
        }        
    

        
}

function login(){
    let email = document.getElementById("email");
    let contact = document.getElementById('password');
    if (email.value==null || email.value==""){
            text="Email is Required";
            document.getElementById("validationresult").innerHTML = text;
        } 
    else if (contact.value==null || contact.value==""){
            text="Password is Required";
            document.getElementById("validationresult").innerHTML = text;
        }
    else
        {
          document.getElementById('loginform').submit();
        }        
    


}