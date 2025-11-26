<template>
  <div class="login">
    <h1>Login</h1>
    <input type="text" placeholder="account" class="firIpt" v-model="username"> <br>
    <input type="password" placeholder="password" v-model="password" @keyup.enter="login()"> <br>
    <button @click="login()">GO</button>
    <p>To&nbsp;&nbsp;<span @click="toSomewhere('register')" class="toReg" @mouseenter="tixing()" ref="toReg">Register</span>&nbsp;</p>
  </div>
</template>

<script>
import {login} from '@/assets/js/api'
export default {
  name: 'Login',
  data(){
    return{
      username:'',
      password:''
    }
  },
  methods:{
    async login(){
      let result = await login(this.username,this.password)
      if(result){
        this.$message.success("登录成功")
        localStorage.setItem('username',this.username)
        setTimeout(()=>this.toSomewhere('info'),1000)
      }
      else this.$message.error("登录信息有误")
    },
    toSomewhere(next){
      this.$router.push({ name:next})
    },
    tixing(){
      this.$refs.toReg.className = 'toReg animate__animated animate__heartBeat'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login{
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
        color: white;
        width: 90px;
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
        color:blanchedalmond;
        margin-left: 220px;
    }
      ::-webkit-input-placeholder{
          color: #CCCCCC;
          font-size: 14px;
      }
    .firIpt{
        margin-top: 50px;
    }
    button{
        width: 100px;
        height: 100px;
        margin-left: 44%;
        background-color: black;
        opacity: .8;
        color: white;
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
        bottom: 15px;
        right: 15px;
        font-size: 20px;
        color: white;
    }
    p .toReg{
        color: #00A4FF;
        display: inline-block;
    }
    /* img{
        position: absolute;
        height: 100px;
        top: -40px;
        left: -35px;
    } */
    p .toReg:hover{
      cursor: pointer;
    }
</style>
