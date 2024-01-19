const URL = 'https://macvendors.co/api/';

function checkMac(){
    const input = document.getElementById("macAddr");
    const mac = input.value;
    console.log("Mac consultado: " + mac);
    input.value = "";
}


let checkBtn = document.getElementById('searchMac');
checkBtn.addEventListener('click', checkMac);