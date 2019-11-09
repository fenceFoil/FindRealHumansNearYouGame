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
    <template v-if="settingPickupLine">
      <h1>Enter pickup line</h1>
      <div class="text">
        <textarea v-model="pickupline" rows="4" cols="50"></textarea>
      </div>
      <div class="button">
        <button v-on:click="submit" type="button">Submit</button>
      </div>
    </template>
    <template v-if="selectingOption">
      <h1>Enhance Your Pickup Line</h1>
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
          settingPickupLine: true,
          selectingOption: false,
          playerName: window.localStorage.getItem("playerName"),
          pictureURL: window.localStorage.getItem("playerPictureURL")
      }
    },
    components:{},
    created: async function() {
        let myint = setInterval(async function() {
          const response2 = await fetch(
            REST_BASE+"/is_it_results_time", {
            method: 'GET'
          });
          const myJson2 = await response2.json();
          if (!myJson2.isItTime) {
            OVERLAY_CONTROL.OFF();
            window.location.href='#/swipe'
            clearInterval(myint);
          }
        }, 1000);
    },
    methods:{
      submit: async function (){
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
            "botScreed":myJson.options[0]
          })
        });
      },
      enhanceLine: async function (ending) {
        alert(ending)
      }
    }
  }
</script>
