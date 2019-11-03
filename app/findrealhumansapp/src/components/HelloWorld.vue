<template>
  <div class="hello">
    <h1>Create a profile now!!</h1>
    <button onclick="window.location.href = '#/profile';" class="japanese">始まりましょうか</button>
    <h1>The number 1 rated dating app for real humans.<br/>Just read the reviews of our very real and happy customers.</h1>
    <div v-for="review in reviews" :key="review">
      <p>{{review}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
  },
  data: function (){
    return {
      reviews: ["The best dating app money can buy 10 out of 10", "didnt find a human, only robots 0 out of 1"]
     }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
