<template>
    <div id="zaz">
      <div id="EChart_3" style="width: 320px; height: 220px;"></div>
    </div>
  </template>

<script>

export default {
    name: 'ldt',
    data(){
      return{
        similarUpData:{},
        fansMax:0,
        playMax:0
      }
    },
    props:{
        basicInfo:{},
        videoInfo:{}
    },
    mounted(){
    let max_ = this.getRank()
    this.fansMax = max_.fansMax
    this.playMax = max_.playMax
    this.getRenderer()
  },
  methods:{
    getRenderer(){
    console.log('FansMax = '+this.getRank().fansMax)
    let EChart = this.$echarts.init(document.getElementById("EChart_3"));
    let option = {
  legend: {
    data: [this.similarUpData.name || '哎呀，数据丢失啦',this.basicInfo.name],
    orient : 'vertical',
    x : 'left',
    y:'top',
    textStyle:{
                 color:"white",
                 fontWeight:'light'
              },
  },
  radar: {
    // shape: 'circle',
    // center:['50%','50%'],
    radius: '60%',
    indicator: [
      { name: '粉丝量', max: this.fansMax },
      { name: '平均播放量', max: this.playMax },
      { name: '平均点赞率', max: 0.1 },
      { name: '平均重播量', max: 0.01 },
      { name: '平均弹幕互动率', max: 0.01 },
      { name: '视频综合质量', max: 100 }
    ],
    axisName: {
      color: "white",
      fontWeight: "lighter"
    },
  },
  series: [
    {
      name: 'UP主对比',
      type: 'radar',
      data: [
      {
          value: [this.similarUpData.fans, this.similarUpData.avgplay, this.similarUpData.avgThu, 
          this.similarUpData.avgrep, this.similarUpData.avgdanmu, this.similarUpData.vQuli],
          name: this.similarUpData.name || '哎呀，数据丢失啦',
          itemStyle: {     //此属性的颜色和下面areaStyle属性的颜色都设置成相同色即可实现
                        color: '#008B8B',
                        fontWeight:'lighter',
                        fontSize:'10px',
                        borderColor: '#008B8B',
                },
                areaStyle: {
                        color: '#008B8B',
                 },
        },
        {
          value: [],
          name: this.basicInfo.name,
          itemStyle: {     //此属性的颜色和下面areaStyle属性的颜色都设置成相同色即可实现
                        color: '#5840D4',
                        borderColor: '#5840D4',
                },
                areaStyle: {
                        color: '#5840D4',
                 },
        }
      ]
    }
  ]
};
let arr = [this.basicInfo.follower]
let avgPlay = (this.getSum('play') / this.videoInfo.length).toFixed(0)
if(avgPlay > this.getRank().playMax) avgPlay = this.playMax

let avgThuRate = (this.getSum('thumb_up') / this.videoInfo.length).toFixed(3)
if(avgThuRate > 0.1) avgThuRate = 0.1

let avgRepRate = (this.getSum('reply') / this.videoInfo.length).toFixed(3)
if(avgRepRate > 0.01) avgRepRate = 0.01

let avgDanRate = (this.getSum('danmaku') / this.videoInfo.length).toFixed(3)
if(avgDanRate > 0.01) avgDanRate = 0.01

let videoQulity = this.getVideoQulity(avgPlay,avgThuRate,avgRepRate,avgDanRate)

arr.push(avgPlay,avgThuRate,avgRepRate,avgDanRate,videoQulity)
// console.log('播放量'+avgPlay +', 重播率' + avgRepRate +', 点赞率' + avgThuRate + '弹幕率' + avgDanRate +'视频得分' +videoQulity)
this.$emit('videoAnaBack',{avgPlay,avgRepRate,avgThuRate,avgDanRate,videoQulity})
option.series[0].data[1].value = arr
setTimeout(()=> EChart.setOption(option), 500)
    },
    getSum(tag){
    let count = 0
    if(tag == 'play'){
        for(let i = 0; i < this.videoInfo.length; i++){
            count += this.videoInfo[i].cnt_info.play
        }
        return count
    } else{
        for(let i = 0; i < this.videoInfo.length; i++){
            let rate = this.videoInfo[i].cnt_info[tag] / this.videoInfo[i].cnt_info.play
            count += rate
        }
        return count
    }
  },
  getVideoQulity(avgPlay,avgThuRate,avgRepRate,avgDanRate){
    let fans = this.basicInfo.follower
    let playScore,thumbUpScore,replyScore,danmakuScore
    if((avgPlay - (fans * 0.5)) <= 0) playScore = 0
    else playScore = ((avgPlay - (fans * 0.4)) / avgPlay) * 30 //假设粉丝看到此视频的概率为0.5,那么可以根据非粉丝带来的播放量占比计算播放量得分

    if(avgThuRate <= 0.01) thumbUpScore = 0
    else thumbUpScore = (avgThuRate / avgThuRate) * 30

    if(avgRepRate >= 0.005)  replyScore = 20
    else replyScore = (avgRepRate / 0.005) * 20

    if(avgDanRate >= 0.005) danmakuScore = 20
    else danmakuScore = (avgDanRate / 0.005) * 20

    let videoQulity = Math.round(playScore + thumbUpScore + replyScore + danmakuScore)
    return (videoQulity)
  },
  getRank(){
    let fansMax,playMax
    let fansNum = this.basicInfo.follower
    let o = {
      name:'',
      fans:0,
      avgThu:0.0,
      avgplay:0,
      avgdanmu:0.0,
      avgrep:0.0,
      vQuli:0
    }
    if(fansNum <= 30000) { //0-3w
        fansMax = 30000
        playMax = 20000
        o.name = '小强视频啊'
        o.fans = 6444
        o.avgThu = 0.045
        o.avgdanmu = 0.004
        o.avgrep = 0.01
        o.vQuli = 53
        o.avgplay = 8094
        this.similarUpData = o
    }else if(fansNum > 30000 && fansNum < 50000){ //3w-5w
        fansMax = 50000
        playMax = 200000
        o.name = '青又轻'
        o.fans = 44598
        o.avgThu = 0.033
        o.avgdanmu = 0.001
        o.avgrep = 0.005
        o.vQuli = 50
        o.avgplay = 34623
        this.similarUpData = o
    }else if(fansNum > 50000 && fansNum < 200000){ //5w-20w
        fansMax = 200000
        playMax = 500000
        o.name = '同福小号'
        o.fans = 111376
        o.avgThu = 0.008
        o.avgdanmu = 0.007
        o.avgrep = 0.002
        o.vQuli = 44
        o.avgplay = 97817
        this.similarUpData = o
    }else if(fansNum > 200000 && fansNum < 500000){ //20w-50w
        fansMax = 500000
        playMax = 2000000
        o.name = '里昂的奇妙人生'
        o.fans = 331752
        o.avgThu = 0.063
        o.avgdanmu = 0.001
        o.avgrep = 0.001
        o.vQuli = 54
        o.avgplay = 992324
        this.similarUpData = o
    }else if(fansNum > 500000 && fansNum < 1000000){ //50w-100w
        fansMax = 1000000
        playMax = 2000000
        o.name = '峡谷混学家'
        o.fans = 597221
        o.avgThu = 0.065
        o.avgdanmu = 0.002
        o.avgrep = 0.001
        o.vQuli = 56
        o.avgplay = 1003928
        this.similarUpData = o
    }else if(fansNum > 1000000 && fansNum < 5000000){ //100w-500w
        fansMax = 5000000
        playMax = 5000000
        o.name = '上将王司徒'
        o.fans = 2066562
        o.avgThu = 0.061
        o.avgdanmu = 0.002
        o.avgrep = 0.001
        o.vQuli = 46
        o.avgplay = 1499306
        this.similarUpData = o
    }else if(fansNum > 5000000 && fansNum < 10000000){ //500w-1000w
        fansMax = 10000000
        playMax = 10000000
        o.name = '逗比的雀巢'
        o.fans = 7493836
        o.avgThu = 0.064
        o.avgdanmu = 0.001
        o.avgrep = 0.001
        o.vQuli = 41
        o.avgplay = 10000000
        this.similarUpData = o
    }else{ // 1000w+
        fansMax = 20000000
        playMax = 10000000
        o.name = '罗翔说刑法'
        o.fans = 20000000
        o.avgThu = 0.081
        o.avgdanmu = 0.004
        o.avgrep = 0.003
        o.vQuli = 51
        o.avgplay = 1848916
        this.similarUpData = o
    }
    return {fansMax,playMax}
  }
  }
}
</script>
