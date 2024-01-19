//import axios from 'axios';

const URL = 'https://macvendors.co/api/';

async function checkMac(){
    const input = document.getElementById("macAddr");
    const mac = input.value;
    console.log("Mac consultado: " + mac);
    const info = await axios.get(URL + mac);
    console.log(info);
    input.value = "";
}


let checkBtn = document.getElementById('searchMac');
checkBtn.addEventListener('click', checkMac);