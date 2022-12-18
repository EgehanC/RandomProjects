var numofbuttons = document.querySelectorAll("button").length;
for (let i = 0; i < numofbuttons; i++) {
  document.querySelectorAll("button")[i].addEventListener("click", function() {
    alert("I got clicked");
  })
}
