
$(document).ready(function () {
  
  // Load existing cards from localStorage on page load
  loadExistingCards();

  function loadExistingCards() {
    const existingCards = localStorage.getItem('cards');
    if (existingCards) {
      $('#card-container').html(existingCards);
    }
  }

  function updateCards() {
    $.ajax({
      url: '/get_latest_images',
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        // Append new cards to the existing ones
        for (let i = 0; i < data.length; i++) {
          let cardHtml = `<div class="card">
                                        <img src="/static/images/${data[i].imageName}" alt="Vandalism Image" onload="saveCardsToLocalStorage()">
                                        <h3>Vandalism Deteced</h3>
                                        <p>Camera: ${data[i].cameraName}</p>
                                        <p>Timestamp: 19th December 2023 (1 hour ago) </p>
                                        <button class="fine-button" onclick="poseFine(${i})">Pose a Fine</button>
                                    </div>`;
          $('#card-container').append(cardHtml);
        }
        saveCardsToLocalStorage();

        removeOlderCards();
      },
    });
  }

  function saveCardsToLocalStorage() {
    const updatedCards = $('#card-container').html();
    localStorage.setItem('cards', updatedCards);
  }

  function removeOlderCards() {
    const maxCardsToShow = 10; // Adjust as needed
    const $cards = $('#card-container').children('.card');

    if ($cards.length > maxCardsToShow) {
      $cards.slice(0, $cards.length - maxCardsToShow).remove();
      saveCardsToLocalStorage(); // Save the updated cards after removal
    }
  }

  // Periodically update cards every 5 seconds (adjust as needed)
  setInterval(updateCards, 5000);
});

function poseFine(data) {
  var modal = document.getElementById("myModal");
  modal.style.display = "block";
  var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
  modal.style.display = "none";
}
}

let currentAmount = 5000; // Initial amount

// Function to update the amount and display it
function updateAmount() {
  document.getElementById('estimated-amount').innerText = currentAmount;
}

// Function to change the amount based on the provided operation
function changeAmount(operation) {
  if (operation === '+') {
    currentAmount += 100;
  } else if (operation === '-' && currentAmount >= 100) {
    currentAmount -= 100;
  }

  updateAmount(); // Update the displayed amount
}

function whatsapp() {
  const url = 'https://graph.facebook.com/v17.0/189062327616427/messages';
  const accessToken = 'EAATdygZB3UwQBOZBxDv0ZA2G5dLByZC5pQkfWVFVskwhU3GTMQDOQgquH03jZC9ix8zO3lUwgNsJEld0PDUrvZBHm1b3jDPweVD5NyxEXWbAMAt8vR4ZBNZBZA6EA6opPgUYZBalWiytWPGqlFR2D0nfKSecPjWWTTr39fbbXBQgpCDMcORGgUOiFvzUweFEb8TOh1jFUKjVPlikwf9wT20w8ZD'; // Replace with your actual access token

  const headers = {
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/json',
  };
  const data = {
    "messaging_product": "whatsapp",
    "to": "917266040123",
    "type": "template",
    "template": {
      "name": "fine_imposed_sih",
      "language": {
        "code": "en_US",
      },
      "components": [
        {
          "type": "body",
          "parameters": [
            {
              "type": "text",
              "text": "Shaurya"
            },
            {
              "type": "text",
              "text": "vandalism"
            },
            {
              "type": "text",
              "text": "Golkunda Fort"
            },
            {
              "type": "text",
              "text": "23rd December, 2023"
            },
            {
              "type": "text",
              "text": "5000"
            },
            {
              "type": "text",
              "text": "E1234567"
            },
          ]
        }
      ]
    }
  };

//Whatsapp yaha se ho rha h 
  $.ajax({
    url: url,
    type: 'POST',
    headers: headers,
    contentType: 'application/json',
    data: JSON.stringify(data),
    success: function(response) {
      console.log('Response:', response);
      alert("Fine Imposed and User informed via WhatsApp & Message")
    },
    error: function(error) {
      console.error('Error:', error.responseJSON);
      alert(error.responseJSON)
    },
  });
  //SMS yaha se ja rha h
  $.ajax({
    url: 'https://api.twilio.com/2010-04-01/Accounts/AC6ab9b90e28b8e83d0530f9f7282adf2d/Messages.json',
    type: 'POST',
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Authorization", "Basic " + btoa("AC6ab9b90e28b8e83d0530f9f7282adf2d:ebeda0e21381ccdeb17510fdd884fae6"));
    },
    data: {
      To: '+918586011672',
      From: '+12058807420',
      Body: 'Dear Shaurya,  You have been fined for Rs '+currentAmount+' for the violation of Vandalism at Golkunda Fort on 23rd December If you think this is a mistake, please contact us at +91 00000 0000  Your E-Challan ID is: E1234567'
    },
    success: function(response) {
      console.log(response);
      // Handle the success response here
    },
    error: function(xhr, status, error) {
      console.error(error);
      // Handle the error response here
    }
  });
  
}