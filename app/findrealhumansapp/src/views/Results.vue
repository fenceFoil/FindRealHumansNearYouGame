<template>
  <div class="results">
    <h1>This is teh result page</h1>
    <button v-on:click="submit">Ready</button>
  </div>
</template>
<script>
  export default {
    name:'pickupline',
    components:{},
    methods:{
      submit: function (){
        window.location.href='#/pickupline'
      }
    }
  }
</script>