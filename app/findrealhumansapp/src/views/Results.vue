<template>
  <div class="results">
    <h1 class="header-title">{{playerName}}</h1>
    <h1 class="round-num">Round {{round}}</h1>
    <h1>
    <span v-for="n in hearts" :key="n">
      <span style="color: pink;" class="hearts">* </span>
    </span>
    </h1>
    <h1 class="implants">cybernetic implants</h1>
    <div>
    <span style="margin-right: 1em;" v-for="n in implants" :key="n">
      <Implant/>
    </span>
    </div>    
    <div v-for="pickupline in pickuplines" :key="pickupline">
    <h1 class="seperator"><div class="asterisk left">*</div><span class="underscore left">_</span><span class="pipe left">|</span><span class="underscore left">_</span><span class="pipe left">|</span><span class="underscore left">_</span><span class="pipe left">|</span><span class="underscore left">_</span><span class="pipe left">|</span><span class="underscore left">_</span><span class="pipe left">|</span><span class="underscore middle">_</span><span class="pipe right">|</span><span class="underscore right">_</span><span class="pipe right">|</span><span class="underscore right">_</span><span class="pipe right">|</span><span class="underscore right">_</span><span class="pipe right">|</span><span class="underscore right">_</span><span class="pipe right">|</span><span class="underscore right">_</span><div class="asterisk right">*</div></h1>
      <h1 class="robo-pickuplines">{{pickupline}}</h1>
    </div>
    <h1 class="seperator"><div class="asterisk left">*</div><span class="underscore left">_</span><span class="pipe left">|</span><span class="underscore left">_</span><span class="pipe left">|</span><span class="underscore left">_</span><span class="pipe left">|</span><span class="underscore left">_</span><span class="pipe left">|</span><span class="underscore left">_</span><span class="pipe left">|</span><span class="underscore middle">_</span><span class="pipe right">|</span><span class="underscore right">_</span><span class="pipe right">|</span><span class="underscore right">_</span><span class="pipe right">|</span><span class="underscore right">_</span><span class="pipe right">|</span><span class="underscore right">_</span><span class="pipe right">|</span><span class="underscore right">_</span><div class="asterisk right">*</div></h1>
    <h1 class="dated">Your lovely Dates</h1>
    <div class="dates-container">
      <img v-for="date in dates" :key="date" class="waifu-thumbnail" :src="date">
    </div>
    <button v-on:click="submit">Ready</button>
  </div>
</template>
<style>
  .waifu-thumbnail{
    width: 20%;
  }
  .dates-container{
    overflow-x: auto;
    display: flex;
    flex-direction: row;
  }
</style>

<script>
import Implant from '@/components/Implant.vue'
  export default {
    name:'pickupline',
    data: function (){
        return {
          playerName: window.localStorage.getItem("playerName"),
          round: 1,
          hearts: 4,
          implants: 2,
          pickuplines: ["Hey I am a Robot. Plz beleive me","Just a hot single looking to become a hot mess."],
          dates: ["https://www.thiswaifudoesnotexist.net/example-196646.jpg", "https://www.thiswaifudoesnotexist.net/example-196647.jpg", "https://www.thiswaifudoesnotexist.net/example-196647.jpg", "https://www.thiswaifudoesnotexist.net/example-196647.jpg", "https://www.thiswaifudoesnotexist.net/example-196647.jpg", "https://www.thiswaifudoesnotexist.net/example-196647.jpg", "https://www.thiswaifudoesnotexist.net/example-196647.jpg", "https://www.thiswaifudoesnotexist.net/example-196647.jpg", "https://www.thiswaifudoesnotexist.net/example-196627.jpg", "https://www.thiswaifudoesnotexist.net/example-112647.jpg", "https://www.thiswaifudoesnotexist.net/example-106647.jpg", "https://www.thiswaifudoesnotexist.net/example-192647.jpg"],
      }
    },
    components:{Implant},
    methods:{
      submit: function (){
        window.location.href='#/pickupline'
      }
    }
  }
</script>