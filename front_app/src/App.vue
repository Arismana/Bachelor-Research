<template>
  <div id="app">
    <bar v-if="getItem()" @logout="logout"></bar>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>

import bar from './components/bar.vue'
export default {
  name: 'App',
  components: {bar},
  data(){
    return{
      _beforeUnload_time:0,
    }
  },
  mounted(){
    window.addEventListener('beforeunload', e => {
      this._beforeUnload_time = new Date().getTime()
    })
    window.addEventListener('unload', e => {
      let _gap_time = new Date().getTime() - this._beforeUnload_time
      if (_gap_time <= 6) {
        localStorage.removeItem('username')
      }
    })
  },
  methods:{
    getItem(){
      let item = localStorage.getItem('username')
      if(item) return true
      else return false
    }
  }
}
</script>

<style>
*{
   margin: 0;
   padding: 0;
}
#app {
  width: 100%;
  min-height:100vh;
  position: relative;
  background: #233A54;
}
</style>
