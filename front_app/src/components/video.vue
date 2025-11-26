<template>
    <div id="video">
		<div class="searchWrapper" ref="searchWrapper" v-if="searchShow">
			<div class="title" style="height: 50px; line-height: 50px; color: rgb(255,255,240,.8); padding-left: 5px; font-size: 24px; font-weight: bolder; border-bottom: 1px solid rgb(255,255,255,.2); background: rgb(255,255,255,.1);">视频分析</div>
            <div ref="video_search">
       			<div class="wrapper">
	    			<div class="input-data">
		   				<input type="text" required="" style="background-color: #D2D3D6;" @keyup.enter="getVInfo()" v-model="bvid"/>
						<div class="underline"></div>
						<label>BV</label>
	    			</div>
      			</div>
        	</div>
		</div>
		<div ref="loading" style="margin-left: 650px; margin-top: 250px;" v-if="loadingShow">
			<loading></loading>
		</div>
		<div ref="videoInfo" style="color: white;" v-if="vDataShow">
			<svg t="1713617450379" @click="back()" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="8525" width="30" height="30"><path d="M511.347131 65.214281c-246.678192 0-446.650643 199.972451-446.650643 446.650643s199.972451 446.650643 446.650643 446.650643 446.650643-199.972451 446.650643-446.650643S758.025323 65.214281 511.347131 65.214281zM510.744403 894.491391c-211.92262 0-383.720382-171.797761-383.720382-383.720382s171.797761-383.720382 383.720382-383.720382 383.720382 171.797761 383.720382 383.720382S722.667024 894.491391 510.744403 894.491391zM502.173191 708.726523c8.139378 8.138354 8.139378 21.332864 0 29.471219l0 0c-8.138354 8.139378-21.332864 8.139378-29.471219 0L261.234723 526.730493c-8.139378-8.138354-8.139378-21.331841 0-29.471219l0 0c8.138354-8.138354 21.332864-8.138354 29.471219 0L502.173191 708.726523 502.173191 708.726523zM290.705941 526.470573c-8.138354 8.139378-21.332864 8.139378-29.471219 0l0 0c-8.139378-8.138354-8.139378-21.331841 0-29.471219l211.467249-211.467249c8.138354-8.138354 21.332864-8.138354 29.471219 0l0 0c8.139378 8.139378 8.139378 21.332864 0 29.472242L290.705941 526.470573 290.705941 526.470573zM290.705941 526.470573M737.565339 483.569484c15.624862-0.010233 28.296463 12.648065 28.304649 28.271904l0 0c0.010233 15.623839-12.648065 28.296463-28.271904 28.304649l-405.963988 0.233314c-15.623839 0.010233-28.29544-12.647041-28.304649-28.271904l0 0c-0.00921-15.623839 12.649088-28.29544 28.271904-28.304649L737.565339 483.569484 737.565339 483.569484z" fill="rgb(255,255,255,.5)" p-id="8526"></path></svg>
			<vd 
			  :vBasicInfo="vBasicInfo" 
			  :videoFeedBackCiyun="videoFeedBackCiyun" 
			  :danmuScore="danmuScore" 
			  :pinglunScore="pinglunScore"
			  :danmuQxzb="danmuQxzb"
			  :commentsQxzb="commentsQxzb"
			  >
			</vd>
		</div>
    </div>
  </template>
  
  <script>
  import vd from './vKuwashii.vue';
  import loading from './loading.vue';
  import {getVideoBasicInfo} from '@/assets/js/api'
  export default {
    name: 'video',
    components: {vd,loading},
    data(){
        return{
            bvid:'',
            vBasicInfo:{},
            videoFeedBackCiyun:[],
			danmuScore:0,
			pinglunScore:0,
			danmuQxzb:{},
			commentsQxzb:{},
			searchShow:true,
			loadingShow:false,
			vDataShow:false
        }
    },
    methods:{
        async getVInfo(){
			this.searchShow = false
			this.loadingShow = true
			let username = localStorage.getItem('username')
		    let result = await getVideoBasicInfo(this.bvid,username)
			if(result.result == 0) {
				this.loadingShow = false
				this.searchShow = true
				return this.$message.warning("bvid格式错误")
			}
			else if(result.result == 2){
				this.loadingShow = false
				this.searchShow = true
				return this.$message.info("啥也木搜到")
			}
			else if(result.result == 3){
				this.loadingShow = false
				this.searchShow = true
				return this.$message.error("啊哦，出错了")
			}
			let data = result.data
		    this.vBasicInfo = data.videoBasicInfo
            this.videoFeedBackCiyun = data.videoFeedBackCiyun.vFeedBackKws
			this.danmuQxzb = data.videoFeedBackCiyun.danmuAz.danmuQxtj
			this.commentsQxzb = data.videoFeedBackCiyun.pinglunAz.commentsQxtj
			this.danmuScore = data.videoFeedBackCiyun.danmuAz.danmuScore
			this.pinglunScore = data.videoFeedBackCiyun.pinglunAz.pinglunScore
            this.showResult()
        },
        showResult(){
			setTimeout(()=>{
				this.loadingShow = false
				this.vDataShow = true
			},1500)
        },
        toSomewhere(next){
            this.$router.push({ name:next})
        },
        back(){
			this.vDataShow = false,
		    this.searchShow = true
	    },
		deactivated(){
    	this.searchShow = true
    	this.loadingShow = false
    	this.vDataShow = false
   		this.bvid = ''
 	 }
    }
  }
  </script>
  
  <style scoped>
  #video{
	position: absolute;
    width: 1400px;
    height: 700px;
    right: 20px;
    top: 20px;
	background-color: #1E2131;
	z-index: 0;
  }
.wrapper{
	width: 450px;
	padding: 30px;
    margin: 50px auto;
	box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
	border-radius: 5px;
	background: rgb(255, 255, 255,.8);
}
.wrapper .input-data{
	width: 100%;
	height: 40px;
	position: relative;
    border: none;
    outline: none;
}
.wrapper .input-data input{
	width: 100%;
	height: 100%;
    border: none;
	border-bottom: 2px solid silver;
	color: #8B0000;
	font-size: 17px;
    outline: none;
}
.input-data input:focus ~ label,
.input-data input:valid ~ label{
	transform: translateY(-20px);
	font-size: 15px;
	color: black;
    border: none;
    outline: none;
}
.wrapper .input-data label{
	position: absolute;
	bottom: 10px;
	left: 0;
	color: grey;
	pointer-events: none;
	transition: all 0.3s ease;
}
.wrapper .input-data .underline{
	position: absolute;
	bottom: 0px;
	height: 2px;
	width: 100%;
}
.input-data .underline:before{
	position: absolute;
	content: "";
	height: 100%;
	width: 100%;
	background: black;
	transform: scaleX(0);
	transition:transform 0.3s ease;
    border: none;
    outline: none;
}

.input-data input:focus ~ .underline:before,
.input-data input:valid ~ .underline:before{
	transform: scaleX(1);
    border: none;
    outline: none;
}

.input-data input:focus{
    border: none;
}
.back{
	height: 50px;
	width: 50px;
	margin-top: 20px;
}
.back img{
	display: inline-block;
	height: 100%;
	width: 100%;
}
.back:hover{
	cursor: pointer;
}
.icon{
	margin-top: 10px;
	margin-left: 20px;
	transition: all .4s;
}
.icon:hover{
  cursor: pointer;
  transform: scale(1.2);
}
.icon:hover path{
  fill: rgb(255,255,255,.8);
}
  </style>