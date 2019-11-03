var ipAddress = "localhost";
var port = "5000";
var statsRoute="scoreboard_stats";
var statsUrlGlobal = "http://ec2-18-221-77-224.us-east-2.compute.amazonaws.com:443/scoreboard_stats";

var mostHeartsListNode;
var mostImplantsListNode;
var bestPickupLinesListNode;

window.onload = function() {
    initElements();
    loadData();
    
    const interval = setInterval(function() {
        clearData();
        loadData();
    }, 10000);
}

function initElements() {
    mostHeartsListNode = document.getElementById('mostHeartsList');
    mostImplantsListNode = document.getElementById('mostImplantsList');
    bestPickupLinesListNode = document.getElementById('bestPickupLinesList');
}

function clearData() {
    while (mostHeartsListNode.firstChild) {
        mostHeartsListNode.removeChild(mostHeartsListNode.firstChild);
    }
    while (mostImplantsListNode.firstChild) {
        mostImplantsListNode.removeChild(mostImplantsListNode.firstChild);
    }
    while (bestPickupLinesListNode.firstChild) {
        bestPickupLinesListNode.removeChild(bestPickupLinesListNode.firstChild);
    }
}

function loadData() {
    clearData();
    makeGetRequest2(statsUrlGlobal, loadDataCallback);
}

function loadDataCallback(dataJson) {
    if (dataJson === null)
    {
      console.log('Error retrieving latest data');
      return;
    }
    let profiles = dataJson.profiles;
    let pickupLines = dataJson.pickupLines;
    let likes = dataJson.likes;
    console.log("ALL_Likes");
    console.log(likes);
    populateMostHearts(profiles);
    populateMostImplants(profiles);
    populateBestPickupLines(profiles, pickupLines, likes);
}

function populateMostHearts(profileData) {
    profileData.sort(function(a,b) {
        return a.hearts - b.hearts;
    });
    
    for (let i = 0; i < profileData.length; i++) {
        createElementNode(mostHeartsListNode, 'mostHeartsEntry', profileData[i], null);
    }
}

function populateMostImplants(profileData) {
    profileData.sort(function(a,b) {
        return a.implants - b.implants;
    });
    
    for (let i = 0; i < profileData.length; i++) {
        createElementNode(mostImplantsListNode, 'mostImplantsEntry', profileData[i], null);
    }
}

function populateBestPickupLines(profiles, pickupLines, likes) {
    //{profile, roundNum, numberOfLikes, pickupLine
    
    let combinedResults = [];
    // For every profile
    for(let i = 0; i < profiles.length; i++){
        // Go through every round and found out the like count for the pickup line in each
        let curResultsProfile = [null, null, null, null, null, null];// {profile: profiles[i], roundNum: roundNum, numberOfLikes: 0, line: ""};
        for (roundNum = 1; roundNum <= 5; roundNum++) {
            // GO through the likes for the round
            for(let likeIndex = 0; likeIndex < likes.length; likeIndex++) {
                // If this is a like for us and is new
                let likeValue = likes[likeIndex];
                if(likeValue.action == "RIGHT" && !curResultsProfile[likeValue.roundNum] && likeValue.roundNum == roundNum && likeValue.destPlayerID == profiles[i].playerID) {
                    // Find the like's pickup line
                    let line = "";
                    for(let lineIndex = 0; lineIndex < pickupLines.length; lineIndex++){
                        let pickupLine = pickupLines[lineIndex];
                        if(pickupLine.playerID == likeValue.destPlayerID && pickupLine.roundNum == roundNum) {
                            console.log("FOund a LLING");
                            line = pickupLine.humanWords + pickupLine.botScreed;
                        }
                    }
                    // Add the new entry
                    curResultsProfile[likeValue.roundNum] = {profile: profiles[i], roundNum: roundNum, numberOfLikes: 1, pickupLine: line};
                }
                else if(likeValue.action == "RIGHT" && likeValue.roundNum == roundNum && likeValue.destPlayerID == profiles[i].playerID) {
                    // If the like is ours and is not new
                    // Add it to the likes count
                    curResultsProfile[likeValue.roundNum].numberOfLikes = curResultsProfile[likeValue.roundNum].numberOfLikes + 1;
                }
            }
        }
        // Combine every pickup line stuff for the profile
        for(let curProf = 0; curProf < curResultsProfile.length; curProf++) {
            if(curResultsProfile[curProf] != null) {
                combinedResults.push(curResultsProfile[curProf]);
            }
        }
    }
    // Sort
    combinedResults.sort(function(a,b) {
        return a.numberOfLikes - b.numberOfLikes;
    });
    
    // FInally add them to the UI
    for (let i = 0; i < combinedResults.length; i++) {
        createElementNodePickupLines(bestPickupLinesListNode, 'bestPickupLinesEntry', combinedResults[i]);
    }
}

function createElementNode(root, nodeName, profile, extraValue) {
    let parentElement = document.createElement("div");
    parentElement.setAttribute('class', nodeName);
    
    let childImageElement = document.createElement("img");
    childImageElement.setAttribute('class', 'profileImage');
    childImageElement.setAttribute('src', profile.picture);
    
    let childNameElement = document.createTextNode(profile.name);
    //childImageElement.setAttribute('class', 'profileName');
    
    let extraValueNameElement;
    if(extraValue != null) {
        extraValueNameElement = document.createTextNode(extraValue);
        extraValueNameElement.setAttribute('class', 'extraValue');
    }
    
    parentElement.appendChild(childImageElement);
    parentElement.appendChild(childNameElement);
    if(extraValue != null) {
        parentElement.appendChild(extraValueNameElement);
    }
    root.appendChild(parentElement);
    
}

function createElementNodePickupLines(root, nodeName, pickupLine) {
    console.log("UI WORK");
    console.log(pickupLine);
    let parentElement = document.createElement("div");
    parentElement.setAttribute('class', nodeName);
    
    let childImageElement = document.createElement("img");
    childImageElement.setAttribute('class', 'profileImage');
    childImageElement.setAttribute('src', pickupLine.profile.picture);
    
    let childNameElement = document.createTextNode(pickupLine.profile.name);
    //childNameElement.setAttribute('class', 'profileName');
    
    let childLikesElement = document.createTextNode("Likes: " + pickupLine.numberOfLikes);
    //childLikesElement.setAttribute('class', 'numberOfLikes');
    
    let childLineElement = document.createTextNode(pickupLine.pickupLine);
    //childLineElement.setAttribute('class', 'pickupLine');
    
    
    parentElement.appendChild(childImageElement);
    parentElement.appendChild(childNameElement);
    parentElement.appendChild(childLikesElement);
    parentElement.appendChild(childLineElement);
    
    root.appendChild(parentElement);
    
}

function makeGetRequest(route, parameters, callback)
{
  let url = new URL(ipAddress + ":" + port + "/" + route);
  url.search = new URLSearchParams(parameters);
  console.log(url);
  fetch(url)
  .then((resp) => resp.json())
  .then(function (data) {
      callback(data);
  })
  .catch((error) => {
      console.log(error)
    callback(null);
  });
}

function makeGetRequest2(urlString, callback)
{
  let url = new URL(urlString);
  console.log(url);
  fetch(url)
  .then((resp) => resp.json())
  .then(function (data) {
      callback(data);
  })
  .catch((error) => {
      console.log(error);
    callback(null);
  });
}