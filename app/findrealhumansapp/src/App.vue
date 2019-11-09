<template>
<div id="overall" >
  <LoadingOverlay></LoadingOverlay>
  <Hud></Hud>
  <div id="app">
    <router-view/>
  </div>
  </div>
</template>
<script>
import LoadingOverlay from '@/components/LoadingOverlay.vue'
import Hud from '@/components/Hud.vue'

  export default {
    name:'app',
    components:{LoadingOverlay, Hud},
    methods:{
    }
  }
</script>
<style>
#app {
  min-width: 1900px;
  max-width: 1940px;
  margin: auto;
  font-family: Glitter, 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

button, input, textarea{
  font-family: Glitter;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
