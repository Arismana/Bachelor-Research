<template>
    <div id="zzt">
      <div id="EChart_1" style="width: 500px; height: 230px; padding: 10px;"></div>
    </div>
  </template>
  
  <script>
  
  export default {
    name: 'zzt',
    components: {},
    data(){
        return{
            vsSortByPlay:[]
        }
    },
    props:{
        allNums:{},
        allRates:{}
    },
    mounted(){
        setTimeout(()=> this.getRenderer() , 500)
    },
   methods:{
    getRenderer() {
      let EChart = this.$echarts.init(document.getElementById("EChart_1"));
      var option = {
        title : {
        text: '视频数据',
        // subtext: '纯属虚构',
        x:'center',
        textStyle:{
          color:"white",
          fontWeight:'bolder'
        },
    },
    grid:{
		y:100,
	},
            tooltip: {
				        trigger:'axis',
				        // formatter: '{b0}({a0}): {c0}<br />{b1}({a1}): {c1}%'
			      },
            legend: {
              orient : 'vertical',
              x : 'left',
              data:["视频数据","比率数据"],
              textStyle:{
                 color:"white",
                 fontWeight:'light'
              },
            },
            xAxis: {
                type:'category',
                data: ["点赞量","投币量","收藏量","转发量","弹幕量","重播量"],
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
            yAxis: [{
                type: 'value',
                name: '次数',
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
                axisTick: {
                   alignWithLabel: false,
                   show: false,
               },
               splitLine:{
                show:false
               },
               show:true,
                axisLabel: {
                    formatter: (value) => {
                        return value*100 + '%'
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: 'white',//纵坐标轴和字体颜色
                        width: 2
                    }
                }
            }],
            series: [{
                name: '视频数据',
                type: 'bar',
				barWidth : '50%',
                data: [this.allNums.like,
                this.allNums.coin,
                this.allNums.favorite,
                this.allNums.share,
                this.allNums.danmaku,
                this.allNums.reply
            ],
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
                name: '比率数据',
                type: 'line',
				smooth:true,
                yAxisIndex:1, //以右边为轴,找了好久。。。
                data: [this.allRates.likeRate,this.allRates.coinRate,this.allRates.favoRate,this.allRates.shareRate,this.allRates.danmuRate,this.allRates.replyRate]
            }]
        };
        setTimeout(()=> EChart.setOption(option) , 1000)
    }
   } 
  }
  </script>