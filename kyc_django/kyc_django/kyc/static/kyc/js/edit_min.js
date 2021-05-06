function select_rejection(){
    if(document.getElementById("Reject").value == "accept_val"){
        document.getElementById("rej_1").disabled = 'true';
        document.getElementById("rej_2").disabled = 'true';
        document.getElementById("rej_3").disabled = 'true';
        document.getElementById("rej_4").disabled = 'true';
        document.getElementById("rej_5").disabled = 'true';
        

    }
    else if(document.getElementById("Reject").value == "reject_val"){
        document.getElementById("rej_1").disabled = '';
        document.getElementById("rej_2").disabled = '';
        document.getElementById("rej_3").disabled = '';
        document.getElementById("rej_4").disabled = '';
        document.getElementById("rej_5").disabled = '';
        
        
   }
}
