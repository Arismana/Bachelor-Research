<template>
    <div class="vd">
        <div class="basicInfo" style="margin-top:10px;border: 2px solid #0095f2;  background-color: #1E2131; height: 290px; width: 800px; margin-left: 20px;">
            <div class="title">基本信息</div>
            <div class="_line1" style=" margin-top: 20px; position: relative;">
                <span style="margin-left: 20px; color: white; width: 200px; display: inline-block; white-space: nowrap; overflow-x: hidden; text-overflow: ellipsis;">
                    标题：{{ vBasicInfo.title }}
                </span>
              <span style="margin-left: 20px; color: white; width: 200px; display: inline-block; white-space: nowrap; overflow-x: hidden; text-overflow: ellipsis;">
                上传者：{{ vBasicInfo.owner.name }}
              </span>
              <span style="margin-left: 100px; margin-top: 20px;color: white; display: inline-block;">封面:</span>
              <tr></tr>
              <span style="margin-left: 20px; margin-top: 20px;color: white; display: inline-block;">
                上传时间：{{ getDate(vBasicInfo.pubdate) }}
              </span>
              <span style="margin-left: 20px; color: white; width: 115px;">bv号：{{ vBasicInfo.bvid }}</span>
              <tr></tr>
              <div style="position: absolute; right: 40px; top: 0px; color: white;">
                <img :src="vBasicInfo.pic" alt="cover" style="display: inline-block; height: 100px; vertical-align: middle; ">
              </div>
            </div>
            <div class="_line2" style="margin-top: 40px;">
              <ul>
              <li style="margin-left: 0;">
                <div style="background-color: #252E44; height: 30px; font-size: 14px; font-weight: lighter; line-height: 30px;">播放量</div>
                <div style="color:#FF4500">{{ vBasicInfo.stat.view }}</div>
              </li>
              <li>
                <div style="background-color: #252E44; height: 30px; font-size: 14px; font-weight: lighter; line-height: 30px;">点赞量</div>
                <div style="color:yellow">{{ vBasicInfo.stat.like }}</div>
              </li>
              <li>
                <div style="background-color: #252E44; height: 30px; font-size: 14px; font-weight: lighter; line-height: 30px;">投币量</div>
                <div style="color:blueviolet">{{ vBasicInfo.stat.coin }}</div>
              </li>
              <li>
                <div style="background-color: #252E44; height: 30px; font-size: 14px; font-weight: lighter; line-height: 30px;">收藏量</div>
                <div style="color: aqua;">{{ vBasicInfo.stat.favorite }}</div>
              </li>
              <li>
                <div style="background-color: #252E44; height: 30px; font-size: 14px; font-weight: lighter; line-height: 30px;">分享量</div>
                <div style="color:goldenrod">{{ vBasicInfo.stat.share }}</div>
              </li>
              <li>
                <div style="background-color: #252E44; height: 30px; font-size: 14px; font-weight: lighter; line-height: 30px;">弹幕量</div>
                <div style="color: blanchedalmond;">{{ vBasicInfo.stat.danmaku }}</div>
              </li>
              </ul>
            </div>  
        </div>

          <div style="border: 2px solid #0095f2;margin-top:10px;  background-color: #1E2131; margin-left: 20px;">
            <div class="title">数据柱状图</div>
            <zzt :allNums="allNums" :allRates="allRates"></zzt>
          </div>

        <div style="margin-left: 20px;margin-top: 30px; border: 2px solid #0095f2;  background-color: #1E2131;">
            <div class="title">数据雷达图</div>
            <vldt :allNums="allNums" :bvid="vBasicInfo.bvid"></vldt>
        </div>

        <div style="margin-left: 20px;margin-top: 30px; border: 2px solid #0095f2;  background-color: #1E2131;">
           <div class="title">弹幕词云图</div>
            <cyt :videoFeedBackCiyun="videoFeedBackCiyun"></cyt>
        </div>

        <div style=" margin-left: 20px;margin-top: 30px;border: 2px solid #0095f2;  background-color: #1E2131; width: 520px; height: 290px;">
            <div class="title">情感分析</div>
            <div class="danmu" style="display: inline-block;margin-top: 20px;margin-left: 10px;">
              <danmuB :danmuQxzb="danmuQxzb"></danmuB>
              <div style="margin-left:30px;font-size: small;">
                <span style="color: rgb(255, 255, 255,.7); font-weight: bold;">弹幕情感得分：</span>
                <span style="color: aqua; font-size: large;">{{ danmuScore.toFixed(0) }}</span>
              </div> 
            </div>
            <div class="comments" style="display: inline-block;margin-left:-10px;margin-top: 20px;">
              <commentsB :commentsQxzb="commentsQxzb"></commentsB>
              <div style="margin-left:30px;font-size: small;">
                <span style="color: rgb(255, 255, 255,.7); font-weight: bold;">评论情感得分：</span>
                <span style="color:gold;font-size: large;">{{ pinglunScore.toFixed(0) }}</span>
              </div> 
            </div>
        </div>
    </div>
</template>

<script>
import zzt from './echarts/zzt.vue'
import vldt from './echarts/vldt.vue'
import cyt from './echarts/cyt.vue'
import danmuB from './echarts/danmuQxb.vue'
import commentsB from './echarts/commentsQxb.vue'
  export default {
    name: 'vd',
    components: {zzt,vldt,cyt,danmuB,commentsB},
    data(){
        return{
          allRates:{
          replyRate:0,
          likeRate:0,
          coinRate:0,
          favoRate:0,
          shareRate:0,
          danmuRate:0
        },
        allNums:{
          view:0,
          like:0,
          coin:0,
          favorite:0,
          share:0,
          danmaku:0,
          reply:0
        },
        videoSore:0
        }
    },
    props:{
        vBasicInfo:{},
        danmuQxzb:{},
        commentsQxzb:{},
        videoFeedBackCiyun:[],
        danmuScore:Number,
        pinglunScore:Number
    },
    mounted(){
      this.getDatas()
      this.getVScore()
    },
    methods:{
      toDuration(dur){
        let min = Math.floor(dur / 60)
        let s = dur - (min * 60)
        return (min + '分' + s +'秒')
      },
      getDatas(){
        this.allRates.replyRate = (this.vBasicInfo.stat.reply/this.vBasicInfo.stat.view).toFixed(3)
        this.allRates.likeRate = (this.vBasicInfo.stat.like/this.vBasicInfo.stat.view).toFixed(3)
        this.allRates.coinRate = (this.vBasicInfo.stat.coin/this.vBasicInfo.stat.view).toFixed(3)
        this.allRates.favoRate = (this.vBasicInfo.stat.favorite/this.vBasicInfo.stat.view).toFixed(3)
        this.allRates.shareRate = (this.vBasicInfo.stat.share/this.vBasicInfo.stat.view).toFixed(3)
        this.allRates.danmuRate = (this.vBasicInfo.stat.danmaku/this.vBasicInfo.stat.view).toFixed(3)
        this.allNums.view = this.vBasicInfo.stat.view
        this.allNums.like = this.vBasicInfo.stat.like
        this.allNums.coin = this.vBasicInfo.stat.coin
        this.allNums.favorite = this.vBasicInfo.stat.favorite
        this.allNums.share = this.vBasicInfo.stat.share
        this.allNums.danmaku = this.vBasicInfo.stat.danmaku
        this.allNums.reply = this.vBasicInfo.stat.reply
      },
      getVScore(){
        let score = 500 * (Number(this.allRates.likeRate) + Number(this.allRates.coinRate) + Number(this.allRates.favoRate) + Number(this.allRates.shareRate) + Number(this.allRates.danmuRate) + Number(this.allRates.replyRate))
        this.videoSore = score >= 100 ? 100 : score
      },
      getFinalScore(){
        return (this.videoSore / 2 + this.danmuScore / 4 + this.pinglunScore / 4).toFixed(2)
      },
      getDate(time){
        let timestamp3 = time
        let newDate = new Date()
        newDate.setTime(timestamp3 * 1000)
        return newDate.toLocaleDateString()
      }
    }
  }
  </script>

  <style scoped>
.vd{
    display: flex;
    flex-wrap: wrap;
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
.vd .basicInfo ul{
  list-style: none;
  display: flex;
  margin-top: 20px;
  justify-content: center;
}
.vd .basicInfo ul li{
  border: 1px solid #252E44;
  margin-left: 20px;
  width: 100px;
}
.vd .basicInfo ul li div{
  color: white;
  font-weight: bold;
  height: 40px;
  font-size: 14px;
  text-align: center;
  line-height: 40px;
  background-color: #1E2131;
  border: 1px solid #252E44;
}
</style>