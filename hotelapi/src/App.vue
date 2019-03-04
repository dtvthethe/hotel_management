<template>

  <div id="app">
    <p>{{cc}}</p>
  </div>
</template>

<script>
import { areRangesOverlapping } from 'date-fns';

export default {
  name: "app",
  components: {},
  data: function() {
    return {
      a1: new Date("2019/02/03"),
      a2: new Date("2019/02/10"),
      b1: new Date("2019/02/12"),
      b2: new Date("2019/02/23")
    };
  },
  computed:{
    cc : function(){
      return areRangesOverlapping(this.a1,this.a2,this.b1,this.b2);
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
