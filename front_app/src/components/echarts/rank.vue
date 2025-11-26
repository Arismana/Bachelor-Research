<template>
    <div class="rank">
        <div id="EChart_rank" style="height: 300px; width: 280px;"></div>
    </div>
</template>

<script>
export default {
  name: 'rank',
  props: {
    vArr:{},
  },
  data(){
    return{
        scoreRank:[]
    }
  },
  mounted(){
    this.getData()
    this.getRenderer()
  },
  methods:{
    getRenderer() {
      let EChart = this.$echarts.init(document.getElementById("EChart_rank"));
     let option = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {
    x:'left',
    textStyle:{
                 color:"white",
                 fontWeight:'light'
    },
  },
  grid: {
    left: '3%',
    right: '4%',
    top:'10%',
    containLabel: true
  },
  xAxis: {
    type: 'value',
    boundaryGap: [0, 0.01],
    axisLine: {
                    lineStyle: {
                        color: 'rgb(255,255,255,.2)',
                        width: 0.5
                    }
                },
    axisLabel: {
            formatter: (value)=>{
                return (value / 10000).toFixed(1)
            },
            color:'rgb(255,255,255,.5)',
            textStyle: {
                fontSize: 10,
                fontWeight:'lighter'
            },
    },
    splitLine:{
                lineStyle: {
                        color: 'rgb(255,255,255,.4)',
                        width: 0.1
                    }
    }
  },
  yAxis: {
    type: 'category',
    data: [this.scoreRank[7].title,this.scoreRank[6].title,this.scoreRank[5].title,this.scoreRank[4].title,this.scoreRank[3].title,
    this.scoreRank[2].title,this.scoreRank[1].title,this.scoreRank[0].title
  ],
    axisLabel:{
                    color:'rgb(255,255,255,.5)',
                    textStyle: {
                        fontSize: 10,
                        fontWeight:'lighter'
                    },
                    formatter:(value) =>{
                        if(value.length > 3){
                            return `${value.slice(0,3)}...`
                        }
                        return value
                    }
                }
  },
  series: [
    {
      name: '评分',
      barWidth: '40%',
      type: 'bar',
      itemStyle:{
                    normal: {
                        color: '#506BFF'
                        // function(params) {
                        //     let color = ['#FF9900','#CCFFFF','#003399','#FF0033','#FFFF00',]
                        //     return color[params.dataIndex]
                        // }
                    }
                },
      data: [this.scoreRank[7].score, this.scoreRank[6].score, this.scoreRank[5].score, this.scoreRank[4].score, this.scoreRank[3].score,
      this.scoreRank[2].score,this.scoreRank[1].score,this.scoreRank[0].score
    ]
    }
  ]
}
setTimeout(()=>{
    EChart.setOption(option);
},500)

    
    },
    getData(){
        let rankArr = []
        let i = 0
        for(i;i<=8;i++){
          let item = this.vArr[i]
            let obj = {
                'title':item.title,
                'score':this.getScore(item.playData.favorite,item.playData.share,item.playData.coin,item.playData.like,item.playData.danmaku,item.dur)
            }
            rankArr.push(obj)
        }
        rankArr.sort((a,b) => b.score - a.score)
        this.scoreRank = rankArr
    },
    getScore(fav,share,coin,like,danmaku,dur){
        return (0.497 * fav + 0.463 * share + 0.257 * coin + 0.095 * like - 0.0269 * danmaku - 0.001 * dur - 0.017 * 5 - 0.018 * 50).toFixed(1)
    }
  }
}
</script>