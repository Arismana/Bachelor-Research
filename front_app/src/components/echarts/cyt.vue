<template>
    <div class="cyt">
            <div ref="chart1" style="width: 388px;height:250px;"></div>
    </div>
  </template>
   
  <script>
  import 'echarts-wordcloud'
  export default {
    name: "cyt",
    data() {
      return {
        handledVDK:[]
      }
    },
    props:{
      videoFeedBackCiyun:[]
    },
    mounted() {
      setTimeout(() => {
        this.danmuHandle()
        this.showEeharts()
      },1000)
    },
    methods: {
      danmuHandle(){
        for(let i = 0; i < this.videoFeedBackCiyun.length; i++){
          let o = {'name':this.videoFeedBackCiyun[i][0],'value':this.videoFeedBackCiyun[i][1]}
          this.handledVDK[i] = o
        }
      },
      showEeharts() {
        let chart1 = this.$echarts.init(this.$refs.chart1)
        const colorList = [
          '#FF34B3','#FF1493', '#FF4500','#FFFF00',
         '#FFE384','#F0FFFF','#F5F5F5','#7FFFD4','#7FFF00',
         '#FF6103','#87CEEB','#7FFF00','#C0C0C0','#FFF5EE','#F0FFFF','#CAFF70','#FFC1C1','#FFB6C1','#FF00FF',
         '#FFE1FF','#9B30FF','#FF3E96','#FFF0F5','#F0FFF0','#FFFFF0']
            let chartOption = {
            title: {
                text: '',
            },
            backgroundColor: 'rgba(0, 0, 0, 0.1)', //F7F7F7
            tooltip: {
                show: true
            },
            series: [{
                name: '关键词权重',//数据提示窗标题
                type: 'wordCloud',
                sizeRange: [8, 35],//画布范围，如果设置太大会出现少词（溢出屏幕）
                rotationRange: [-45, 90],//数据翻转范围
                //shape: 'circle',
                textPadding: 0,
                autoSize: {
                    enable: true,
                    minSize: 6
                },
                textStyle: {
                    normal: {
                        color: function() {
                          let index = Math.floor(Math.random() * colorList.length)
                          return colorList[index]
                        }
                    },
                    emphasis: {
                        shadowBlur: 10,
                        shadowColor: 'white'
                    }
                },
                data: this.handledVDK,
            }]
        };
        chart1.setOption(chartOption);
      },
    },
  };
  </script>