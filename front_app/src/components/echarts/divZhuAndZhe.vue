<template>
    <div id="divzaz">
      <div id="EChart_divzaz" style="width: 600px; height: 230px;"></div>
    </div>
  </template>
  
  <script>
  
  export default {
    name: 'divzaz',
    components: {},
    data(){
        return{
            vsSortByPlay:[]
        }
    },
    props:{
        videoInfo:{},
        dName:String
    },
    mounted(){
        this.getData()
        this.getRenderer()
    },
   methods:{
    getData(){
        let videoData = [];
        let i;
        let length = this.videoInfo.length
        for(i = 0; i<length; i++){
            videoData[i] = this.videoInfo[i].playData
            videoData[i].title = this.videoInfo[i].title
        }
        videoData.sort((a,b) => b.view - a.view)
        this.vsSortByPlay = videoData.slice(0,5)
    },
    getRenderer() {
      let EChart = this.$echarts.init(document.getElementById("EChart_divzaz"))
      var option = {
        grid:{
		    y:100,
            
	    },
        tooltip: {
			trigger:'axis',
			formatter: '{b0}({a0}): {c0}<br />{b1}({a1}): {c1}%'
		},
            legend: {
              orient : 'vertical',
              x : 'left',
              data:["播放量","点赞率"],
              textStyle:{
                 color:"white",
                 fontWeight:'light'
              },
            },
            xAxis: {
                type:'category',
                data: [],
                axisLine: {
                    lineStyle: {
                        color: 'rgb(255,255,255,.2)',
                        width: 0.5
                    }
                },
                axisLabel:{
                    color:'rgb(255,255,255,.5)',
                    textStyle: {
                        fontSize: "12",
                        fontWeight:'lighter'
                    },
                    rotate:45,
                    formatter:(value) =>{
                        if(value.length > 3){
                            return `${value.slice(0,3)}...`
                        }
                        return value
                    }
                }
            },
            yAxis: [ {
                type: 'value',
                name: '播放量(千万)',
                interval: this.dName=='鬼畜'?20000000:5000000,
                axisTick: {
                   alignWithLabel: false,
                   show: false,
               },
               axisLabel: {
                    formatter: (value)=>{
                        return (value / 10000000).toFixed(1)
                    },
                    color:'rgb(255,255,255,.5)',
                    textStyle: {
                        fontSize: 10,
                        fontWeight:'lighter'
                    },
                },
               show:true,
               splitLine:{
               lineStyle: {
                        color: 'rgb(255,255,255,.4)',
                        width: 0.1
                    }
               },
               axisLine: {
                    lineStyle: {
                        color: 'rgb(255,255,255,.5)',
                        textStyle:{
                            fontSize: 10,
                            fontWeight:'lighter'
                        },
                        width: 0.5
                    }
                }
            },{
                type: 'value',
                name: '比率',
                min: 0.0,
                max: 20.0,
                interval: 10.0,
                splitLine:{
                show:false
               },
                axisTick: {
                   alignWithLabel: false,
                   show: false,
               },
                axisLabel: {
                    formatter: '{value}%',
                    color:'rgb(255,255,255,.5)',
                    textStyle: {
                        fontSize: 10,
                        fontWeight:'lighter'
                    },
                },
                axisLine: {
                    lineStyle: {
                        color: 'rgb(255,255,255,.5)',//纵坐标轴和字体颜色
                        width: 0.5,
                        textStyle:{
                            fontSize: 10,
                            fontWeight:'lighter'
                        },
                    }
                }
            }],
            series: [{
                name: '播放量',
                type: 'bar',
                data: [],
                barWidth: '20%',
                yAxisIndex:0,
                itemStyle:{
                    normal: {
                        color: function(params) {
                            let color = ['#FF9900','#CCFFFF','#003399','#FF0033','#FFFF00',]
                            return color[params.dataIndex]
                        }
                    }
                }
            },{
                name: '点赞率',
                type: 'line',
				smooth:true,
                itemStyle:{
                    normal:{
                        color:'rgb(255,255,255,.5)',
                        lineStyle:{
                        width:1,
                        color:'rgb(19,254,154)'
                        }
                    }
                },
                yAxisIndex:1, //以右边为轴,找了好久。。。
                data: []
            }]
        };
        for(let i = 0; i < this.vsSortByPlay.length; i++){
            let item = this.vsSortByPlay[i]
            option.xAxis.data.push(item.title)
            option.series[0].data.push(item.view)
            let tuRate = ((item.like/item.view) * 100).toFixed(1)
            option.series[1].data.push(tuRate)
        }
        setTimeout(()=> EChart.setOption(option) , 500)
    }
   } 
  }
  </script>
  
  <style>
  </style>