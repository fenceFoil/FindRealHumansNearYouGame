<template>
  <div class="about">
    <h1>{{prospects[index].name}}</h1>
    <div class="picture">
      <img :src="prospects[index].src">
    </div>
    <h1>{{prospects[index].line}}</h1>
    <button v-on:click="submit('LEFT')" type="submit">LEFT</button>
    <button v-on:click="submit('RIGHT')" type="submit">RIGHT</button>
  </div>
</template>
<script>
  export default {
    name:'swipe',
    data: function (){
      return {
        index: 0,
        prospects: [{name: "Name 1", src:"https://www.thiswaifudoesnotexist.net/example-196646.jpg", line: "Pickup Line 1"},
                    {name: "Name 2", src:"https://www.thiswaifudoesnotexist.net/example-196647.jpg", line: "Pickup Line 2"}],
      }
    },
    components:{},
    methods:{
      submit: function (direction){
        alert(direction)
        if(this.index < this.prospects.length-1){
          this.index++
        }else{
          window.location.href='#/results'
        }
      }
    }
  }
</script>