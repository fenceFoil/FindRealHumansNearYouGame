<template>
  <div id="overall">
    <LoadingOverlay></LoadingOverlay>
    <Hud></Hud>
    <div id="background"></div>
    <div id="vertical-app-layout">
      <div id="app">
        <router-view />
      </div>
    </div>
  </div>
</template>
<script>
import LoadingOverlay from '@/components/LoadingOverlay.vue'
import Hud from '@/components/Hud.vue'
import { REST_BASE, OVERLAY_CONTROL } from "./constants/constants.js";

export default {
  name: "App",
  components:{LoadingOverlay, Hud},
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

        // Save state for rest of app
        window.localStorage.setItem('gameState', JSON.stringify(serverState))

        // Respond to new server state

        // Update status bar message
        that.statusBarText = serverState.message + " -- " + serverState.countdownSecs;

        // Check for new game
        if (serverState.gameID != currGameID) {
          // Game was reset!
          if (window.localStorage.getItem("iJustStartedGameID") != currGameID) {
            // When the user has clicked "create profile" during game over, the game will reset itself.
            // But since the player has already started creating their profile, let them keep going.
            window.location.href='#/'
          }
          OVERLAY_CONTROL.OFF();
          currGameID = serverState.gameID
        }
      }
    }, 1000);
  }
};
</script>

<style>
body {
  margin: 2em;
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

#background {
    position: fixed; /* Sit on top of the page content */
    width: 100%; /* Full width (cover the whole page) */
    height: 100%; /* Full height (cover the whole page) */
    display: block;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0,0,0,0); /* Black background with opacity */
    z-index: -2;  /* Specify a stack order in case you're using a different order for other elements */
    cursor: pointer; /* Add a pointer on hover */
}

button, input, textarea{
  font-family: Glitter;
  font-size: 2em;
}

</style>
