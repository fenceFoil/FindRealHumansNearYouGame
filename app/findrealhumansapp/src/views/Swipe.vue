<template>
  <div class="about">
    <h1 class="header-title">{{prospects[index].name}}</h1>
    <h1 class="this-is-not-you japanese">これはあなたじゃないです</h1>
    <div class="picture">
      <img class="waifu" :src="prospects[index].picture">
    </div>
    <h1>{{prospects[index].pickupLine.humanWords + prospects[index].pickupLine.botScreed}}</h1>
    <button class="button-2 japanese" v-on:click="submit('RIGHT')" type="submit">右</button>
    <button class="button-1 japanese" v-on:click="submit('LEFT')" type="submit">左</button>
  </div>
</template>
<script>
  export default {
    name:'swipe',
    data: function (){
      return {
        index: 0,
        prospects: []
      }
    },
    components:{},
    created: async function() {
      var url = 'http://findrealhumansnearyou.com/';
      const response = await fetch(
        url+"get_prospects/"+window.localStorage.getItem('playerID'), {
        method: 'GET'
      });
      const myJson = await response.json();
      this.prospects = myJson.prospects
    },
    methods:{
      submit: async function (direction){
        var url = 'http://findrealhumansnearyou.com/swipes';
          await fetch(
          url+"", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          body: JSON.stringify({
            "playerID": window.localStorage.getItem('playerID'),
            "targetID": this.prospects[this.index].playerID,
            "action": direction
          })
        });
        if(this.index < this.prospects.length-1){
          this.index++
        }else{
          window.location.href='#/results'
        }
      }
    }
  }


</script>
