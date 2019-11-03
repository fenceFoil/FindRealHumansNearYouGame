<template>
  <div class="about">
    <h1 class="header-title">Your Name</h1>
    <h1 class="this-is-you japanese">これはあなたです</h1>
    <div class="left-right">👉</div>
    <div class="left-right-reverse">👉</div>
    <div class="left-to-right">👉</div>
    <div class="picture">
      <img class="waifu" src="https://www.thiswaifudoesnotexist.net/example-196646.jpg">
    </div>
    <h1>Enhance Your Pickup Line</h1>
    <div v-for="ending in endings" :key="ending" class="text">
      <div class="button">
        <button v-on:click="submit(ending)" type="button">{{ending}}</button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name:'selectline',
    data: function (){
        return {
          pickupline: "",
          endings: ["Ending 1","Ending 2"]
      }
    },
    components:{},
    methods:{
      submit: function (ending){
        alert(ending)
        window.location.href='#/swipe'
      }
    }
  }
</script>
