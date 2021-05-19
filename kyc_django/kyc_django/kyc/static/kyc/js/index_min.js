function validate()
      {
        //alert("hello");
        var NIC = document.getElementById("NIC").value;
        var drlicense = document.getElementById("drlicense").value;
        var drive_exp = document.getElementById("drive_exp").value;
        var passport = document.getElementById("passport").value;
        var passport_exp = document.getElementById("passport_exp").value;
        var Nationality = document.getElementById("Nationality").value;
        var otherNationality = document.getElementById("otherNationality").value;
        var birthday = document.getElementById("birthday").value;
        var Mobile = document.getElementById("mobile").value;
        var Officetel = document.getElementById("officetel").value;
        var Hometel = document.getElementById("hometel").value;
        var email = document.getElementById("email").value;
        var fullName = document.getElementById("fullName").value;
        var nwi = document.getElementById("nwi").value;
        var ID_type = document.getElementById("ID_type").value;
        var houseNo = document.getElementById("houseNo").value;
        var street = document.getElementById("street").value;
        var city = document.getElementById("city").value;
        var country = document.getElementById("country").value;

        
        if(ID_type!="" && NIC!="" && NIC.length!=9 && NIC.length!=11)
        {
          alert("Invalid NIC Number");
          return false;
        }
        else if(drlicense!="" && drive_exp=="")
        {
          alert("Fill the expiration date of driving licence.");
          return false;
        }
        else if(passport!="" && passport_exp=="")
        {
          alert("Fill the expiration date of passport.");
          return false;
        }
        else if(Nationality=="Other" && otherNationality=="")
        {
          alert("Fill Your Nationality.");
          return false;
        }
        else if(Nationality=="Sri Lankan" && otherNationality!="")
        {
          alert("Fill Your Nationality Correctly.");
          return false;
        }
        else if(fullName!="" && nwi!="" && ID_type!="" && NIC!="" && Nationality!="" && birthday!="" && houseNo!="" && street!="" && city!="" && country!="" && Mobile=="" && Officetel=="" && Hometel=="" && email=="")
        {
          alert("Fill aleast one of following contact information.");
          return false;
        }
        else if(Mobile!="" && Mobile.length!=10)
        {
          alert("Fill the Mobile contact number with 10 digits.");
          return false;
        }
        else if(Officetel!="" && Officetel.length!=10)
        {
          alert("Fill the Office contact number with 10 digits.");
          return false;
        }
        else if(Hometel!="" && Hometel.length!=10)
        {
          alert("Fill the Home contact number with 10 digits.");
          return false;
        }
        else if(email!="" &&(email.indexOf("@")==-1 || email.lastIndexOf(".")==-1))
        {
          alert("Email Address is Invalid");
          return false;
        }
        else
        {
          return true;
        }

      }

//===================================================
      function isnumber(event)
      {
        var isNumb = String.fromCharCode(event.which);

        if(!(/[0-9]/.test(isNumb)))
        {
          event.preventDefault();
        }
      }
//======================================================
      function lettersOnly(input)
      {
        var regex = /[^a-z]/gi;
        input.value = input.value.replace(regex, "");
      }


function choicesCompleted() {
  var c = 0;
  var e= document.getElementsByTagName('input');
  var inactive_text = $('input[type="text"]:disabled');
  var inactive_num = $('input[type="number"]:disabled');
  var inactive_file = $('input[type="file"]:disabled');
  var inactive_date = $('input[type="date"]:disabled');
  var inactive_radio = $('input[type="radio"]:disabled');
  var inactive_email = $('input[type="email"]:disabled');
  var inactive = (inactive_text.length+inactive_num.length+inactive_file.length+inactive_date.length+inactive_radio.length+inactive_email.length);
	var inactiv_col = inactive;

  for (i = 0; i < (e.length-3); i++) {

    if ((document.getElementById("mobile").value !== '') && (i==0)) {
      c = c + 1;
    }
    else if ((document.getElementById("officetel").value !== '') && (i==1)) {
      c = c + 1;
    }
    else if ((document.getElementById("hometel").value !== '') && (i==2)) {
      c = c + 1;
    }
    else if ((document.getElementById("email").value !== '') && (i==3)) {
      c = c + 1;
    }

  }
  var ans = (c/(e.length-inactiv_col-3))*100;
  document.getElementById("profile_rate").value = ans + "%";
  document.getElementById("showc1").innerHTML = inactiv_col;
  document.getElementById("showc2").innerHTML = e.length-3;
}