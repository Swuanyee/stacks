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



function deleteDeck(clicked_id) {
  console.log(clicked_id);
	var csrftoken = getCookie("csrftoken");
  data = JSON.stringify({
    info: clicked_id 
  });
  fetch(URL, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      Accept: "application/json",
      "X-Requested-With": "XHMLHttpREquest",
      "X-CSRFToken": csrftoken,
    },
    body: data,
  })
    .then((response) => {
      console.log(response.status);
      return response;
    })
    .catch((error) => {
      console.log(error);
    });
	location=location;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    console.log(cookieValue);
    return cookieValue;
  }
