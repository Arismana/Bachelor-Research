<template>
    <div class="info">
        <div class="title" style="height: 50px; line-height: 50px; color: rgb(255,255,240,.8); padding-left: 5px; font-size: 24px; font-weight: bolder; border-bottom: 1px solid rgb(255,255,255,.2); background: rgb(255,255,255,.1);">个人信息</div>
        <div class="name" style="top: 70px; margin-left: 20px; position: absolute;" @mouseover="showChange('username_editor')" @mouseout="hideChange('username_editor')">
          <span style="color: rgb(255,255,255,.7); font-weight: lighter; font-size: 12px;">用&nbsp;&nbsp;户&nbsp;&nbsp;名&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <span>{{ username }}</span>
          <!-- <span style="color: #1296db; display: none; margin-left: 20px;" class="editor" ref="username_editor"><img src="../assets/images/editor.png" style="display: inline-block; height: 20px; vertical-align: middle;">编辑</span> -->
        </div>
        <div class="psw" style="top: 120px; margin-left: 20px; position: absolute;"  @mouseover="showChange('psw_editor')" @mouseout="hideChange('psw_editor')">
          <span style="color: rgb(255,255,255,.7); font-weight: lighter; font-size: 12px;">密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <span class="psw_f" v-if="!showpsw" @click="showpsw = !showpsw"></span>
          <span class="psw_t" v-if="showpsw" @click="showpsw = !showpsw">{{ userInfo.password }}</span>
          <span style="color: #1296db; display: none; margin-left: 20px;" class="editor" ref="psw_editor" @click="open()"><img src="../assets/images/editor.png" style="display: inline-block; height: 20px; vertical-align: middle;">修改</span>
          <!-- <el-button type="text" @click="open">点击打开 Message Box</el-button> -->
        </div>
        <div style="top: 170px; margin-left: 20px; position: absolute;" @mouseover="showChange('gender_editor')" @mouseout="hideChange('gender_editor')">
          <span style="color: rgb(255,255,255,.7); font-weight: lighter; font-size: 12px;">
            性&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;别&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          </span>
          <span v-show="showGender">{{ userInfo.gender }}</span>
          <span v-show="!showGender">
            <input type="radio" value="男" name="type" checked style="vertical-align: middle;" v-model="sex">&nbsp;男<input type="radio" value="女" name="type" style="margin-left:20px;vertical-align: middle;" v-model="sex">&nbsp;女<input type="radio" value="保密" name="type" style="margin-left:20px;vertical-align: middle;" v-model="sex">&nbsp;保密
            <span style="margin-left: 10px; display: inline-block; height: 30px; font-size: 12px; font-weight: bolder; color: rgb(255,255,255,.8); line-height: 30px; width: 80px; text-align: center; background-color: #1296db; border-radius: 2px;" @click="changeGender()" class="confirm">确认</span>
          </span>
          <span style="color: #1296db; display: none; margin-left: 20px;" class="editor" ref="gender_editor" @click="showChange_('showGender')"><img src="../assets/images/editor.png" style="display: inline-block; height: 20px; vertical-align: middle;">编辑</span>
        </div>
        <div style="top: 220px; margin-left: 20px; position: absolute;" @mouseover="showChange('address_editor')" @mouseout="hideChange('address_editor')">
          <span style="color: rgb(255,255,255,.7); font-weight: lighter; font-size: 12px;">所在地区&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <span>{{ userInfo.location }}</span>
          <!-- <span style="color: #1296db; display: none; margin-left: 20px;" class="editor" ref="address_editor"><img src="../assets/images/editor.png" style="display: inline-block; height: 20px; vertical-align: middle;">编辑</span> -->
        </div>
        <div style="top: 270px; margin-left: 20px; position: absolute;" @mouseover="showChange('bir_editor')" @mouseout="hideChange('bir_editor')">
          <span style="color: rgb(255,255,255,.7); font-weight: lighter; font-size: 12px;">出生日期&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <span v-show="showBir">{{ userInfo.birthday }}</span>
          <span v-show="!showBir">
            <input type="number" placeholder="年(4位)" style="border: 1px solid rgb(0,0,0,.8); width: 100px; height: 30px;outline: none; padding-left: 5px; color: rgb(0,0,0,.7);" class="input_" v-model="year">-
            <input type="number" placeholder="月(2位)" style="border: 1px solid rgb(0,0,0,.8); width: 60px; height: 30px;outline: none; padding-left: 5px; color: rgb(0,0,0,.7);" class="input_" v-model="month">-
            <input type="number" placeholder="日(2位)" style="border: 1px solid rgb(0,0,0,.8); width: 60px; height: 30px;outline: none; padding-left: 5px; color: rgb(0,0,0,.7);" class="input_" v-model="day">
            <span style="margin-left: 10px; display: inline-block; height: 30px; font-size: 12px; font-weight: bolder; color: rgb(255,255,255,.8); line-height: 30px; width: 80px; text-align: center; background-color: #1296db; border-radius: 2px;" @click="changeBir()" class="confirm">确认</span>
          </span>
          <span style="color: #1296db; display: none; margin-left: 20px;" class="editor" ref="bir_editor" @click="showChange_('showBir')"><img src="../assets/images/editor.png" style="display: inline-block; height: 20px; vertical-align: middle;">编辑</span>
        </div>
        <div style="top: 320px; margin-left: 20px; position: absolute;" @mouseover="showChange('sum_editor')" @mouseout="hideChange('sum_editor')">
          <span style="color: rgb(255,255,255,.7); font-weight: lighter; font-size: 12px;">个人简介&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <span v-show="showIntro">{{ userInfo.introdution }}</span>
          <input type="text" placeholder="表达自己的个性" style="border: 1px solid rgb(0,0,0,.8); width: 200px; height: 30px;outline: none; padding-left: 5px; color: rgb(0,0,0,.7);" v-show="!showIntro" class="input_" @keyup.enter="changeIntro()" v-model="intro">
          <span style="color: #1296db; display: none; margin-left: 20px;" class="editor" ref="sum_editor" @click="showChange_('showIntro')"><img src="../assets/images/editor.png" style="display: inline-block; height: 20px; vertical-align: middle;">编辑</span>
        </div>
        <div class="regTime" style="top: 370px; margin-left: 20px; padding-bottom: 20px; position: absolute;">
          <span style="color: rgb(255,255,255,.7); font-weight: lighter; font-size: 12px;">注册时间&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          {{ userInfo.registerTime }}
        </div>
        
    </div>
</template>

<script>
import {getUserInfo,changePsw,changeGender,changeIntro,changeBir} from '@/assets/js/api'
export default {
  name: 'info',
  data(){
    return{
      showpsw:false,
      username:'',
      userInfo:{},
      sex:'男',
      showGender:true,
      showIntro:true,
      intro:'',
      showBir:true,
      year:'',
      month:'',
      day:''
    }
  },
  mounted(){
    // console.log(parseInt('04'))
    this.getUserInfo()
    this.$nextTick(()=>{
             this.getUserInfo()
     })
  },
  activated(){
    this.getUserInfo()
    this.showpsw = false
    this.showBir = true
  },
  deactivated(){
    this.showpsw = false
    this.userInfo = {}
    this.username = ''
    this.intro = ''
    this.showGender = true
    this.showIntro = true
    this.showBir = true
  },
  methods:{
    showChange(editor){
      this.$refs[editor].style.display = 'inline-block'
    },
    hideChange(editor){
      this.$refs[editor].style.display = 'none'
    },
    async getUserInfo(){
      let username = localStorage.getItem('username')
      this.username = username
      let result = await getUserInfo(username)
      this.userInfo = result
    },
    open() {
        this.$prompt('请输入新密码', '修改密码', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
        }).then(async ({ value }) => {
          if(value==null || value.length < 6 || value.length >= 12) return this.$message.error("密码长度有误")
          let result = await changePsw(this.username,value)
        if(result.state){
          this.$message.success("修改成功,请重新登录")
          localStorage.removeItem('username')
          this.$router.push({ name:'login'})
          return
        }
        this.$message.error("出错了")
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消'
          });       
        });
      },
      showChange_(tag) {
        this[tag] = !this[tag]
      },
      async changeGender(){
        let result = await changeGender(this.username,this.sex)
        if(result.state){
          this.showGender = true
          return this.$message.success("修改成功")
        }
        this.$message.error("出错了")
      },
      async changeIntro() {
        if(this.intro.length <= 0 || this.intro.length >= 20) return this.$message.error("超出字数限制")
        let result = await changeIntro(this.username,this.intro)
        if(result.state) {
          this.showIntro = true
          return this.$message.success("修改成功")
        }
        
        return this.$message.error("出错了")
      },
      async changeBir(){
        let myDate = new Date()
        let y = parseInt(myDate.getFullYear())
        let m = parseInt(myDate.getMonth()) + 1
        let d = parseInt(myDate.getDate())
        let year = parseInt(this.year)
        let mon = parseInt(this.month)
        let day = parseInt(this.day)
        if(this.year.length != 4 || this.month.length != 2 || this.day.length != 2 || year > y || (year==y&&mon>m) || (year==y&&mon==m&&day>d) || mon>12 || day>31 || (mon==2&&day>29) || ((mon==4||mon==6||mon==9||mon==11)&&day>30) || year<=0 || mon<=0 || day<=0) return this.$message.error("生日有误")
        let result = await changeBir(this.username,this.year+'-'+this.month+'-'+this.day)
        if(result.state){
          this.showBir = true
          return this.$message.success("修改成功")
        }
        this.$message.error("出错了")
      }
    }
}
</script>

<style scoped>
.info{
  position: absolute;
  width: 1400px;
  height: 700px;
  right: 20px;
  top: 20px;
  background-color: #1E2131;
  /* background-color: #1E2131; */
  color: rgb(250,250,240,.5);
}
.psw_f{
  display: inline-block;
  height: 20px;
  width: 100px;
  background-color: #ccc;
  vertical-align:middle;
}
.editor:hover{
  cursor: pointer;
}
.confirm:hover{
  cursor: pointer;
}
.input_::placeholder {
  color: #999;
  font-family: Arial, sans-serif;
  font-size: 14px;
}
</style>