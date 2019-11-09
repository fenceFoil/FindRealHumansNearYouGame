<style>
@import './../CSS/motherland.css';
@import './../CSS/animation.css';
</style>
<template>
  <div class="profile">
    <h1 class="header-title">Enter a Name</h1>
    <div class="left-to-right-profile">👉</div>
    <img class="logo anim" src="./../assets/logo-frhny.png">
    <img class="logo anim-1" src="./../assets/logo-frhny.png">
    <img class="logo anim-2" src="./../assets/logo-frhny.png">
    <img class="logo anim-3" src="./../assets/logo-frhny.png">
    <img class="logo anim-4" src="./../assets/logo-frhny.png">
    <form id="profile-name" align="center" method="post" v-on:submit.prevent v-on:submit="submit">
      <input v-model="name" type="text" placeholder="Name" >
      <div class="button">
        <input v-on:click="submit" type="button" value="Submit">
        <!--<input v-on:click="overlay" type="button" value="Overlay On">-->
      </div>

      
    </form>
  </div>
</template>
<script>
  import { REST_BASE, OVERLAY_CONTROL } from './../constants/constants.js';
  export default {
    name:'profile',
    data: function (){
        return {
          name: "",
      }
    },
    components:{},
    created: async function (){
        var myint = setInterval(async function() {
          const response2 = await fetch(
            REST_BASE+"/is_it_results_time", {
            method: 'GET'
          });
          const myJson2 = await response2.json();
          if (myJson2.isItTime) {
            OVERLAY_CONTROL.OFF();
            window.location.href='#/pickupline'
            clearInterval(myint);
          }
      }, 3000);

    },
    methods:{
      submit: async function (){
        OVERLAY_CONTROL.ON();
        var playerPicID = Math.floor(Math.random()*(200000));
        const response = await fetch(
          REST_BASE+"/create_profile", {
            method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          body: JSON.stringify({
            'name': this.name,
            'picture': playerPicID
          })
        });
        const myJson = await response.json();
        window.localStorage.setItem("playerID", myJson.playerID)
        window.localStorage.setItem("playerName", this.name)
        window.localStorage.setItem("playerPictureURL", `https://www.thiswaifudoesnotexist.net/example-${playerPicID}.jpg`)
      }
    }}
</script>