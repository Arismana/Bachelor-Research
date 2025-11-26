<template>
    <div id="zaz">
      <div id="EChart_1" style="width: 700px; height: 250px;"></div>
    </div>
  </template>
  
  <script>
  
  export default {
    name: 'zaz',
    components: {},
    data(){
        return{
            vsSortByPlay:[]
        }
    },
    props:{
        videoInfo:{}
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
            videoData[i] = this.videoInfo[i].cnt_info
            videoData[i].title = this.videoInfo[i].title
        }
        videoData.sort((a,b) => b.play - a.play)
        this.vsSortByPlay = videoData.slice(0,5)
    },
    getRenderer() {
      let EChart = this.$echarts.init(document.getElementById("EChart_1"));
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
                        color: 'white',
                        width: 2
                    }
                },
                axisLabel:{
                    color:'white',
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
                name: '播放量',
                axisTick: {
                   alignWithLabel: false,
                   show: false,
               },
               show:true,
               axisLine: {
                    lineStyle: {
                        color: '#ccc',
                        width: 2
                    }
                }
            },{
                type: 'value',
                name: '比率',
                min: 0.0,
                max: 20.0,
                interval: 5.0,
                splitLine:{
                show:false
               },
                axisTick: {
                   alignWithLabel: false,
                   show: false,
               },
                axisLabel: {
                    formatter: '{value}%'
                },
                axisLine: {
                    lineStyle: {
                        color: 'white',//纵坐标轴和字体颜色
                        width: 2
                    }
                }
            }],
            series: [{
                name: '播放量',
                type: 'bar',
				barWidth : '50%',
                data: [],
                yAxisIndex:0,
                itemStyle:{
                  normal: {
                color: function(params) {
                	//注意，如果颜色太少的话，后面颜色不会自动循环，最好多定义几个颜色
                    let color = ['#FF0033','#FFFF00','#003399','#CCFFFF','#FF9900']
                    return color[params.dataIndex]
                }
            }
                }
            },{
                name: '点赞率',
                type: 'line',
				smooth:true,
                yAxisIndex:1, //以右边为轴,找了好久。。。
                data: []
            }]
        };
        for(let i = 0; i < this.vsSortByPlay.length; i++){
            let item = this.vsSortByPlay[i]
            option.xAxis.data.push(item.title)
            option.series[0].data.push(item.play)
            let tuRate = ((item.thumb_up/item.play) * 100).toFixed(1)
            option.series[1].data.push(tuRate)
        }
        setTimeout(()=> EChart.setOption(option) , 500)
    }
   } 
  }
  </script>
  
  <style>
  </style>