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
          <button v-on:click="submit(ending)" type="button">{{ending}}</button>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
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
    methods:{
      submit: async function (){
        const response = await fetch(
          "/get_pickup_completions", {
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

        alert("The other waifus are preparing...")

        await fetch(
          "/commit_new_pickup", {
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

        var myint = setInterval(async function() {
          const response2 = await fetch(
            "/is_it_results_time", {
            method: 'GET'
          });
          const myJson2 = await response2.json();
          if (!myJson2.isItTime) {
            window.location.href='#/swipe'
            clearInterval(myint);
          }
        }, 1000);

      }
    }
  }
</script>
