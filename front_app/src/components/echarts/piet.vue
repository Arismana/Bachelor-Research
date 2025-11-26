<template>
    <div class="piet">
        <div id="EChart_piet" style="width:600px;height:220px"></div>
    </div>
</template>

<script>
export default {
  name: 'piet',
  props: {
    videoInfo:[]
  },
  data(){
    return{
        perObj:{}
    }
  },
  mounted(){
    this.getData()
    this.getRenderer()
  },
  methods:{
    getRenderer() {
    //   基于准备好的dom，初始化echarts实例
      let EChart = this.$echarts.init(document.getElementById("EChart_piet"));
      let p = this.perObj
      // 配置参数
      let option = {
  tooltip: {
    trigger: 'item'
  },
  visualMap: {
    show: false,
    min: 10,
    max: 50,
    inRange: {
      colorLightness: [0.8, 0]
    }
  },
  series: [
    {
      name: '质量得分范围',
      type: 'pie',
      radius: '80%',
      center: ['55%', '50%'],
      data: [
        { value: p.lt2, name: 'score<2' },
        { value: p.tt3, name: 'score:2~3' },
        { value: p.tt5, name: 'score:3~5' },
        { value: p.mt5, name: 'score>5'}
      ].sort(function (a, b) {
        return a.value - b.value;
      }),
      roseType: 'radius',
      label: {
        color: 'rgba(255, 255, 255, 0.3)'
      },
      labelLine: {
        lineStyle: {
          color: 'rgba(255, 255, 255, 0.3)'
        },
        smooth: 0.2,
        length: 10,
        length2: 20
      },
      itemStyle: {
        color: '#c23531',
        shadowBlur: 200,
        shadowColor: 'rgba(0, 0, 0, 0.5)'
      },
      animationType: 'scale',
      animationEasing: 'elasticOut',
      animationDelay: function (idx) {
        return Math.random() * 200;
      }
    }
  ]
}
setTimeout(()=>{
    EChart.setOption(option)
},500)
    },
    getData(){
        let perObj = {'lt2':0,'tt3':0,'tt5':0,'mt5':0}
        let i = 0
        for(i;i<this.videoInfo.length;i++){
            let item = this.videoInfo[i]
            let score = this.getScore(item.playData.favorite,item.playData.share,item.playData.coin,item.playData.like,item.playData.danmaku,item.dur)
            if(score < 2) perObj.lt2++
            else if(score>=2 && score<3) perObj.tt3++
            else if(score>=3 && score<5) perObj.tt5++
            else perObj.mt5++
        }
        this.perObj = perObj
    },
    getScore(fav,share,coin,like,danmaku,dur){
        return ((0.497 * fav + 0.463 * share + 0.257 * coin + 0.095 * like - 0.0269 * danmaku - 0.001 * dur - 0.017 * 5 - 0.018 * 50)/10000).toFixed(1)
    }
  }
}
</script>