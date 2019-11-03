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
      submit: function (){
        alert(this.pickupline)
        
        window.location.href='#/swipe'
      }
    }
  }
</script>
