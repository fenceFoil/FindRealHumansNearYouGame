<template>
  <div class="home">
    <img src="../assets/logo-frhny.png" style="width:400px; background:#fffa4d;">
    <HelloWorld/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  }
}
</script>

<style>

</style>