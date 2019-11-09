<template>
    <div class="container">
        <div id="hud-displayer" 
        v-on:mouseover="mouseover"
        v-on:mouseleave="mouseleave">Show HUD</div>
        <div id="hud">
            <h1><pre>Game State:<br>{{gamestate}}</pre></h1>
            <!-- add in game info here -->
        </div>
    </div>
</template>

<script>
import { HUD_CONTROL } from './../constants/constants.js';
export default {
    name: 'Hud',
    props: {
    },
    data: function (){
        return {
        }
    },
    methods: {
        mouseover: function(){
            HUD_CONTROL.ON()
        },

        mouseleave: function(){
            HUD_CONTROL.OFF()
        }
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
</style>
