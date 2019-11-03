<template>
  <div class="about">
    <h1>Your Name</h1>
    <div class="picture">
      <img src="https://www.thiswaifudoesnotexist.net/example-196646.jpg">
    </div>
    <h1>Enter pickup line</h1>
    <textarea rows="4" cols="50"></textarea>
    <button v-on:click="submit" type="button">Submit</button>
  </div>
</template>

<script>
  export default {
    name:'pickupline',
    components:{},
    methods:{
      submit: function (){
        window.location.href='#/swipe'
      }
    }
  }
</script>
