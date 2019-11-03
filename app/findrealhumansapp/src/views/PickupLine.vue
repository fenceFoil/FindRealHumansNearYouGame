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
