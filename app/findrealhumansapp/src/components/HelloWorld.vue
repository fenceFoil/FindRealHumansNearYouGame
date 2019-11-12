<template>
  <div class="hello">
    <img src="../assets/logo-frhny-big.png" style="width:400px; background:#fffa4d;">
    <h1>Create a profile now!!</h1>
    <button v-on:click="createProfile" v-bind:disabled="clickedCreateProfile" class="japanese">始まりましょうか</button>
    <h1>The number 1 rated dating app for real humans.<br/>Just read the reviews of our very real and happy customers.</h1>
    <div v-for="review in reviews" :key="review">
      <p>"{{review}}</p>
    </div>
  </div>
</template>

<script>
import { REST_BASE } from './../constants/constants.js'

export default {
  name: 'HelloWorld',
  props: {
  },
  data: function (){
    return {
      reviews: [], //["The best dating app money can buy 10 out of 10", "didnt find a human, only robots 0 out of 1"],
      gamestate: "Loading...",
      clickedCreateProfile: false
     }
  },
  created: async function() {
    let that = this;
    let i = 0;
    var myint = setInterval(async function() {
      const response2 = await fetch(
        REST_BASE+"/get_review", {
        method: 'GET'
      });
      const reviewText = await response2.text();
      that.reviews.push(reviewText+'"');
      if (++i > 3) {
        clearInterval(myint);
      }
    }, 3200);
  },
  methods: { 
    createProfile: async function() {
      // Announce someone is joining the game.
      // Wait until reply to start game. This will prevent you from joining a dead server.
      // TODO: Test that joining a game-over state server does reset the game and does not 
      // cause you to bounce back to the home screen after seeing the profile screen.
      const resp = await fetch(REST_BASE+"/announce_new_player");
      if (resp.ok) {
        if (resp.text != "ok") {
          this.clickedCreateProfile = true;
          window.localStorage.setItem("iJustStartedGameID", await resp.text())
          setTimeout(() => window.location.href='#/profile', 1500) // Wait for game reset watchdog to fire off before moving to next screen. I give up.
        } else {
          window.location.href='#/profile';
        }
      } else {
        alert("Server-chan is sick today. Her entirely meat-based processing is becoming a liability to us all.")
        this.clickedCreateProfile = false;
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
