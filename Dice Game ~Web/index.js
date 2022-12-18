function randomIntFromInterval(min, max) { // min and max included
  return Math.floor(Math.random() * (max - min + 1) + min);
}

var fdice = randomIntFromInterval(1, 6);
var sdice = randomIntFromInterval(1, 6);

var fdice_src = "images/dice" + String(fdice) + ".png"
var sdice_src = "images/dice" + String(sdice) + ".png"

document.querySelectorAll("div.dice img")[0].src = fdice_src;
document.querySelectorAll("div.dice img")[1].src = sdice_src;

if (fdice > sdice) {
  document.querySelector("div.container h1").textContent = "🚩Player 1 Wins!";
} else if (fdice < sdice) {
  document.querySelector("div.container h1").textContent = "Player 2 Wins! 🚩";
} else {
  document.querySelector("div.container h1").textContent = "Draw!";
}
