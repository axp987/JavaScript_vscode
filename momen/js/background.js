
const images = ["IMG_9430.jpeg", "IMG_R_1019.png", "IMG_R_1020.png"];

const chocenImages = images[Math.floor(Math.random() * images.length)];

const bgImage = document.createElement("img");
bgImage.src = `../image/${chocenImages}`;
document.body.prepend(bgImage);