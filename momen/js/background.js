
const images = ["IMG_94301.jpeg", "IMG_R_10191.png", "IMG_R_10201.png"];

const chocenImages = images[Math.floor(Math.random() * images.length)];

const bgImage = document.createElement("img");
bgImage.src = `../image/${chocenImages}`;
document.body.prepend(bgImage);