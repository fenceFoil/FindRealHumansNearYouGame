<template>
  <div class="about">
    <h1 class="header-title">{{prospects[index].name}} (?)</h1>
    <h1 class="this-is-not-you japanese">これはあなたじゃないです</h1>
    <div class="picture">
      <img class="waifu" :src="prospects[index].picture" />
    </div>
    <div class="speech-bubble">
      <div class="arrow top right"></div>
      {{prospects[index].pickupLine.humanWords + prospects[index].pickupLine.botScreed}}
    </div>
    <button class="button-2 japanese" v-on:click="submit('RIGHT')" type="submit">右 💕</button>
    <button class="button-1 japanese" v-on:click="submit('LEFT')" type="submit">左</button>
  </div>
</template>
<script>
//{{prospects[index].name}}
//prospects[index].picture
//{{prospects[index].pickupLine.humanWords + prospects[index].pickupLine.botScreed}}
import { REST_BASE } from "./../constants/constants.js";
export default {
  name: "swipe",
  data: function() {
    return {
      index: 0,
      prospects: [],
      pictureURL: window.localStorage.getItem("playerPictureURL")
    };
  },
  components: {},
  created: async function() {
    // Set timer to move to results stage if we've moved on
    let myint = setInterval(async function() {
      if (JSON.parse(window.localStorage.getItem("gameState")).stage === "WRITING_PICKUPS") {
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
        // Announce we have finished swiping
        await fetch(REST_BASE + "/finished_swiping", {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8"
          },
          body: JSON.stringify({
            playerID: window.localStorage.getItem("playerID")
          })
        });
        // Move to results page
        window.location.href = "#/results";
      }
    }
  }
};
</script>

<style>
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
</style>