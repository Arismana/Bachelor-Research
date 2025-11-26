<template>
    <div class="main">
    </div>
</template>

<script>
export default {
  name: 'main',
  props: {},
  methods:{
    toSomewhere(next){
      if(next == 'login') localStorage.removeItem('username')
      this.$router.push({ name:next})
    }
  }
}
</script>

<style scoped>
.main{
  position: absolute;
  width: 1400px;
  height: 700px;
  right: 20px;
  top: 20px;
  background-color: rgb(105,105,105,.5);
}
</style>