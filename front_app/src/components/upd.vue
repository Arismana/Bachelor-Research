<template>
     <div class="upd">
        <div class="basicInfo" style="margin-top: 10px;margin-left: 10px; border: 2px solid #0095f2; width: 650px; background-color: #1E2131; height: 290px;">
            <div class="title">基本信息</div>
            <div class="_line1" style="height: 50px; margin-top: 20px; position: relative;">
              <div style="position: absolute; right: 30px; top: 50px; color: rgb(255,255,255,.5);">
                头像：<img :src="basicInfo.txUrl" alt="touxiang" style="display: inline-block; width: 80px; height: 80px; vertical-align: middle; ">
              </div>
              <span style="margin-left: 20px; margin-top: 20px; width: 150px; display: inline-block; white-space: nowrap; overflow-x: hidden; text-overflow: ellipsis;">
                up主：
                <span style="color:rgb(255,255,255,.7)">{{ basicInfo.name }}</span>
              </span>
              <span style="margin-left: 30px;  width: 115px;">uid：<span style="color:rgb(255,255,255,.7)">{{ basicInfo.uid }}</span></span>
              <span style="margin-left: 30px; ">性别：
                <span style="color:rgb(255,255,255,.7)">{{ basicInfo.sex }}</span>
                </span>
              <tr></tr>
              <span style="margin-left: 20px;  margin-top: 40px; display: inline-block;">生日：
                <span style="color:rgb(255,255,255,.7)">{{ basicInfo.birthday }}</span>
              </span>
              <span style="margin-left: 30px; display: inline-block;">等级：
                <span style="color:rgb(255,255,255,.7)">{{ basicInfo.level }}</span>
              </span>
              <span style="margin-left: 30px;  display: inline-block;">学校：
                <span style="color:rgb(255,255,255,.7)">{{ basicInfo.school }}</span>
              </span>
              <tr></tr>
              <span style="margin-left: 20px;  margin-top: 40px; display: inline-block;">粉丝数：
                <span style="color:rgb(255,255,255,.7)">{{ basicInfo.follower }}</span>
              </span>
              <span style="margin-left: 30px; display: inline-block;">
                <span style="color:rgb(255,255,255,.7)">关注数：{{ basicInfo.following }}</span>
                </span>
              <span style="margin-left: 30px; display: inline-block; white-space: nowrap; overflow-x: hidden; text-overflow: ellipsis; width: 200px;">
                <span style="color:rgb(255,255,255,.7)">签名：{{ basicInfo.sign }}</span>
              </span>
            </div>
        </div>

        <div style="margin-left:20px;margin-top: 10px; border: 2px solid #0095f2; background-color: #1E2131;">
          <div class="title">优质稿件数据</div>
          <zaz :videoInfo="videoInfo"></zaz>
        </div>

          <div style="margin-left:10px; margin-top: 20px; border: 2px solid #0095f2; background-color: #1E2131;">
            <div class="title">稿件时长</div>
            <zab :videoInfo="videoInfo" :tag="false"></zab>
          </div>

        <div style="margin-left:7px; margin-top: 20px; border: 2px solid #0095f2; background-color: #1E2131;">
          <div class="title">同体量up主对比</div>
          <ldt :videoInfo="videoInfo" :basicInfo="basicInfo" @videoAnaBack="summary"></ldt>
        </div>

        <div style="margin-left:20px; margin-top: 20px; border: 2px solid #0095f2; background-color: #1E2131;">
          <div class="title">近期视频标签</div>
          <cyt :videoFeedBackCiyun="videoKeywords"></cyt>
        </div>

        <div class="basicInfo" style="margin-left:20px;margin-top: 20px; border: 2px solid #0095f2; width: 287px; background-color: #1E2131; height: 290px;">
            <div class="title">up主综合评价</div>
            <div style="width: 100%;">
              <p style="color: rgb(84,255,159,.5); margin-top: 15px; padding-left: 20px; font-size: small;">粉丝得分</p>
              <ul>
              <li>
                <div>{{ getNumber(6,'fanScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(5,'fanScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(4,'fanScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(3,'fanScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(2,'fanScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(1,'fanScore') }}</div>
              </li>
            </ul>
            </div>

            <div style="width: 100%;">
              <p style="color: rgb(127,255,212,.5); margin-top: 15px; padding-left: 20px; font-size: small;">视频得分</p>
              <ul>
              <li>
                <div>{{ getNumber(6,'videoQulityScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(5,'videoQulityScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(4,'videoQulityScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(3,'videoQulityScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(2,'videoQulityScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(1,'videoQulityScore') }}</div>
              </li>
            </ul>
            </div>

            <div style="width: 100%;">
              <p style="color: rgb(0,255,255,.8); margin-top: 15px; padding-left: 22px;">总得分</p>
              <ul>
              <li>
                <div>{{ getNumber(6,'totalScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(5,'totalScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(4,'totalScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(3,'totalScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(2,'totalScore') }}</div>
              </li>
              <li>
                <div>{{ getNumber(1,'totalScore') }}</div>
              </li>
            </ul>
            </div>
            
        </div>
     </div>
</template>

<script>

import zab from './echarts/zhuAndBing.vue'
import zaz from './echarts/zhuAndZhe.vue'
import ldt from './echarts/ldt.vue'
import cyt from './echarts/cyt.vue'
export default {
  name: 'upd',
  props: {
    basicInfo:{},
    videoInfo:{},
    videoKeywords:[]
  },
  data(){
    return {
      bInfo:this.basicInfo,
      totalScore:0,
      fanScore:0,
      videoQulityScore:0,
      anaData:{}
    }
  },
  mounted(){
    for(let i = 0; i < this.videoInfo.length; i++){
      this.videoInfo[i].pubtime = this.toTime(this.videoInfo[i].pubtime)
      this.videoInfo[i].duration = this.toDuration(this.videoInfo[i].duration)
      this.videoInfo[i].copy_right = this.toCopyRight(this.videoInfo[i].copy_right)
	}
  },
  components:{zab,zaz,ldt,cyt},
  methods:{
  toSomewhere(next){
        this.$router.push({ name:next})
    },
  goBack() {
		this.$parent.attention()
    history.pushState(null, null, document.URL);
        window.addEventListener('popstate', function () {
            history.pushState(null, null, document.URL);
        });
  },
  summary(anaData){ //计算up主总得分
    this.anaData = anaData
    let fansNum = this.basicInfo.follower
    let count = 0

    let fanNumScore = Math.round(1000 * (fansNum / 10000)) //粉丝量得分
    if(fanNumScore > 600000) fanNumScore = Math.floor(Math.random() * 10000) + 600000 //超出得分界限，获得随机数

    let fanQulityScore = Math.round(100000 * (anaData.avgPlay / (fansNum * 0.6))) //粉丝质量得分
    if(fanQulityScore > 200000) fanQulityScore = Math.floor(Math.random() * 10000) + 200000 
    
    this.fanScore = fanQulityScore + fanNumScore //粉丝得分

    let videoQulityScore = Math.round(200000 * (anaData.videoQulity / 100)) //视频质量得分
    if(videoQulityScore > 200000) videoQulityScore = Math.floor(Math.random() * 10000) + 200000 

    this.videoQulityScore = videoQulityScore

    count = (fanNumScore + fanQulityScore + videoQulityScore)
    if(count > 999999) count = 999999
    this.totalScore = count
  },
  getNumber(wTag,tag){
    return (Math.floor(this[tag] / Math.pow(10, wTag - 1)) % 10)
  },
  toTime(time){
    let now = new Date(time * 1000),
    y = now.getFullYear(),
    m = now.getMonth() + 1,
    d = now.getDate();
    return y + "-" + (m < 10 ? "0" + m : m) + "-" + (d < 10 ? "0" + d : d) + " " + now.toTimeString().substr(0, 8);
  },
  toDuration(dur){
    let min = Math.floor(dur / 60)
    let s = dur - (min * 60)
    return (min + '分' + s +'秒')
  },
  toCopyRight(copyRight){
    return (copyRight == 1 ? '是' : '否')
  }
  },
  created() { 
    // 检查浏览器是否支持history API
    if (window.history && window.history.pushState) {
  // 如果支持，给window添加popstate监听事件，用于监听后退按钮的点击
    window.addEventListener('popstate', this.goBack, false);
    }

// 在IE中，为了确保后退按钮可以触发popstate事件，必须执行以下两行代码
    window.history.pushState('forward', null, '');
    window.history.forward(1);
  },
  destroyed() { // 销毁vm组件
  // 避免堆栈溢出，多次创建、多次触发
    window.removeEventListener('popstate', this.goBack, false);
  }
}
</script>

<style scoped>
.upd{
    display: flex;
    flex-wrap: wrap;
} 
.upd .basicInfo .title{
  height: 40px;
  text-align: left;
  border: none;
  background-color: #252E44;
  padding-left: 20px;
  line-height: 40px;
  font-weight: bolder;
  font-size: 16px;
  color: white;
}
.upd .basicInfo ul{
  list-style: none;
  display: flex;
  justify-content: center;
}
.upd .basicInfo ul li{
  border: 1px solid #252E44;
  height: 20px;
  width: 20px;
  margin: 10px;
  margin-top: 10px;
}
.upd .basicInfo ul li div{
  color: white;
  font-weight: bolder;
  font-size: 12px;
  text-align: center;
  line-height: 20px;
  background-color: #204397;
}
.zxstyle{
        text-align: left;
        font-weight: bold;
        color: aliceblue;
        padding-top: 10px;
    }
.ly {
        text-align: center;
        font-size: 25px;
        color: white;
        width: 100%;
        background-color: #252E44;
    }
/* /deep/ .el-table .el-table__row{
    background-color: #282C34 !important;
    color: #ffffff !important;
    font-weight: lighter !important;
}
/deep/ .el-table .el-table__row:hover{
  background-color: #ccc !important;
  color: black !important;
  cursor: pointer;
} */

.basicInfo span{
  color: rgb(255,255,255,.5);
}

.title{
  height: 40px;
  text-align: left;
  border: none;
  background-color: #252E44;
  padding-left: 20px;
  line-height: 40px;
  font-weight: bolder;
  font-size: 16px;
  color: white;
}
</style>