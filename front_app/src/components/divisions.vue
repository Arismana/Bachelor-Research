<template>
    <div class="div">
        <div v-if="searchShow">
            <div class="title" style="height: 50px; line-height: 50px; color: rgb(255,255,240,.8); padding-left: 5px; font-size: 24px; font-weight: bolder; border-bottom: 1px solid rgb(255,255,255,.2); background: rgb(255,255,255,.1);">分区分析</div>
        <div style="margin: 50px auto; height: 50px; width: 250px;">
            <el-autocomplete 
            v-model="state" 
            :fetch-suggestions="querySearchAsync" 
            placeholder="请选择分区" 
            @select="handleSelect"
            >
        </el-autocomplete>
        </div>
        <div style="color: rgb(255,255,255,.5); margin-left: 10px; margin-top: 150px;height: 40px; line-height: 40px; border-bottom: 1px solid rgb(255,255,255,.2);">
            <span>热门分区</span>
            <svg t="1713770239970" class="icon" style="padding-top: 5px; vertical-align: text-bottom;" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="7017" width="30" height="30"><path d="M423.477333 938.666667S45.045333 855.424 214.186667 442.282667c0 0 38.4 45.909333 33.12 68 0 0 30.101333-104.277333 95.072-166.570667C398.165333 290.186667 454.848 139.712 402.570667 85.333333c0 0 258.933333 54.378667 287.754666 326.378667 0 0 33.12-86.666667 101.12-95.232 0 0-20.906667 47.616 0 119.04 0 0 214.485333 367.146667-155.157333 491.242667 0 0 110.805333-125.813333-124.181333-341.717334 0 0-55.402667 115.626667-88.533334 156.373334-0.096 0.106667-92.522667 103.722667-0.096 197.248z" fill="#d81e06" p-id="7018"></path></svg>
        </div>
        <div style="display: flex;">
            <div style="height: 250px; width: 200px; background-color: rgb(0,0,0,.2); margin-top: 50px; margin-left: 40px;">
                <div style="width: 200px; height: 115px; overflow: hidden;" @click="handleSelect({value:'全站',tid:'0',rid:'0'})"><img src="../assets/images/Bilibili-logo.jpg" style="display: inline-block; width: 200px;"></div>
                    <div style="margin-top: 12px;">
                        <div style="color: rgb(255,255,255,.8);">全站</div>
                        <div style="color: rgb(255,255,255,.5); font-size: 12px; font-weight: lighter; margin-top: 15px;">该网站于2009年6月26日创建,是中国年轻一代的标志性品牌及领先的视频社区,被网友们亲切地称为“B站”。</div>
                    </div>
            </div>
            <div style="height: 250px; width: 200px; background-color: rgb(0,0,0,.2); margin-top: 50px; margin-left: 40px;">
                <div>
                    <div style="width: 200px; height: 113px; overflow: hidden;" @click="handleSelect({value:'动画',tid:'13',rid:'1'})"><img src="../assets/images/anime.jpg" style="display: inline-block; width: 200px;"></div>
                    <div style="margin-top: 12px;">
                        <div style="color: rgb(255,255,255,.8);">动漫区</div>
                        <div style="color: rgb(255,255,255,.5); font-size: 12px; font-weight: lighter; margin-top: 15px;">主要有六个子分区,包含动画或静画的二次创作视频、手办或模型玩具的开箱展示等内容。</div>
                    </div>
                </div>
            </div>
            <div style="height: 250px; width: 200px; background-color: rgb(0,0,0,.2); margin-top: 50px; margin-left: 440px;">
                <div>
                    <div style="width: 200px; height: 120px; overflow: hidden;" @click="handleSelect({value:'鬼畜',tid:'119',rid:'119'})"><img src="../assets/images/guichu.jpg" style="display: inline-block;height: 120px;"></div>
                    <div style="margin-top: 12px;">
                        <div style="color: rgb(255,255,255,.8);">鬼畜区</div>
                        <div style="color: rgb(255,255,255,.5); font-size: 12px; font-weight: lighter; margin-top: 15px;">Bilibili鬼畜区建立于2014年9月。这里有一众鬼畜明星,元首,金坷垃,金馆长等陪你笑不停! </div>
                    </div>
                </div>
            </div>
            <div style="height: 250px; width: 200px; background-color: rgb(0,0,0,.2); margin-top: 50px; margin-left: 40px;">
                <div>
                    <div style="width: 200px; height: 120px; overflow: hidden;" @click="handleSelect({value:'科技',tid:'188',rid:'188'})"><img src="../assets/images/keji.jpg" style="display: inline-block; width: 200px;"></div>
                    <div style="margin-top: 12px;">
                        <div style="color: rgb(255,255,255,.8);">科技区</div>
                        <div style="color: rgb(255,255,255,.5); font-size: 12px; font-weight: lighter; margin-top: 15px;">原数码区与新增的软件应用、计算机技术、工业·工程·机械和极客DIY二级分区,一同组成为新的科技一级分区。</div>
                    </div>
                </div>
            </div>
        </div>
        </div>
        
        <div ref="loading" style="margin-left: 650px; margin-top: 250px;" v-if="loadingShow">
			      <loading></loading>
		    </div>

        <div v-if="dataShow">
            <div class="title" style="height: 50px; line-height: 50px; color: rgb(255,255,240,.8); padding-left: 5px; font-size: 24px; font-weight: bolder; border-bottom: 1px solid rgb(255,255,255,.2); background: rgb(255,255,255,.2);">{{ dName+'分区' }}</div>
            <svg t="1713617450379" @click="back(0)" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="8525" width="30" height="30"><path d="M511.347131 65.214281c-246.678192 0-446.650643 199.972451-446.650643 446.650643s199.972451 446.650643 446.650643 446.650643 446.650643-199.972451 446.650643-446.650643S758.025323 65.214281 511.347131 65.214281zM510.744403 894.491391c-211.92262 0-383.720382-171.797761-383.720382-383.720382s171.797761-383.720382 383.720382-383.720382 383.720382 171.797761 383.720382 383.720382S722.667024 894.491391 510.744403 894.491391zM502.173191 708.726523c8.139378 8.138354 8.139378 21.332864 0 29.471219l0 0c-8.138354 8.139378-21.332864 8.139378-29.471219 0L261.234723 526.730493c-8.139378-8.138354-8.139378-21.331841 0-29.471219l0 0c8.138354-8.138354 21.332864-8.138354 29.471219 0L502.173191 708.726523 502.173191 708.726523zM290.705941 526.470573c-8.138354 8.139378-21.332864 8.139378-29.471219 0l0 0c-8.139378-8.138354-8.139378-21.331841 0-29.471219l211.467249-211.467249c8.138354-8.138354 21.332864-8.138354 29.471219 0l0 0c8.139378 8.139378 8.139378 21.332864 0 29.472242L290.705941 526.470573 290.705941 526.470573zM290.705941 526.470573M737.565339 483.569484c15.624862-0.010233 28.296463 12.648065 28.304649 28.271904l0 0c0.010233 15.623839-12.648065 28.296463-28.271904 28.304649l-405.963988 0.233314c-15.623839 0.010233-28.29544-12.647041-28.304649-28.271904l0 0c-0.00921-15.623839 12.649088-28.29544 28.271904-28.304649L737.565339 483.569484 737.565339 483.569484z" fill="rgb(255,255,255,.5)" p-id="8526"></path></svg>
            <div style="display: flex; flex-wrap: wrap;">
                <div style="margin-top: 10px;margin-left: 10px; border: 2px solid #0095f2; background-color: #1E2131; height: 270px; width: 450px;">
                    <div class="title">分区介绍</div>
                    <div style="margin-top: 20px;  margin-left: 10px;">
                        <span style="color: rgb(255,255,255,.7); font-weight: lighter; font-size: 12px;">分区名</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: rgb(255,255,240,.8);">{{ divInfo.dInfo.basicinfo.name }}</span> <tr></tr>
                        <span style="color: rgb(255,255,255,.7); margin-top: 15px; display: inline-block; font-weight: lighter; font-size: 12px;">分区ID</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: rgb(255,255,240,.8);">{{ divInfo.dInfo.basicinfo.channelId }}</span> <tr></tr>
                        <span style="color: rgb(255,255,255,.7); margin-top: 15px; display: inline-block; font-weight: lighter; font-size: 12px;">网&nbsp;&nbsp;&nbsp;址</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a style="color: #60BFE2; text-decoration: none;" :href="divInfo.dInfo.basicinfo.url">https:{{ divInfo.dInfo.basicinfo.url }}</a> <tr></tr>
                        <span style="color: rgb(255,255,255,.7); margin-top: 15px; display: inline-block; font-weight: lighter; font-size: 12px;">子分区</span><tr></tr>
                        <div style="display: flex; justify-content:center">
                            <el-tag v-for="(item,index) in divInfo.dInfo.basicinfo.sub" v-show="index<=4" :key="index" :style="{marginLeft:(index==0?'0':'10px'),marginTop:'15px'}"><a :href="item.url" style="text-decoration: none; color: #409EFF;">{{ item.name }}</a></el-tag>
                        </div>
                    </div>
                </div>

                <div :style="{marginTop:'10px',marginLeft:'10px', border: '2px solid #0095f2', backgroundColor: '#1E2131', height: '270px', width: '280px'}">
                  <div class="title">热门标签</div>
                  <div style="display: flex; justify-content: space-around; background-color: #353846; color: #199DFF; font-weight: lighter; height: 30px; line-height: 30px; font-size: small;">
                    <span>序号</span><span>标签ID</span><span>标签名</span>
                  </div>
                    <gundong :hotTags="divInfo.dInfo.hotTags.tags"></gundong>
                  </div>

                <div :style="{marginTop:'10px',marginLeft:'10px', border: '2px solid #0095f2', backgroundColor: '#1E2131'}">
                  <div class="title">热门视频数据</div>
                  <divzaz :videoInfo="divInfo.vInfo" :dName="dName"></divzaz>
                </div>

                <div style="margin-left:10px; margin-top: 10px; border: 2px solid #0095f2; background-color: #1E2131; ">
                  <div class="title">稿件时长</div>
                  <zab :videoInfo="divInfo.vInfo" :tag="true"></zab>
                </div>

                <div :style="{marginTop:'10px',marginLeft:'10px', border: '2px solid #0095f2', backgroundColor: '#1E2131', height: '300px', width: '280px'}">
                    <div class="title">评分排行</div>
                    <rank :vArr="divInfo.vInfo"></rank>
                </div>
                
                <div :style="{marginTop:'10px',marginLeft:'10px', border: '2px solid #0095f2', backgroundColor: '#1E2131',height:'300px',width:'600px'}">
                  <div class="title">发布地址</div>
                  <chinaMap :vArr="divInfo.vInfo"></chinaMap>
                </div>

            </div>
        </div>

        <div v-if="allDataShow">
          <div class="title" style="height: 50px; line-height: 50px; color: rgb(255,255,240,.8); padding-left: 5px; font-size: 24px; font-weight: bolder; border-bottom: 1px solid rgb(255,255,255,.2); background: rgb(255,255,255,.2);">全站分析</div>
          <svg t="1713617450379" @click="back(1)" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="8525" width="30" height="30"><path d="M511.347131 65.214281c-246.678192 0-446.650643 199.972451-446.650643 446.650643s199.972451 446.650643 446.650643 446.650643 446.650643-199.972451 446.650643-446.650643S758.025323 65.214281 511.347131 65.214281zM510.744403 894.491391c-211.92262 0-383.720382-171.797761-383.720382-383.720382s171.797761-383.720382 383.720382-383.720382 383.720382 171.797761 383.720382 383.720382S722.667024 894.491391 510.744403 894.491391zM502.173191 708.726523c8.139378 8.138354 8.139378 21.332864 0 29.471219l0 0c-8.138354 8.139378-21.332864 8.139378-29.471219 0L261.234723 526.730493c-8.139378-8.138354-8.139378-21.331841 0-29.471219l0 0c8.138354-8.138354 21.332864-8.138354 29.471219 0L502.173191 708.726523 502.173191 708.726523zM290.705941 526.470573c-8.138354 8.139378-21.332864 8.139378-29.471219 0l0 0c-8.139378-8.138354-8.139378-21.331841 0-29.471219l211.467249-211.467249c8.138354-8.138354 21.332864-8.138354 29.471219 0l0 0c8.139378 8.139378 8.139378 21.332864 0 29.472242L290.705941 526.470573 290.705941 526.470573zM290.705941 526.470573M737.565339 483.569484c15.624862-0.010233 28.296463 12.648065 28.304649 28.271904l0 0c0.010233 15.623839-12.648065 28.296463-28.271904 28.304649l-405.963988 0.233314c-15.623839 0.010233-28.29544-12.647041-28.304649-28.271904l0 0c-0.00921-15.623839 12.649088-28.29544 28.271904-28.304649L737.565339 483.569484 737.565339 483.569484z" fill="rgb(255,255,255,.5)" p-id="8526"></path></svg>
          <div style="display: flex; flex-wrap: wrap;">
            <div :style="{marginLeft:'10px', border: '2px solid #0095f2', backgroundColor: '#1E2131',height:'300px',width:'600px'}">
                  <div class="title">分区热门视频数前五</div>
                  <ddz :allDivInfo="allDivInfo"></ddz>
            </div>

            <div :style="{marginLeft:'10px', border: '2px solid #0095f2', backgroundColor: '#1E2131',height:'300px'}">
                  <div class="title">全站热门视频时长</div>
                  <zab :videoInfo="allDivInfo.varr" :tag="false"></zab>
            </div>

            <div :style="{marginLeft:'10px', border: '2px solid #0095f2', backgroundColor: '#1E2131',height:'300px'}">
                  <div class="title">全站热门标签</div>
                  <cyt :videoFeedBackCiyun="allDivInfo.keywords"></cyt>
            </div>

            <div :style="{marginTop:'2px',marginLeft:'10px', border: '2px solid #0095f2', backgroundColor: '#1E2131',height:'300px'}">
                  <div class="title">全站视频质量占比</div>
                  <piet :videoInfo="allDivInfo.varr"></piet>
            </div>

            <div :style="{marginTop:'2px',marginLeft:'10px', border: '2px solid #0095f2', backgroundColor: '#1E2131',height:'300px',width:'718px'}">
                  <div class="title">发布地址</div>
                  <chinaMap :vArr="allDivInfo.varr" :tag="true"></chinaMap>
            </div>
          </div>
        </div>
    </div>
</template>

<script>
import {getDivInfo,getAllDivInfo} from '@/assets/js/api'
import loading from './loading.vue'
import gundong from './gundong.vue'
import zab from './echarts/zhuAndBing.vue'
import divzaz from './echarts/divZhuAndZhe.vue'
import rank from './echarts/rank.vue'
import chinaMap from './echarts/chinaMap.vue'
import ddz from './echarts/ddZhu.vue'
import cyt from './echarts/cyt.vue'
import piet from './echarts/piet.vue'

  export default {
    name:'div',
    components:{loading,gundong,zab,divzaz,rank,chinaMap,ddz,cyt,piet},
    data() {
      return {
        restaurants: [],
        state: '',
        timeout:  null,
        divInfo:{},
        searchShow:true,
        loadingShow:false,
        dataShow:false,
        allDataShow:false,
        dName:'',
        allDivInfo:{}
      }
    },
    methods: {
      loadAll() {
        return [
          { "value": "全站", "rid": "0","tid":"" },
          { "value": "动画", "rid": "1" ,"tid":"13"},
          { "value": "音乐", "rid": "3" ,"tid":"3"},
          { "value": "舞蹈", "rid": "129" ,"tid":"129"},
          { "value": "游戏", "rid": "4","tid":"4" },
          { "value": "知识", "rid": "36","tid":"36" },
          { "value": "科技", "rid": "188","tid":"188" },
          { "value": "运动", "rid": "234","tid":"234" },
          { "value": "汽车", "rid": "223","tid":"223" },
          { "value": "生活", "rid": "160","tid":"160" },
          { "value": "美食", "rid": "211","tid":"211" },
          { "value": "动物圈", "rid": "217","tid":"217" },
          { "value": "鬼畜", "rid": "119","tid":"119" },
          { "value": "时尚", "rid": "155","tid":"155" },
          { "value": "娱乐", "rid": "5","tid":"5" },
          { "value": "影视", "rid": "181","tid":"181" },
          { "value": "原创", "rid": "0" ,"tid":"167"}
        ]
      },
      querySearchAsync(queryString, cb) { //模糊关键词查询
        var restaurants = this.restaurants;
        var results = queryString ? restaurants.filter(this.createStateFilter(queryString)) : restaurants
        clearTimeout(this.timeout);
        this.timeout = setTimeout(() => {
          cb(results);
        }, 3000 * Math.random());
      },
      createStateFilter(queryString) {
        return (state) => {
          return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0)
        }
      },
      async handleSelect(item) { //选择某一项后触发的函数
        this.searchShow = false
        this.loadingShow = true
        let username = localStorage.getItem('username')
        this.dName = item.value
        if(this.dName == '全站'){
          let result = await(getAllDivInfo(username))
          if(result.error) return this.$message.error("网络出现波动")
          this.allDivInfo = result
          setTimeout(()=>{
            this.loadingShow = false
            this.allDataShow = true
        },1000)
        }
        else{
          this.divInfo = await(getDivInfo(username,item.tid,item.rid,item.value))
          setTimeout(()=>{
            this.loadingShow = false
            this.dataShow = true
        },1000)
        }
      },
      back(tag){
        if(tag) this.allDataShow = false
        else this.dataShow = false
        this.searchShow = true
      }
    },
    mounted() {
      this.restaurants = this.loadAll()
    },
    deactivated(){
    this.searchShow = true
    this.loadingShow = false
    this.allDataShow = false
    this.dataShow = false
  }
  }
</script>

<style scoped>
.div{
    position: absolute;
    width: 1400px;
    height: 700px;
    right: 20px;
    top: 20px;
	background-color: #1E2131;
	z-index: 0;
}
img{
    transition: all .4s;
}
img:hover{
  cursor: pointer;
  transform: scale(1.2);
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
.icon{
  margin-left: 10px;
	transition: all .4s;
}
.icon:hover{
  cursor: pointer;
  transform: scale(1.2);
}
.icon:hover path{
  fill: rgb(255,255,255,.8);
}
</style>