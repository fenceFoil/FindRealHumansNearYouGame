<template>
  <div id="overall">
    <LoadingOverlay></LoadingOverlay>
    <Hud></Hud>
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
import LoadingOverlay from '@/components/LoadingOverlay.vue'
import Hud from '@/components/Hud.vue'
import { REST_BASE } from "./constants/constants.js";

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

button, input, textarea{
  font-family: Glitter;
}

</style>
