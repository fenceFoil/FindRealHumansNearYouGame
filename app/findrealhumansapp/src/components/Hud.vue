<template>
    <div class="container">
        <div id="hud-displayer" 
        v-on:mouseover="mouseover">Show HUD</div>
        <div id="hud">
            <div id="status-bar">
                <h1 id="status-bar-text">{{statusBarText}}</h1>
            </div>
            <h1><pre>Game State:<br>{{gamestate}}</pre></h1>
            <!-- add in game info here -->
        </div>
    </div>
</template>

<script>
import { HUD_CONTROL, OVERLAY_CONTROL, REST_BASE } from './../constants/constants.js';
export default {
    name: 'Hud',
    props: {
    },
    data: function (){
        return {
            statusBarText: "",
            toggle: true
        }
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
                that.statusBarText = serverState.message + " -- " + serverState.countdownSecs;

                // Check for new game
                if (serverState.gameID != currGameID) {
                // Game was reset!
                window.location.href='#/'
                OVERLAY_CONTROL.OFF();
                currGameID = serverState.gameID
                }
            }
        }, 1000);
    },
    methods: {
        mouseover: function(){
            if(this.toggle){
                HUD_CONTROL.ON();
            }else{
                HUD_CONTROL.OFF();
            }
            this.toggle = !this.toggle;
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #hud-displayer {
        position: fixed;
        font-size: 2em;
    }

    #hud {
        position: fixed; /* Sit on top of the page content */
        width: 100%; /* Full width (cover the whole page) */
        height: 100%; /* Full height (cover the whole page) */
        display: none;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0,0,0,0); /* Black background with opacity */
        z-index: -1; /* Specify a stack order in case you're using a different order for other elements */
        cursor: pointer; /* Add a pointer on hover */
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
</style>
