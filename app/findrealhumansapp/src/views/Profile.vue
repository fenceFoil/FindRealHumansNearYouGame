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
    <form id="profile-name" align="center" method="post">
      <input v-model="name" type="text" placeholder="Name">
      <div class="button"><input v-on:click="submit" type="button" value="Submit"></div>
      </form>
  </div>
</template>
<script>
  export default {
    name:'profile',
    data: function (){
        return {
          name: "",
      }
    },
    components:{},
    methods:{
      submit: function (){
        alert(this.name)
        window.location.href='#/pickupline'
      }
    }
  }
</script>