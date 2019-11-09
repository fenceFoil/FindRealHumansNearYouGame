<template>
  <div class="about">
    <h1 class="header-title">{{prospects[index].name}}</h1>
    <h1 class="this-is-not-you japanese">これはあなたじゃないです</h1>
    <div class="picture">
      <img class="waifu" :src="prospects[index].picture" />
    </div>
    <h1>{{prospects[index].pickupLine.humanWords + prospects[index].pickupLine.botScreed}}</h1>
    <button class="button-2 japanese" v-on:click="submit('RIGHT')" type="submit">右</button>
    <button class="button-1 japanese" v-on:click="submit('LEFT')" type="submit">左</button>
  </div>
</template>
<script>

import { REST_BASE } from "./../constants/constants.js";
export default {
  name: "swipe",
  data: function() {
    return {
      index: 0,
      prospects: []
    };
  },
  components: {},
  created: async function() {
    // Set timer to move to results stage if we've moved on
    let myint = setInterval(async function() {
      const response2 = await fetch(
        REST_BASE+"/is_it_results_time", {
        method: 'GET'
      });
      const myJson2 = await response2.json();
      if (myJson2.isItTime) {
        window.location.href='#/results'
        clearInterval(myint);
      }
    }, 1000);

    // Load prospects when entering this stage
    const response = await fetch(
      REST_BASE + "/get_prospects/" +
        window.localStorage.getItem("playerID"),
      {
        method: "GET"
      }
    );
    const myJson = await response.json();
    this.prospects = myJson.prospects;
  },
  methods: {
    submit: async function(direction) {
      await fetch(REST_BASE + "/swipes", {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8"
        },
        body: JSON.stringify({
          playerID: window.localStorage.getItem("playerID"),
          targetID: this.prospects[this.index].playerID,
          action: direction
        })
      });
      if (this.index < this.prospects.length - 1) {
        this.index++;
      } else {
        window.location.href = "#/results";
      }
    }
  }
};
</script>
