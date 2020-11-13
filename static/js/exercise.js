window.addEventListener("load", (event) => {
  //setting variable
  var exerciseCardBack = document.querySelectorAll(".exerciseCardBack");
  var exerciseCard = document.querySelectorAll(".exerciseCard");
  var numId = qns_count;
  var separator = document.getElementById("separator_" + numId);
  let flipper = document.getElementById("card_" + numId);
  let cardHolder = document.querySelectorAll(".cardHolder");
  let wrong = document.querySelectorAll(".wrong");
  let correct = document.querySelectorAll(".correct");
  var csrftoken = getCookie("csrftoken");
  var name = flipper.getAttribute("name");

  /* Color function */
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
    "F86663",
    "6AC8F0",
    "85E4FE",
    "D6D6FF",
  ];

  function cardHolderColor() {
    rndNum = getRandomInt(colorArray.length);
    let rndColor = "#" + colorArray[rndNum];
    cardHolder[0].style.backgroundColor = rndColor;
  }
  cardHolderColor();

  //loop through it
  for (var i = 0; i < exerciseCardBack.length; i++) {
    rndNum = getRandomInt(colorArray.length);
    let rndColor = "#" + colorArray[rndNum];
    exerciseCardBack[i].style.backgroundColor = rndColor;
    exerciseCard[i].style.backgroundColor = rndColor;
  }
  /* end of color function */

  /* delay function to give time to load the data from model */
  setTimeout(() => {
    cardHolder[0].style.visibility = "visible";
  }, 180);

  /* end of delay function */

  /* Flipper function */
  separator.onclick = () => {
    flip(flipper);
  };

  /* end of flipper function */

  /* swipe left */
  Hammer(cardHolder[0]).on("swipeleft", () => {
    console.log("Left");
    console.log(numId);
    flipper = document.getElementById("card_" + numId);
    separator = document.getElementById("separator_" + numId);
    var name = flipper.getAttribute("name");
    var wrongAnimate = anime({
      targets: document.getElementById("separator_" + numId),
      translateX: "-150%",
      duration: 1500,
    });
    //separator.style.display = "none";
    sendData(URL, "wrong", name, csrftoken);
    nextCard();
    console.log(numId);
    separator.onclick = () => {
      flip(flipper);
    };
  });

  /* swipe right */
  Hammer(cardHolder[0]).on("swiperight", () => {
    console.log("Right");
    flipper = document.getElementById("card_" + numId);
    separator = document.getElementById("separator_" + numId);
    var rightAnimate = anime({
      targets: document.getElementById("separator_" + numId),
      translateX: "150%",
      duration: 1500,
    });
    var name = flipper.getAttribute("name");
    //separator.style.display = "none";
    sendData(URL, "correct", name, csrftoken);
    nextCard();
    separator.onclick = () => {
      flip(flipper);
    };
  });
  /* start of wrong card removal */

  wrong[0].addEventListener("click", () => {
    console.log(numId);
    flipper = document.getElementById("card_" + numId);
    separator = document.getElementById("separator_" + numId);
    var name = flipper.getAttribute("name");
    var wrongAnimate = anime({
      targets: document.getElementById("separator_" + numId),
      translateX: "-150%",
      duration: 1500,
    });
    //separator.style.display = "none";
    sendData(URL, "wrong", name, csrftoken);
    nextCard();
    console.log(numId);
    separator.onclick = () => {
      flip(flipper);
    };
  });

  /* end of wrong card removal */

  /* start of correct card removal */

  correct[0].addEventListener("click", () => {
    flipper = document.getElementById("card_" + numId);
    separator = document.getElementById("separator_" + numId);
    var rightAnimate = anime({
      targets: document.getElementById("separator_" + numId),
      translateX: "150%",
      duration: 1500,
    });
    var name = flipper.getAttribute("name");
    //separator.style.display = "none";
    sendData(URL, "correct", name, csrftoken);
    nextCard();
    separator.onclick = () => {
      flip(flipper);
    };
  });

  /* end of correct card removal */

  /* start of nextCard function */
  // this have to be inside the window.load
  // because it needs to change the numId

  function nextCard() {
    numId--;
    separator = document.getElementById("separator_" + numId);
    flipper = document.getElementById("card_" + numId);
  }

  /* nextCard function end */

  /* get csrfttoken */
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
  //end of get csrfttoken
});

//generate random number

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

//end of random number function

// start of reusable card flip function

function flip(elem) {
  if (elem.style.transform != "rotateY(180deg)") {
    elem.style.transform = "rotateY(180deg)";
  } else if ((elem.style.transform = "rotateY(180deg)")) {
    elem.style.transform = "rotateY(0deg)";
  }
}

// end of reusable cardflip function

// send score to models

function sendData(URL, passOrFail, questionId, csrftoken) {
  data = JSON.stringify({
    info: passOrFail + " " + questionId,
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
}

// end of sendData to models
