<template>
    <div class="rank">
        <div id="EChart_ddz" style="height: 260px; width:100%;"></div>
    </div>
</template>

<script>
export default {
  name: 'ddz',
  props: {
    vArr:{},
    allDivInfo:{}
  },
  data(){
    return{
        divRank:[]
    }
  },
  mounted(){
    setTimeout(()=>{
        this.getData()
        this.getRenderer()
    },500)
  },
  methods:{
    getRenderer() {
      let EChart = this.$echarts.init(document.getElementById("EChart_ddz"))
     let option = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      // Use axis to trigger tooltip
      type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
    }
  },
  legend: {
    x:'left',
    orient : 'vertical',
    textStyle:{
          color:"white",
          fontWeight:'light'
    },
  },
  grid: {
    top:'3%',
    left:'15%',
    right: '3%',
    bottom: '3%',
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
    data: [this.divRank[0].tname, this.divRank[1].tname, this.divRank[2].tname, this.divRank[3].tname, this.divRank[4].tname],
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
      name: '~50w',
      type: 'bar',
      barWidth: '50%',
      stack: 'total',
      itemStyle:{
                    normal: {
                        color: '#8129DD'
                    }
                },
      label: {
        show: true,
        position: 'insideBottom',
    	formatter: function(params) {
	 		const a = params.value[params.encode.y[0]]
    		if (a > 0) {
				return a
			} else {
				return ''
			}
		}
      },
      emphasis: {
        focus: 'series'
      },
      data: [this.getNum(this.divRank[0].arr,1),this.getNum(this.divRank[1].arr,1), this.getNum(this.divRank[2].arr,1),
      this.getNum(this.divRank[3].arr,1), this.getNum(this.divRank[4].arr,1)]
    },
    {
      name: '50~75w',
      type: 'bar',
      barWidth: '50%',
      stack: 'total',
      label: {
        show: true,
        position: 'insideBottom',
    	formatter: function(params) {
	 		const a = params.value[params.encode.y[0]]
    		if (a > 0) {
				return a
			} else {
				return ''
			}
		}
      },
      itemStyle:{
                    normal: {
                        color: '#8EC63F'
                    }
                },
      emphasis: {
        focus: 'series'
      },
      data: [this.getNum(this.divRank[0].arr,2), this.getNum(this.divRank[1].arr,2), this.getNum(this.divRank[2].arr,2), 
      this.getNum(this.divRank[3].arr,2),this.getNum(this.divRank[4].arr,2)]
    },
    {
      name: '75~100w',
      type: 'bar',
      barWidth: '50%',
      stack: 'total',
      itemStyle:{
                    normal: {
                        color: '#2756CA'
                    }
                },
                label: {
        show: true,
        position: 'insideBottom',
    	formatter: function(params) {
	 		const a = params.value[params.encode.y[0]]
    		if (a > 0) {
				return a
			} else {
				return ''
			}
		}
      },
      emphasis: {
        focus: 'series'
      },
      data: [this.getNum(this.divRank[0].arr,3), this.getNum(this.divRank[1].arr,3), this.getNum(this.divRank[2].arr,3), 
      this.getNum(this.divRank[3].arr,3),this.getNum(this.divRank[4].arr,3)]
    },
    {
      name: '100~150w',
      type: 'bar',
      barWidth: '50%',
      stack: 'total',
      itemStyle:{
                    normal: {
                        color: '#F1B601'
                    }
                },
                label: {
        show: true,
        position: 'insideBottom',
    	formatter: function(params) {
	 		const a = params.value[params.encode.y[0]]
    		if (a > 0) {
				return a
			} else {
				return ''
			}
		}
      },
      emphasis: {
        focus: 'series'
      },
      data: [this.getNum(this.divRank[0].arr,4), this.getNum(this.divRank[1].arr,4), this.getNum(this.divRank[2].arr,4), 
      this.getNum(this.divRank[3].arr,4),this.getNum(this.divRank[4].arr,4)]
    },
    {
      name: '150~200w',
      type: 'bar',
      barWidth: '50%',
      stack: 'total',
      itemStyle:{
                    normal: {
                        color: '#F86423'
                    }
                },
                label: {
        show: true,
        position: 'insideBottom',
    	formatter: function(params) {
	 		const a = params.value[params.encode.y[0]]
    		if (a > 0) {
				return a
			} else {
				return ''
			}
		}
      },
      emphasis: {
        focus: 'series'
      },
      data: [this.getNum(this.divRank[0].arr,5), this.getNum(this.divRank[1].arr,5), this.getNum(this.divRank[2].arr,5), 
      this.getNum(this.divRank[3].arr,5),this.getNum(this.divRank[4].arr,5)]
    },
    {
      name: '200w+',
      type: 'bar',
      stack: 'total',
      barWidth: '50%',
      label: {
        show: true,
        position: 'insideBottom',
    	formatter: function(params) {
	 		const a = params.value[params.encode.y[0]]
    		if (a > 0) {
				return a
			} else {
				return ''
			}
		}
      },
      itemStyle:{
                    normal: {
                        color: '#27AAE3'
                    }
                },
      emphasis: {
        focus: 'series'
      },
      data: [this.getNum(this.divRank[0].arr,6), this.getNum(this.divRank[1].arr,6), this.getNum(this.divRank[2].arr,6), 
      this.getNum(this.divRank[3].arr,6),this.getNum(this.divRank[4].arr,6)]
    }
  ]
};
setTimeout(()=>{
    EChart.setOption(option);
},500)
    },
    getData(){
        let divArr = []
        let i = 0
        for(i;i<this.allDivInfo.varr.length;i++){
            let tname = this.allDivInfo.varr[i].tname
            let play = this.allDivInfo.varr[i].playData.view
            let j = 0
            for(j;j<divArr.length;j++){
                if(divArr[j].tname == tname){
                    divArr[j].num++
                    divArr[j].arr.push(play)
                    break
                }
            }
            if(j >= divArr.length){
                let obj = {
                    'tname':tname,
                    'num':1,
                    'arr':[play]
                }
                divArr.push(obj)
            }
        }
        divArr.sort((a,b) => b.num - a.num)
        this.divRank = divArr
    },
    getNum(arr,tag){
        switch (tag) {
            case 1:
                return this.getNum_(0,500000,arr)
            case 2:
                return this.getNum_(500000,750000,arr)
            case 3:
                return this.getNum_(750000,1000000,arr)
            case 4:
                return this.getNum_(1000000,1500000,arr)
            case 5:
                return this.getNum_(1500000,2000000,arr)
            case 6:
                return this.getNum_(2000000,9999999999,arr)
        }
    },
    getNum_(min,max,arr){
        let num = 0
        let i = 0
        for(i;i<arr.length;i++){
            if(arr[i] >= min && arr[i] < max) num++
        }
        return num
    }
  }
}
</script>