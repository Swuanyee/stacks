window.addEventListener("load", (event) => {
  //generate random number
  function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
  }
  //array of colors to select from
  var colorArray = [
    "79ADDC",
    "FFC09F",
    "FFEE93",
    "FCF5C7",
    "ADF7B6",
    "00A878",
    "D8F1A0",
    "F3C178",
    "885053",
    "9590A8",
  ];
  //creat an array with the class of deckCards
  var deckCards = document.querySelectorAll(".deckCards");
  //loop through it
  for (var i = 0; i < deckCards.length; i++) {
    rndNum = getRandomInt(colorArray.length);
    let rndColor = "#" + colorArray[rndNum];
    deckCards[i].style.backgroundColor = rndColor;
  }
});
