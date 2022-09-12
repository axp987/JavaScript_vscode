const API_KEY = "a70525b0ab3bc598232754063d83d836";

function OneGeoOk(position) {
    const lat = position.coords.latitude;
    const long = position.coords.longitude;
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${position.coords.latitude}&lon=${position.coords.longitude}&appid=${API_KEY}&units=metric`;
    fetch(url).then(response => response.json()).then(data => {
        const name = data.name;
        const wea = data.weather[0].main;
        
        const city_name = document.querySelector("#weather span:first-child");
        const city_wea = document.querySelector("#weather span:last-child");
        city_name.innerText=`도시: ${name}`;
        city_wea.innerText=`날씨: ${wea}`;
        
    });
    
}

function onGeoError() {
    alert("cna't find you, No wheater for you");
}

navigator.geolocation.getCurrentPosition(OneGeoOk, onGeoError);
