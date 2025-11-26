<template>
    <div class="suisan">
		<div class="title" style="height: 50px; line-height: 50px; color: rgb(255,255,240,.8); padding-left: 5px; font-size: 24px; font-weight: bolder; border-bottom: 1px solid rgb(255,255,255,.2); background: rgb(255,255,255,.1);">为您推荐</div>
        <div v-show="loading">
            <div class="background">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
        <div v-show="!loading" style="margin-left: 20px;"> 
            <div style="margin-top: 10px;margin-left: 20px; font-weight: bolder; color: rgb(0,255,255,.8);">视频推荐</div>
            <div style="display: flex; flex-wrap: wrap; color: rgb(255,255,255,.5);">
                <div v-for="(v,index) in showVideos" :key="index" style="height: 200px; width: 200px; margin-left: 20px; margin-top: 20px; background: rgb(255,255,255,.1);">
                    <a :href="v.arcurl" target="_blank">
                        <div style="height: 100px; overflow: hidden;"><img :src="v.pic" style="display: inline-block; height: 100px; width: 200px;"></div>
                    </a>
                    <div style="height: 40px; line-height: 40px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: rgb(255,255,255,.8);">{{ strHandle(v.title) }}</div> 
                    <div style="font-size: 12px; padding-left: 10px;">
                        <span>播放量&nbsp;&nbsp;&nbsp;{{ numHandle(v.play) }}</span> <tr></tr>
                        <span>点赞量&nbsp;&nbsp;&nbsp;{{ numHandle(v.like) }}</span> <tr></tr>
                        <span> 时&nbsp;&nbsp;&nbsp;长&nbsp;&nbsp;&nbsp;{{ v.duration }}</span>
                    </div> 
                </div>
                <div style="height: 140px; width: 140px; margin-left: 20px; margin-top: 20px; padding-left: 60px; padding-top: 60px;">
                    <div @click="videoChange()">
                      <svg t="1715517070939" class="icon" viewBox="0 0 1310 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5109" width="80" height="80"><path d="M1154.33472 486.6048l32.52224-30.3104a52.96128 52.96128 0 0 1 74.71104 2.53952c19.8656 21.2992 18.67776 54.84544-2.58048 74.71104l-130.33472 121.56928a52.6336 52.6336 0 0 1-37.2736 14.17216c-16.71168 0-31.5392-7.74144-41.24672-19.82464l-119.56224-128.2048a52.71552 52.71552 0 0 1 2.58048-74.67008 52.96128 52.96128 0 0 1 74.71104 2.58048l40.96 43.95008c-12.288-208.93696-185.58976-374.53824-397.59872-374.53824-91.01312 0-174.8992 30.63808-241.95072 82.00192a52.75648 52.75648 0 1 1-69.46816-78.39744L339.1488 121.2416a501.9648 501.9648 0 0 1 312.1152-108.25728c268.0832 0 487.34208 209.42848 503.11168 473.57952z m-900.79232 7.45472A398.29504 398.29504 0 0 0 651.264 915.37408a396.9024 396.9024 0 0 0 255.09888-92.40576l0.8192 1.024a52.8384 52.8384 0 0 1 84.3776 42.31168c0 20.43904-11.63264 38.13376-28.59008 46.8992a501.9648 501.9648 0 0 1-311.7056 107.97056c-278.3232 0-504.0128-225.6896-504.0128-504.0128 0-5.36576 0.08192-10.73152 0.28672-16.05632l-30.06464 23.92064a52.75648 52.75648 0 0 1-74.21952-8.3968A52.87936 52.87936 0 0 1 51.6096 442.368l134.47168-107.19232a52.87936 52.87936 0 0 1 79.21664 3.97312l111.08352 139.34592a52.87936 52.87936 0 0 1-82.7392 65.9456l-40.09984-50.33984z" fill="rgb(255,255,255,.5)" p-id="5110"></path></svg>
                    </div>
                </div>
            </div>
            <div style="margin-left: 20px; font-weight: bolder; margin-top: 20px; color: goldenrod;">up推荐</div>
            <div style="display: flex; color: rgb(255,255,255,.5);">
                <div v-for="(u,index) in tjUps" :key="index" style="width: 200px; margin-left: 20px; margin-top: 10px; height: 150px;">
                  <div style="margin: 10px auto; height: 50px; width: 50px;"><a :href="'https://space.bilibili.com/'+u.mid" target="_blank"><img :src="u.upic" alt="" style="height: 50px; width: 50px; display: inline-block; border-radius: 25px;"></a></div>
                  <div style="margin: 10px auto; height: 50px; width: 100px; line-height: 50px; font-size: 12px; font-weight: lighter; color: white; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; text-align: center;">{{ u.uname }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {getSuisan} from '@/assets/js/api'

export default {
  name: 'suisan',
  data(){
    return{
        tjVideos:[],
        showVideos:[],
        loading:true,
        tjUps:[]
    }
  },
  mounted(){
    this.getVideos()
  },
  methods:{
    async getVideos(){
      let result = await getSuisan(localStorage.getItem('username'))
      this.tjVideos = result.ssVideos
      this.tjUps = result.ssUps.sort((u1,u2)=>u2.fans-u1.fans).splice(0,6)
      if(this.tjVideos.length == 0){
        this.tjVideos = this.videos
      }
      this.videoChange()
      setTimeout(()=>this.loading=false,2000)
    },
    videoChange(){
        if(this.tjVideos.length == 0) return this.$message.info("没有更多了~")
        this.showVideos = this.tjVideos.splice(0,11)
    },
    strHandle(str){
        return str.replace('<em class="keyword">',"").replace('</em>','')
    },
    numHandle(num){
        if(num < 10000) return num
        else return (num/10000).toFixed(1) + '万'
    }
  },
  activated(){
    this.getVideos()
  },
  deactivated(){
    this.loading = true
  }
}
</script>

<style scoped>
.suisan{
  position: absolute;
  width: 1400px;
  height: 700px;
  right: 20px;
  top: 20px;
  background-color: #1E2131;
  /* background-color: #1E2131; */
  color: rgb(250,250,240,.5);
}
img:hover{
    cursor: pointer;
}
.icon:hover{
    cursor: pointer;
}
.background {
  width: 1400px;
  height: 500px;
  --amount: 20;
  margin-top: 20px;
}

.background span {
  width: 8vmin;
  height: 8vmin;
  border-radius: 4vmin;
  backface-visibility: hidden;
  position: absolute;
  animation-name: move;
  animation-timing-function: cubic-bezier(0.4, 0, 1, 0.8);
  animation-iteration-count: infinite;
  animation-duration: 3s;
  top: calc(50% - 4vmin);
  left: 50%;
  transform-origin: -4vmin center;
}
.background span:nth-child(1) {
  background: #35b0ab;
  animation-delay: -0.5s;
  opacity: 0;
}
.background span:nth-child(2) {
  background: #35b0ab;
  animation-delay: -1s;
  opacity: 0;
}
.background span:nth-child(3) {
  background: #c5f0a4;
  animation-delay: -1.5s;
  opacity: 0;
}
.background span:nth-child(4) {
  background: #35b0ab;
  animation-delay: -2s;
  opacity: 0;
}
.background span:nth-child(5) {
  background: #226b80;
  animation-delay: -2.5s;
  opacity: 0;
}
.background span:nth-child(6) {
  background: #226b80;
  animation-delay: -3s;
  opacity: 0;
}

@keyframes move {
  0% {
    transform: scale(1) rotate(0deg) translate3d(0, 0, 1px);
  }
  30% {
    opacity: 1;
  }
  100% {
    z-index: 10;
    transform: scale(0) rotate(360deg) translate3d(0, 0, 1px);
  }
}
</style>