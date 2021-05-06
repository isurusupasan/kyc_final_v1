function validate_2()
{
  var haveAcc = document.getElementById("haveAcc");
  var noAcc = document.getElementById("noAcc");
  var chec1 = document.getElementsByName("chec1");
  var chec2 = document.getElementsByName("chec2");
  var chec3 = document.getElementsByName("chec3");
  var chec4 = document.getElementsByName("chec4");
  var haschecked1 = false; 
  var haschecked2 = false;
  var haschecked3 = false;
  var haschecked4 = false;

  for (var i=0; i<chec1.length; i++)
  {
    if(chec1[i].checked)
          {
            haschecked1=true;
            break;         
          }
  }

  for (var j=0; j<chec2.length; j++)
  {
    if(chec2[j].checked)
          {
            haschecked2=true;
            break;
          }
  }

  for (var m=0; m<chec3.length; m++)
  {
    if(chec3[m].checked)
          {
            haschecked3=true;
            break;
          }
  }

  for (var p=0; p<chec4.length; p++)
  {
    if(chec4[p].checked)
          {
            haschecked4=true;
            break;
          }
  }

//==============================================================================================================

  if(haveAcc.checked!=true && noAcc.checked!=true)
  {
    alert("Fill wheather that you have or don't have an account already.");
    return false;
    
  }
  else if(haschecked1==false)
  {
    alert("Please select your account type(s).");
    return false;
  }
  else if(haschecked2==false)
  {
    alert("Please Selecte Your Purpose(s) of the Account.");
    return false;
  }
  else if(document.getElementById("Occutation_Status").value=="")
  {
    alert("Please Fill Your Occupation Status.");
    //return false;
  }
  else if(document.getElementById("occupation").value=="")
  {
    alert("Please Fill Your Occupation.");
    //return false;
  }
  else if(haschecked3==false)
  {
    alert("Please Selecte Your Source(s) of Income.");
    return false;
  }
  else if(document.getElementById("otherIncome").checked==true && document.getElementById("other_Incometypes").value=="")
  {
    alert("Mention Your Other Incomes.");
    return false;
  }
  else if(document.getElementById("other_Incometypes").value!="" && document.getElementById("otherIncome").checked!=true)
  {
    alert("To provide the other income source(s), please tick the 'Other' option in income feild.");
    return false;
  }
  else if(document.getElementById("Average_Income").value=="")
  {
    alert("Please Select Your Average Monthly Income.");

  }
  else if(haschecked4==false)
  {
    alert("Please Select Mode(s) of Transaction..");
    return false;
  }
  else
  {
    return true;
  }
 
}

//==============================================================

function lettersOnly(input)
      {
        var regex = /[^a-z]/gi;
        input.value = input.value.replace(regex, "");
      }