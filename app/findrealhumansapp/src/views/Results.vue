<template>
  <div class="results">
    <h1 class="header-title">{{playerName}}</h1>
    <h1 class="round-num">Round {{round}}</h1>
    <h1>
      <span v-for="n in hearts" :key="n">
        <span style="color: pink;" class="hearts">*</span>
      </span>
    </h1>
    <h1 class="implants">cybernetic implants</h1>
    <div>
      <span style="margin-right: 1em;" v-for="n in implants" :key="n">
        <Implant />
      </span>
    </div>
    <div v-for="pickupline in pickuplines" :key="pickupline">
      <h1 class="seperator">
        <div class="asterisk left">*</div>
        <span class="underscore left">_</span>
        <span class="pipe left">|</span>
        <span class="underscore left">_</span>
        <span class="pipe left">|</span>
        <span class="underscore left">_</span>
        <span class="pipe left">|</span>
        <span class="underscore left">_</span>
        <span class="pipe left">|</span>
        <span class="underscore left">_</span>
        <span class="pipe left">|</span>
        <span class="underscore middle">_</span>
        <span class="pipe right">|</span>
        <span class="underscore right">_</span>
        <span class="pipe right">|</span>
        <span class="underscore right">_</span>
        <span class="pipe right">|</span>
        <span class="underscore right">_</span>
        <span class="pipe right">|</span>
        <span class="underscore right">_</span>
        <span class="pipe right">|</span>
        <span class="underscore right">_</span>
        <div class="asterisk right">*</div>
      </h1>
      <h1 class="robo-pickuplines">{{pickupline}}</h1>
    </div>
    <h1 class="seperator">
      <div class="asterisk left">*</div>
      <span class="underscore left">_</span>
      <span class="pipe left">|</span>
      <span class="underscore left">_</span>
      <span class="pipe left">|</span>
      <span class="underscore left">_</span>
      <span class="pipe left">|</span>
      <span class="underscore left">_</span>
      <span class="pipe left">|</span>
      <span class="underscore left">_</span>
      <span class="pipe left">|</span>
      <span class="underscore middle">_</span>
      <span class="pipe right">|</span>
      <span class="underscore right">_</span>
      <span class="pipe right">|</span>
      <span class="underscore right">_</span>
      <span class="pipe right">|</span>
      <span class="underscore right">_</span>
      <span class="pipe right">|</span>
      <span class="underscore right">_</span>
      <span class="pipe right">|</span>
      <span class="underscore right">_</span>
      <div class="asterisk right">*</div>
    </h1>
    <h1 class="dated">Your lovely Dates</h1>
    <div class="dates-container">
      <img v-for="date in datePics" :key="date" class="waifu-thumbnail" :src="date" />
    </div>
    <template v-if="!gameOver">
      <button v-on:click="submit" class="ready-button">Ready</button>
    </template>
    <template v-if="gameOver">
      <button v-on:click="leaveGame" class="ready-button">Say Goodbye</button>
    </template>
  </div>
</template>
<style>
.results {
  margin-bottom: 6em;
}
.waifu-thumbnail {
  width: 20%;
}
.dates-container {
  overflow-x: auto;
  display: flex;
  flex-direction: row;
}
.ready-button {
  margin-top: 2em;
  font-size: 2em;
}
</style>

<script>
import Implant from "@/components/Implant.vue";
import { REST_BASE } from './../constants/constants.js';
export default {
  name: "pickupline",
  data: function() {
    return {
      playerName: window.localStorage.getItem("playerName"),
      round: 1,
      hearts: 0,
      implants: 0,
      gameOver: false,
      pickuplines: [
        //"Hey I am a Robot. Plz beleive me",
        //"Just a hot single looking to become a hot mess."
      ],
      datePics: [
      ]
    };
  },
  components: { Implant },
  created: async function() {
      // Force player on to swiping again if they timeout their pickup line writing phase looking at their stuff
      // But give the game a couple of seconds to change states and reupload to this page.
      setTimeout(function() {
        let myint = setInterval(async function() {
          if (JSON.parse(window.localStorage.getItem("gameState")).stage === "SWIPING") {
            window.location.href='#/swipe'
            clearInterval(myint);
          }
        }, 1000);
      }, 2000);

      // Meanwhile, immediately continue:
      const response = await fetch(
      REST_BASE+"/results", {
        method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
      body: JSON.stringify({
        playerID: window.localStorage.getItem("playerID")
      })
    });
    const myJson = await response.json();
    this.round = myJson.roundNum;
    this.hearts = myJson.newHearts;
    this.implants = myJson.newImplants;
    this.gameOver = myJson.isFinalResults;
    this.datePics = myJson.youDated.map(x => x.picture)
    this.pickuplines = myJson.youDated.map(x => (x.pickupLine.humanWords + x.pickupLine.botScreed))
  },
  methods: {
    submit: function() {
      window.location.href = "#/pickupline";
    },
    leaveGame: function() {
      window.location.href = "#/";
    }
  }
};
</script>