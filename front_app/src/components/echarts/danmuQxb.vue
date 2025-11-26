<template>
    <div id="dmB">
      <div id="EChart_bing1" style="width: 260px; height: 200px;"></div>
    </div>
  </template>
  
  <script>
  
  export default {
    name: 'danmuB',
    components: {},
    data(){
        return{
            vsSortByPlay:[]
        }
    },
    props:{
        allNums:{},
        allRates:{},
        danmuQxzb:{}
    },
    mounted(){
        setTimeout(()=> this.getRenderer() , 500)
    },
   methods:{
    getRenderer() {
      let EChart = this.$echarts.init(document.getElementById("EChart_bing1"));
      let option = {
        color:['#4962FC','#12e78c','#fe8104'],
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient : 'horizontal',
    x : 'left',
    textStyle:{
        color:"white",
        fontWeight:'light'
    },
  },
  series: [
    {
      name: '弹幕情绪',
      type: 'pie',
      radius: ['40%', '60%'],
      avoidLabelOverlap: false,
      minAngle: 0,
      padAngle: 5,
      itemStyle: {
        borderRadius: 10
      },
      label: {
                    normal: {
                        // 各分区的提示内容
                        // params: 即下面传入的data数组,通过自定义函数，展示你想要的内容和格式
                        formatter: function(params){ 
                            return params.name+"\n\n"+params.percent+"%";
                        },  
                        textStyle: {            // 提示文字的样式
                            color: 'white',
                            fontWeight: 'light'
                        }
                    }
                },
      labelLine: {
        normal:{
                        length:15,     // 指示线宽度
                        lineStyle: {
                            color: "white"    // 指示线颜色  
                        }
                    },
      },
      data: [
        { value: this.danmuQxzb.ac, name: '积极' },
        { value: this.danmuQxzb.xj, name: '消极' },
        { value: this.danmuQxzb.zl, name: '中性' },
      ]
    }
  ]
};
        setTimeout(()=> EChart.setOption(option) , 1000)
    }
   } 
  }
  </script>