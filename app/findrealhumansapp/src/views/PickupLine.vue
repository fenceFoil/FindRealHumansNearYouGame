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
    <div class="text">
    <textarea v-model="pickupline" rows="4" cols="50"></textarea>
    </div>
    <div class="button">
    <button v-on:click="submit" type="button">Submit</button>
    </div>
  </div>
</template>

<script>
  export default {
    name:'pickupline',
    data: function (){
        return {
          pickupline: "",
          playerName: window.localStorage.getItem("playerName"),
          pictureURL: window.localStorage.getItem("playerPictureURL")
      }
    },
    components:{},
    methods:{
      submit: async function (){
        var url = 'http://findrealhumansnearyou.com/';
        const response = await fetch(
          url+"get_pickup_completions", {
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
        alert(myJson.options[0])

        await fetch(
          url+"commit_new_pickup", {
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
          var url2 = 'http://findrealhumansnearyou.com/';
          const response2 = await fetch(
            url2+"is_it_results_time", {
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
