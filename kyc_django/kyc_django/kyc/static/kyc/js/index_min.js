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

          if ((document.getElementById("nwi").value !== '') && (i==0)) {
            c = c + 1;
          }
          else if ((document.getElementById("fullName").value !== '') && (i==1)) {
            c = c + 1;
          }
          else if ((document.getElementById("img").value !== '') && (i==2)) {
            c = c + 1;
          }
          else if ((document.getElementById("vid").value !== '') && (i==3)) {
            c = c + 1;
          }
          else if ((document.getElementById("NIC").value !== '') && (i==4)) {
            c = c + 1;
          }
          else if ((document.getElementById("birthday").value !== '') && (i==5)) {
            c = c + 1;
          }
          else if ((document.getElementById("drlicense").value !== '') && (i==6)) {
            c = c + 1;
          }
          else if ((document.getElementById("drive_exp").value !== '') && (i==7)) {
            c = c + 1;
          }
          else if ((document.getElementById("passport").value !== '') && (i==8)) {
            c = c + 1;
          }
          else if ((document.getElementById("passport_exp").value !== '') && (i==9)) {
            c = c + 1;
          }
          else if ((document.getElementById("BRC").value !== '') && (i==10)) {
            c = c + 1;
          }
          else if ((document.getElementById("PID").value !== '') && (i==11)) {
            c = c + 1;
          }
          else if ((document.getElementById("OAFSC").value !== '') && (i==12)) {
            c = c + 1;
          }
          else if ((document.getElementById("imgVisa").value !== '') && (i==13)) {
            c = c + 1;
          }
          else if ((document.getElementById("imgOther").value !== '') && (i==14)) {
            c = c + 1;
          }
          else if ((document.getElementById("otherNationality").value !== '') && (i==15)) {
            c = c + 1;
          }
          else if ((document.getElementById("visa_exp").value !== '') && (i==16)) {
            c = c + 1;
          }
          else if ((document.getElementById("type_of_your_visa").value !== '') && (i==17)) {
            c = c + 1;
          }
          else if ((document.getElementById("visa_exp_other").value !== '') && (i==18)) {
            c = c + 1;
          }
          else if ((document.getElementById("foreign_address").value !== '') && (i==19)) {
            c = c + 1;
          }
          else if ((document.getElementById("img2").value !== '') && (i==20)) {
            c = c + 1;
          }
          else if ((document.getElementById("pep_id1").value !== '') && (i==21)) {
            c = c + 1;
          }
          else if ((document.getElementById("us_id1").value !== '') && (i==22)) {
            c = c + 1;
          }
          
          else if ((document.getElementById("res_id1").value !== '') && (i==23)) {
            c = c + 1;
          }
          
          else if ((document.getElementById("houseNo").value !== '') && (i==24)) {
            c = c + 1;
          }
          else if ((document.getElementById("street").value !== '') && (i==25)) {
            c = c + 1;
          }
        
          else if ((document.getElementById("postal_code").value !== '') && (i==26)) {
            c = c + 1;
          }
          else if ((document.getElementById("houseNo2").value !== '') && (i==27)) {
            c = c + 1;
          }
          else if ((document.getElementById("street2").value !== '') && (i==28)) {
            c = c + 1;
          }
          
          else if ((document.getElementById("postal_code2").value !== '') && (i==29)) {
            c = c + 1;
          }
          else if ((document.getElementById("mobile").value !== '') && (i==30)) {
            c = c + 1;
          }
          else if ((document.getElementById("officetel").value !== '') && (i==31)) {
            c = c + 1;
          }
          else if ((document.getElementById("hometel").value !== '') && (i==32)) {
            c = c + 1;
          }
          else if ((document.getElementById("email").value !== '') && (i==33)) {
            c = c + 1;
          }
          

        }
        var ans1 = (c/(e.length-inactiv_col-5))*100;
        if (ans1>=100){
          ans = 100;
        }
        else{
          ans = ans1
        }
        document.getElementById("profile_rate").value = ans + "%";
        document.getElementById("showc1").innerHTML = inactiv_col;
        document.getElementById("showc3").innerHTML = c;
        document.getElementById("showc2").innerHTML = e.length-5;
      }