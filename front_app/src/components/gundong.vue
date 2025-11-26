<template>
        <div id="review_box" @mouseover="rollStop()" @mouseout="rollStart(60)" style="height: 140px; overflow: hidden;">
        <ul id="comment1">
            <li v-for="(t,index) in hotTags" :key="index" style="display: flex; font-weight: lighter; color: #60BFE2; font-size: 10px; position: relative; height: 20px; width: 100%; line-height: 20px;">
                <span style="display: inline-block; margin-left: 40px; position: absolute;">{{ index }}</span>
                <span style="display: inline-block; margin-left: 120px; position: absolute;">{{ t.tag_id }}</span>
                <span style="display: inline-block; margin-left: 210px; position: absolute;">{{ t.tag_name }}</span>
            </li>
        </ul>
        <ul id="comment2"></ul>
    </div>
  </template>
   
  <script>
  export default {
    components: {},
    props:{
        hotTags:[]
    },
data (){
    return {
        timer: null,
    }
},
mounted() {
  	this.roll(60);
},
beforeDestroy() {
  	if (this.timer) clearInterval(this.timer);
},
methods:{
    roll(t) {
    var ul1 = document.getElementById("comment1");
    var ul2 = document.getElementById("comment2");
    var ulbox = document.getElementById("review_box");
    ul2.innerHTML = ul1.innerHTML;
    ulbox.scrollTop = 0;
    this.rollStart(t);
},
rollStart(t) {
    var ul1 = document.getElementById("comment1");
    var ul2 = document.getElementById("comment2");
    var ulbox = document.getElementById("review_box");
    this.rollStop();
    this.timer = setInterval(()=>{
        // 当滚动高度大于列表内容高度时恢复为0
        if (ulbox.scrollTop >= ul1.scrollHeight) {
            ulbox.scrollTop = 0;
        } else {
            ulbox.scrollTop++;
        }
    }, t);
},
rollStop(){
    clearInterval(this.timer);
}

},

}
  </script>
   
  <style scoped>
  li:hover{
    background-color: #353846;
  }
  </style>