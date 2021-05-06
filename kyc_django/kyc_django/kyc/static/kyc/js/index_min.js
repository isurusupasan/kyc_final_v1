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


