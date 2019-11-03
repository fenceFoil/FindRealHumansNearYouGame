var ipAddress = "localhost";
var port = "5000";
var statsRoute="scoreboard_stats";
var statsUrlGlobal = "http://localhost:5000/scoreboard_stats";

var mostHeartsListNode;

window.onload = function() {
    mostHeartsListNode = document.getElementById('mostHeartsList');
    loadData();
}

function clearData() {

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
    let responseObject = dataJson.news;
    
    populateMostHearts(responseObject.profiles);
}

function populateMostHearts(profileData) {
    data.sort(function(a,b) {
        return a.hearts - b.hearts;
    });
    
    for (let i = 0; i < data.length; i++) {
        createElementNode(mostHeartsListNode, 'mostHeartsEntry', profileData[i]);
    }
}

function createElementNode(root, nodeName, profile) {
    let parentElement = document.createElement("div");
    parentElement.setAttribute('class', nodeName);
    
    let childImageElement = document.createElement("img");
    childImageElement.setAttribute('class', 'profileImage');
    childImageElement.setAttribute('src', profile.picture);
    
    let childNameElement = document.createTextNode(profile.name);
    childImageElement.setAttribute('class', 'profileName');
    
    parentElement.insertAfter(childImageElement, parentElement.firstChild);
    parentElement.insertAfter(childNameElement, parentElement.firstChild);
    root.insertAfter(parentElement, root.firstChild);
    
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
      console.log(error)
    callback(null);
  });
}