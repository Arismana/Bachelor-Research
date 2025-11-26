<template>
    <div class="zab">
        <div id="EChart_2" :style="{width:(tag?'450px':'320px'),height:'220px'}"></div>
    </div>
</template>

<script>
export default {
  name: 'zab',
  props: {
    videoInfo:[],
    tag:Boolean
  },
  mounted(){
    this.getRenderer();
  },
  methods:{
    getRenderer() {
    //   基于准备好的dom，初始化echarts实例
      let EChart = this.$echarts.init(document.getElementById("EChart_2"));
      // 配置参数
      let option = {
        color:['#4962FC','#FF6666','#dd3ee5','#12e78c','#fe8104'],
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient : 'vertical',
        x : 'right',
        y:'bottom',
        textStyle:{
          color:"white",
          fontWeight:'light'
        },
        data:['<1min(短)','1~5min(中短)','5~10min(中长)','>10min(长)']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {
                show: true, 
                type: ['pie', 'funnel'],
                option: {
                    funnel: {
                        x: '25%',
                        width: '50%',
                        funnelAlign: 'left',
                        max: 1548
                    }
                }
            },
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    series : [
        {
            name:'视频长度',
            type:'pie',
            radius : '60%',
            center: ['35%', '50%'],
            itemStyle: {
                  normal: {
                      label: {
                          textStyle: {
                            color:'white',
                              fontSize: 14,
                              fontWeight:'light'
                          }
                      }
                  }
              },
            data:[]
        }
    ]
};
let durArr = [{value:0,name:'<1min(短)'},{value:0,name:'1~5min(中短)'},{value:0,name:'5~10min(中长)'},{value:0,name:'>10min(长)'}]
for(let i = 0; i < this.videoInfo.length; i++){
    let dur = (this.videoInfo[i].duration ? this.videoInfo[i].duration : this.videoInfo[i].dur)
    if(dur < 60) durArr[0].value++
    else if(dur >= 60 && dur < 300) durArr[1].value++
    else if(dur >= 300 && dur < 600) durArr[2].value++
    else durArr[3].value++
}
setTimeout(()=>{
    option.series[0].data = durArr
    EChart.setOption(option);
},500)

    
},
  }
}
</script>