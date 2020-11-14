document.getElementById("submit").addEventListener('click', async () => {
    const Bt_State = document.getElementById('bt_state').innerHTML;
    if (Bt_State) {
      console.log(Bt_State)
      response = await fetch("/", {
        method: "POST",
        headers: {
          'Content-Type': "application/json",
        },
        body: JSON.stringify({
                    Bt_State: Bt_State
                })
            });
        
        if(response.status == 200){
          if(Bt_State=='connected'){
  
            document.getElementById('bt_state').innerHTML="disconnected"
            document.getElementById('bt_state').innerHTML="disconnected"
            document.getElementById('submit').innerHTML = "disconnected"
            document.getElementById('submit').classList.remove("green");
            document.getElementById('submit').classList.add("red");
            
          }
          else{
            document.getElementById('bt_state').innerHTML="connected"
            document.getElementById('submit').innerHTML = "connected"
            document.getElementById('submit').classList.remove("red");
            document.getElementById('submit').classList.add("green");
            
          }
        }
    }
    else{
        alert("Error : Bt_State undefined");
    }
});