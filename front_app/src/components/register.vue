<template>
    <div class="register">
      <h1>Register</h1>
      <input type="text" placeholder="account" class="firIpt" v-model="username"> <br>
      <input type="password" placeholder="password" v-model="password"> <br>
      <input type="password" placeholder="confirm your pw" v-model="pwa" @keyup.enter="register()"> 
      <span style="font-size: 14px; font-weight: bolder; color: rebeccapurple; display: inline-block; margin-left: 25px;" v-show="password != pwa">
        <img src="../assets/images/warning.png" style="display: inline-block; height: 20px; vertical-align:bottom">密码不一致!
      </span><br>
        <button @click="register()">GO</button>
      <p>To&nbsp;&nbsp;<a @click="toSomewhere('login')">Login</a>&nbsp;</p>
    </div>
  </template>
  
  <script>
  import {register} from '@/assets/js/api'
  export default {
    name: 'register',
    data(){
      return{
        username:'',
        password:"",
        pwa:""
      }
    },
    props: {},
    methods:{
      async register(){
        if(this.username.length == 0 || this.username.length >10){
          this.$message.error("用户名长度有误")
          return
        }
        if(this.password.length < 6 || this.password.length >= 12){
          this.$message.error("密码长度有误")
          return
        }
        if(this.password != this.pwa){
          this.$message.error("两次密码不同")
          return
        }
        let result = await register(this.username,this.password)
        if(result == 1){
          this.$message.success("注册成功")
          setTimeout(()=>this.toSomewhere('login'),1000)
        }
        else this.$message.error("用户名已存在")
      },
      toSomewhere(next){
        this.$router.push({ name:next})
      }
    }
  }
  </script>
  
  <style scoped>
  .register{
        position: absolute;
        width: 800px;
        height: 400px;
        opacity: .7;
        left: 50%;
        top: 50%;
        margin-left: -400px;
        margin-top: -200px;
        border-radius: 10px;
        padding-top: 1px;
        background-color: #0c1622;
      }
      h1{
          margin: 0 auto;
          margin-top: 40px;
          color: rgb(255,255,255,.8);
          width: 130px;
      }
      input{
          background: none;
          width: 400px;
          border:none;
          outline: none;
          border-bottom: 2px solid rgb(199, 191, 219);
          padding-bottom: 2px;
          margin-top: 25px;
          font-size: 16px;
          font-weight: bold;
          color: rgb(255,255,255,.8);
          margin-left: 220px;
      }
        ::-webkit-input-placeholder{
            color: rgb(255,255,255,.2);
            font-size: 14px;
        }
      .firIpt{
          margin-top: 30px;
      }
      button{
          width: 100px;
          height: 100px;
          margin-left: 44%;
          background-color: rgb(0,0,0,.5);
          opacity: .8;
          color: rgb(255,255,255,.8);;
          font-size: 14px;
          font-weight: bolder;
          margin-top: 40px;
          border-radius: 50px;
          border: none;
      }
      button:hover{
          cursor: pointer;
      }
      p{
          width: 115px;
          position: absolute;
          bottom: 30px;
          right: 15px;
          font-size: 20px;
          color: white;
      }
      p:hover{
        cursor: pointer;
      }
      p a{
          text-decoration: none;
          color: #00A4FF;
      }
      .icon{
          position: absolute;
          height: 80px;
          top: -30px;
          left: -30px;
      }   
  </style>
  