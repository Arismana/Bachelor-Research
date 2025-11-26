<template>
    <div id="china_map_box" :style="{height:(tag?'260px':'300px'), width: '100%'}">
        <div id="china_map_" style="height: 100%; width: 100%;"></div>
    </div>
  </template>
  
  <script>
  import '@/assets/js/china.js' 
  export default {
    name:'chinaMap',
    data() {
      return {
        mapData:{}
      }
    },
    props:{
      vArr:[],
      tag:Boolean
    },
    mounted(){
      this.getData()
      setTimeout(()=>this.getRenderer(),1000)
  },
    methods: {
      getRenderer(){
        let EChart = this.$echarts.init(document.getElementById("china_map_"))
        let options = {
          tooltip: {
            triggerOn: "mousemove",   //mousemove、click
            padding:8,
            borderWidth:1,
            borderColor:'#409eff',
            backgroundColor:'rgba(255,255,255,0.7)',
            textStyle:{
              color:'#000000',
              fontSize:13
            },
            formatter: function(e) {
              console.log(e)
              let context = `
                 <div>
                     <p><b style="font-size:15px;">${e.name}</b>(热门视频发布IP)</p>
                     <p class="tooltip_style"><span class="tooltip_left">发布数</span><span class="tooltip_right">${e.value}</span></p>
                 </div>
              `
              return context;
            }
          },
          visualMap: { //范围提示
            show:true,
            left: 26,
            top: 10,
            showLabel:true,
            textStyle:{
              color:'rgb(255,255,255,.5)'
            },
            pieces: [
              {
                gte: 15,
                label: ">= 15",
                color: "#1f307b"
              },
              {
                gte: 10,
                lt: 15,
                label: "10 - 14",
                color: "#3c57ce"
              },
              {
                gte: 5,
                lt:10,
                label: "5 - 9",
                color: "#6f83db"
              },
              {
                gte: 2,
                lt: 5,
                label: "2 - 4",
                color: "#9face7"
              },
              {
                lt:2,
                label:'<=1',
                color: "#bcc5ee"
              }
            ]
          },
          geo: {
            map: "china",
            scaleLimit: {
              min: 1,
              max: 2
            },
            zoom: 1,
            top: 5,
            label: {
              normal: {
                show:true,
                fontSize: "8",
                fontWidth:"lighter",
                color: "rgba(0,0,0,0.3)"
              }
            },
            itemStyle: {
              normal: {
                //shadowBlur: 50,
                //shadowColor: 'rgba(0, 0, 0, 0.2)',
                borderColor: "rgba(0, 0, 0, 0.2)"
              },
              emphasis: {
                areaColor: "#f2d5ad",
                shadowOffsetX: 0,
                shadowOffsetY: 0,
                borderWidth: 0
              }
            }
          },
          series: [
            {
              name: "突发事件",
              type: "map",
              geoIndex: 0,
              data:[]
            }
          ]
        }
        let data_ = []
        for(let key in this.mapData){
            let obj = {'name':key,'value':this.mapData[key]}
            data_.push(obj)
        }
        setTimeout(()=>{
          options.series[0].data = data_
          EChart.setOption(options)
        },500)
      },
      getData(){
        let obj={
          "南海诸岛":0,
            "北京":0,
            "天津": 0,
            "上海": 0,
            "重庆": 0,
            "河北": 0,
            "河南": 0,
            "云南": 0,
            "辽宁": 0,
            "黑龙江": 0,
            "湖南": 0,
            "安徽": 0,
            "山东": 0,
            "新疆": 0,
            "江苏": 0,
            "浙江": 0,
            "江西": 0,
            "湖北": 0,
            "广西": 0,
            "甘肃": 0,
            "山西": 0,
            "内蒙古": 0,
            "陕西": 0,
            "吉林": 0,
            "福建": 0,
            "贵州": 0,
            "广东": 0,
            "青海": 0,
            "西藏": 0,
            "四川": 0,
            "宁夏": 0,
            "海南": 0,
            "台湾": 0,
            "香港": 0,
            "澳门": 0
        }
        let i = 0
        for(i;i<this.vArr.length;i++) obj[this.vArr[i].loc]++
        this.mapData = obj
      }
    },
    // mounted() {
    //     this.$nextTick(()=>{
    //         this.initEchartMap();
    //     })
      
    // }
  }
  </script>
  
  <style scoped>
      /* #china_map_box {
          height: 100%;
          position: relative;
      }
      #china_map_box #china_map{
          height: 100%;
      }
       #china_map_box .china_map_logo{
          position: absolute;
          top: 0;
          left: 0;
          width:45px;
       } */
  </style>
  