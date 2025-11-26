<template>
    <div id="zaz">
      <div id="EChart_3" style="width: 387px; height: 250px;"></div>
    </div>
</template>

<script>

export default {
    name: 'vldt',
    data(){
      return{
        similarVData:{},
        vMaxData:{}
      }
    },
    props:{
        allNums:{},
        bvid:String
    },
    mounted(){
        setTimeout(()=> {
            this.getRank()
            this.getRenderer()
        } , 1000)
  },
  methods:{
    getRenderer(){
    let EChart = this.$echarts.init(document.getElementById("EChart_3"));
    let option = {
  title: {
    text: '',
  },
  legend: {
    data: [this.similarVData.bvid + '(base)' || '哎呀，数据丢失啦',this.bvid],
    orient : 'vertical',
    x : 'left',
    y:'0',
    textStyle:{
                 color:"white",
                 fontWeight:'light'
              },
  },
  radar: {
    // shape: 'circle',
    // center:['50%','50%'],
    indicator: [
      { name: '点赞量', max: this.vMaxData.like },
      { name: '投币量', max: this.vMaxData.coin },
      { name: '收藏量', max: this.vMaxData.favorite },
      { name: '转发量', max: this.vMaxData.share },
      { name: '弹幕量', max: this.vMaxData.danmaku },
      { name: '重播量', max: this.vMaxData.reply }
    ],
    axisName: {
      color: "white",
      fontWeight: "lighter"
    },
  },
  series: [
    {
      name: '相似播放量视频数据对比',
      type: 'radar',
      data: [
      {
          value: [this.similarVData.like>this.vMaxData.like?this.vMaxData.like:this.similarVData.like,
           this.similarVData.coin>this.vMaxData.coin?this.vMaxData.coin:this.similarVData.coin, 
           this.similarVData.favorite>this.vMaxData.favorite?this.vMaxData.favorite:this.similarVData.favorite, 
          this.similarVData.share>this.vMaxData.share?this.vMaxData.share:this.similarVData.share, 
          this.similarVData.danmaku>this.vMaxData.danmaku?this.vMaxData.danmaku:this.similarVData.danmaku,
           this.similarVData.reply>this.vMaxData.reply?this.vMaxData.reply:this.similarVData.reply],
          name: this.similarVData.bvid + '(base)' || '哎呀，数据丢失啦',
          itemStyle: {     //此属性的颜色和下面areaStyle属性的颜色都设置成相同色即可实现
                        color: '#008B8B',
                        borderColor: '#008B8B',
                },
                areaStyle: {
                        color: '#008B8B',
                 },
        },
        {
          value: [this.allNums.like>this.vMaxData.like?this.vMaxData.like:this.allNums.like,
          this.allNums.coin>this.vMaxData.coin?this.vMaxData.coin:this.allNums.coin,
          this.allNums.favorite>this.vMaxData.favorite?this.vMaxData.favorite:this.allNums.favorite,
          this.allNums.share>this.vMaxData.share?this.vMaxData.share:this.allNums.share,
          this.allNums.danmaku>this.vMaxData.danmaku?this.vMaxData.danmaku:this.allNums.danmaku,
          this.allNums.reply>this.vMaxData.reply?this.vMaxData.reply:this.allNums.reply],
          name: this.bvid,
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
setTimeout(()=> EChart.setOption(option), 500)
    },
  getRank(){
    let view = this.allNums.view
    let so = {
          bvid:'',
          like:0,
          coin:0,
          favorite:0,
          share:0,
          danmaku:0,
          reply:0
    }
    let mo = {
          like:0,
          coin:0,
          favorite:0,
          share:0,
          danmaku:0,
          reply:0
    }
    if(view <= 10000) { //0-1w
        mo.like = 2000
        mo.coin = 200
        mo.favorite = 100
        mo.share = 100
        mo.danmaku = 100
        mo.reply = 100

        so.bvid = 'BV1Qm411d7ZN'
        so.like = 538
        so.coin = 60
        so.favorite = 19
        so.share = 2
        so.danmaku = 5
        so.reply = 54
    }else if(view > 10000 && view < 50000){ //1w-5w
        mo.like = 5000
        mo.coin = 500
        mo.favorite = 500
        mo.share = 300
        mo.danmaku = 500
        mo.reply = 200

        so.bvid = 'BV1m3411S7KR'
        so.like = 3487
        so.coin = 102
        so.favorite = 59
        so.share = 23
        so.danmaku = 42
        so.reply = 65
    }else if(view > 50000 && view < 200000){ //5w-20w
        mo.like = 20000
        mo.coin = 2000
        mo.favorite = 2000
        mo.share = 2000
        mo.danmaku = 2000
        mo.reply = 1000

        so.bvid = 'BV1xY4y1U7qQ'
        so.like = 7071
        so.coin = 175
        so.favorite = 582
        so.share = 714
        so.danmaku = 324
        so.reply = 1287
    }else if(view > 200000 && view < 500000){ //20w-50w
        mo.like = 20000
        mo.coin = 2000
        mo.favorite = 2000
        mo.share = 2000
        mo.danmaku = 2000
        mo.reply = 1000

        so.bvid = 'BV1xY4y1U7qQ'
        so.like = 7071
        so.coin = 175
        so.favorite = 582
        so.share = 714
        so.danmaku = 324
        so.reply = 1287
    }else if(view > 500000 && view < 1000000){ //50w-100w
        mo.like = 100000
        mo.coin = 30000
        mo.favorite = 10000
        mo.share = 10000
        mo.danmaku = 10000
        mo.reply = 5000

        so.bvid = 'BV1YX4y1q7Sw'
        so.like = 70393
        so.coin = 29998
        so.favorite = 7670
        so.share = 8942
        so.danmaku = 5674
        so.reply = 4261
    }else if(view > 1000000 && view < 5000000){ //100w-500w
        mo.like = 200000
        mo.coin = 50000
        mo.favorite = 20000
        mo.share = 10000
        mo.danmaku = 10000
        mo.reply = 5000

        so.bvid = 'BV1Na4y1A7wU'
        so.like = 183525
        so.coin = 6619
        so.favorite = 21623
        so.share = 780
        so.danmaku = 3685
        so.reply = 1566
    }else if(view > 5000000 && view < 10000000){ //500w-1000w
        mo.like = 1000000
        mo.coin = 500000
        mo.favorite = 200000
        mo.share = 100000
        mo.danmaku = 20000
        mo.reply = 20000

        so.bvid = 'BV1Dx4y1D7VT'
        so.like = 947469
        so.coin = 570602
        so.favorite = 225238
        so.share = 57106
        so.danmaku = 15447
        so.reply = 11324
    }else{ // 1000w+
        mo.like = 2000000
        mo.coin = 1000000
        mo.favorite = 500000
        mo.share = 100000
        mo.danmaku = 20000
        mo.reply = 20000

        so.bvid = 'BV1TP4y1H7ey'
        so.like = 1560048
        so.coin = 1010950
        so.favorite = 368251
        so.share = 66550
        so.danmaku = 15737
        so.reply = 11885
    }
    this.vMaxData = mo
    this.similarVData = so
  }
  }
}
</script>
