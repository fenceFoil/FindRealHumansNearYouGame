<template>
  <div class="profile">
    <h1>Enter a Name</h1>
      <input v-model="name" type="text" placeholder="Name">
      <button v-on:click="submit" type="button">Submit</button>
  </div>
</template>
<script>
  export default {
    name:'profile',
    components:{},
    methods:{
      submit: function (){
        alert(name)
        window.location.href='#/pickupline'
      }
    }
  }
</script>