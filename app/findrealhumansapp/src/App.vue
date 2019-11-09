<template>
  <div id="overall">
    <div id="overlay">
      <h1 id="overlay-text">*Girls Are Preparing . . .*</h1>
    </div>
    <div id="vertical-app-layout">
      <div id="status-bar">
        <h1 id="status-bar-text">{{statusBarText}}</h1>
      </div>
      <div id="app">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import { REST_BASE } from "./constants/constants.js";

export default {
  name: "App",
  data: function() {
    return {
      statusBarText: ""
    };
  },
  created: async function() {
    let that = this;
    let currGameID = 0;

    // Continuously poll the server for the current game state
    setInterval(async function() {
      const response3 = await fetch(REST_BASE + "/game_state", {
        method: "GET"
      });
      if (response3.status != 200) {
        this.statusBarText =
          "Cannot reach game" + (REST_BASE != "")
            ? " at " + REST_BASE
            : " on same server as this page";
      } else {
        let serverState = await response3.json();

        // Respond to new server state

        // Update status bar message
        that.statusBarText = serverState.message + " -- " + serverState.stateTimeoutTime;

        // Check for new game
        if (serverState.currGameID != currGameID) {
          // Game was reset!
          window.location.href='#/'
          currGameID = serverState.currGameID
        }
      }
    }, 1000);
  }
};
</script>

<style>
body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

* {
  box-sizing: inherit;
}

#app {
  min-width: 1900px;
  max-width: 1940px;
  margin: auto;
  font-family: Glitter, "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  overflow-x: hidden;
}

#status-bar {
  background-color: #a55fc1;
  z-index: 3;
  text-align: center;
}

#status-bar-text {
  font-family: Crayon, Helvatica, Arial, sans-serif;
  margin: 0;
  padding: 0.1em;
  margin-bottom: 0.3em;
  font-size: 1.8em;
  color: #1a232c;
}

#overlay {
  position: fixed; /* Sit on top of the page content */
  width: 100%; /* Full width (cover the whole page) */
  height: 100%; /* Full height (cover the whole page) */
  display: none;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.9); /* Black background with opacity */
  z-index: 2; /* Specify a stack order in case you're using a different order for other elements */
  cursor: pointer; /* Add a pointer on hover */
}

#overlay-text {
  position: absolute;
  top: 50%;
  left: 50%;
  font-size: 10em;
  margin-top: -1em;
  margin-left: -5em;
  color: pink;
}

button,
input,
textarea {
  font-family: Glitter;
}

</style>
