document.getElementById("submit").addEventListener('click', async () => {
    const Bt_State = document.getElementById('bt_state').innerHTML;
    if (Bt_State) {
      console.log(Bt_State)
      response = await fetch("/bluetooth/", {
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
            document.getElementById('bt_state').innerHTML="unconnected"
            document.getElementById('submit').innerHTML = "unconnected"
            document.getElementById('submit').style.backgroundColor = "RED"
          }
          else{
            document.getElementById('bt_state').innerHTML="connected"
            document.getElementById('submit').innerHTML = "connected"
            document.getElementById('submit').style.backgroundColor = "GREEN"
          }
        }
    }
    else{
        alert("Error : Bt_State undefined");
    }
});