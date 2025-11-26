<template>
  <div id="loading">
    <div style="color: rgb(255, 255, 255,.8);font-size: 24px; font-weight: bold;margin-bottom: 30px; margin-left: -50px;">数据分析中</div>
    <div class="loading"></div>
  </div>
</template>

<script>
export default {
  name: 'loading',
}
</script>

<style scoped>
#loading{
  width: 200px;
  height: 200px;
}
.loading {
  display: block;
  position: relative;
  width: 12px;
  height: 20px;
  animation: rectangle infinite 1s ease-in-out -0.2s;
  background-color: rgb(255, 255, 255,.8);
}

.loading:before,
.loading:after {
  position: absolute;
  width: 12px;
  height: 20px;
  content: "";
  background-color: rgb(255, 255, 255,.8);
}

.loading:before {
  left: -28px;
  animation: rectangle infinite 1s ease-in-out -0.4s;
}

.loading:after {
  right: -28px;
  animation: rectangle infinite 1s ease-in-out;
}

@keyframes rectangle {
  0%,
  80%,
  100% {
    height: 40px;
    box-shadow: 0 0 rgb(255, 255, 255,.8);
  }

  40% {
    height: 60px;
    box-shadow: 0 -20px rgb(255, 255, 255,.8);
  }
}
</style>