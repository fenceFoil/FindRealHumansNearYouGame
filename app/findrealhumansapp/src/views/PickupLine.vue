<template>
  <div class="about">
    <h1 class="header-title">{{playerName}}</h1>
    <h1 class="this-is-you japanese">これはあなたです</h1>
    <div class="left-right">👉</div>
    <div class="left-right-reverse">👉</div>
    <div class="left-to-right">👉</div>
    <div class="picture">
      <img class="waifu" :src="pictureURL">
    </div>
    <h1>Enter pickup line</h1>
    <template v-if="settingPickupLine">
      <div class="text speech-bubble">
        <div class="arrow top right"></div>
        <textarea id="pickupLine-input" v-model="pickupline" rows="4" cols="15" placeholder="Enter a pickupline"></textarea>
      </div>
      <div class="button">
        <button v-on:click="submit" type="button">Submit</button>
      </div>
    </template>
    <template v-if="selectingOption">
      <h1>*Enhance* Your Pickup Line</h1>
      <div v-for="ending in endings" :key="ending" class="text">
        <div class="button">
          <button v-on:click="enhanceLine(ending)" type="button">{{ending}}</button>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
  import { REST_BASE, OVERLAY_CONTROL } from './../constants/constants.js'
  
  export default {
    name:'pickupline',
    data: function (){
        return {
          pickupline: "",
          endings: [],
          settingPickupLine: true,
          selectingOption: false,
          playerName: window.localStorage.getItem("playerName"),
          pictureURL: window.localStorage.getItem("playerPictureURL")
      }
    },
    components:{},
    created: async function() {
        let myint = setInterval(async function() {
          if (JSON.parse(window.localStorage.getItem("gameState")).stage === "SWIPING") {
            OVERLAY_CONTROL.OFF();
            window.location.href='#/swipe'
            clearInterval(myint);
          }
        }, 1000);
    },
    methods:{
      submit: async function (){
        this.settingPickupLine = false;
        this.selectingOption = true;

        const response = await fetch(
          REST_BASE+"/get_pickup_completions", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          body: JSON.stringify({
            "playerID":parseInt(window.localStorage.getItem('playerID')),
            "humanWords":this.pickupline
          })
        });
        const myJson = await response.json();
        this.endings = myJson.options;
      },
      enhanceLine: async function (ending) {
        OVERLAY_CONTROL.ON();

        await fetch(
          REST_BASE+"/commit_new_pickup", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          body: JSON.stringify({
            "playerID":parseInt(window.localStorage.getItem('playerID')),
            "humanWords":this.pickupline,
            "botScreed":ending
          })
        });
      }
    }
  }
</script>

<style scoped>
  .speech-bubble{
    background-color: #f8f8f8;
    border: 2px solid #c8c8c8;
    border-radius: .5em;
    width: 50%;
    text-align: center;
    padding: 20px;
    /* position: absolute; */
    margin-left: 25%;
    margin-top: 1em;
    font-size: 3em;

  }

  .arrow {
    border-style: solid;
    position: absolute;
    border-color: transparent transparent #c8c8c8 transparent;
    border-width: 0em .8em .8em .8em;
    margin-top: -1.25em;
    margin-left: -.4em;
    left: 50%;
  }

  .arrow:after {
    border-color: transparent transparent #f8f8f8 transparent;
    border-style: solid;
    border-width: 0px 1em 1em 1em;
    top: 3px;
    content: "";
    position: absolute;
    left: -1em
  }

  #pickupLine-input{
    resize: vertical;
    font-size: 1em;
    border: none;
    background-color: #f8f8f8;
    outline: none;
    font-family: Glitter;
    overflow: hidden;
    text-align: center
  }
</style>