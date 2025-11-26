<template>
    <div class="bar">
      <div class="leftBar">
        <div class="info iconwrap" style="height: 100px;">
          <div class="monji">welcome</div>
          <div class="img" @click="toSomewhere('info')"><img src="../assets/images/bilibili.png" alt="" style="display: inline-block; height: 40px; border-radius: 20px;"></div>
          <div class="tips" style="background: rgb(0,0,0,.2);color:rgb(255,255,255,.7); font-size: small;font-weight: light; height: 50px; width: 100px; line-height: 50px; position: absolute; margin-left: 85px; margin-top: -45px; text-align: center; border-radius: 4px; z-index: 999;">个人信息</div>
        </div>
        <div class="tools" style="border-bottom: none;">
          <div class="mianTools" style="border-bottom: 1px solid rgb(255,255,255,.3);">
            <div class="monji" style="padding-left: 20px;">Tools</div>
            <div style="margin-top: 20px;" @click="toSomewhere('video')" class="iconwrap">
              <svg t="1713427534254" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4291" width="40" height="40"><path d="M849.5 962l-675 0c-66.284 0-112.5-46.216-112.5-112.5l0-675c0-66.284 46.216-112.5 112.5-112.5l675 0c66.284 0 112.5 46.216 112.5 112.5l0 675c0 66.284-46.216 112.5-112.5 112.5zM99.5 212l0 75 150 0-72.858-182.135c-46.619 13.532-77.142 53.522-77.142 107.135zM249.5 99.5l75.001 187.5 112.481 0-74.982-187.5-112.5 0zM436.982 99.5l75.018 187.5 112.5 0-75-187.5-112.519 0zM624.5 99.5l75 187.5 112.5 0-75-187.5-112.5 0zM924.5 212c0-66.284-46.216-112.5-112.5-112.5l75.001 187.5 37.499 0 0-75zM924.5 324.5l-824.999 0 0 487.5c0 66.284 46.216 112.5 112.5 112.5l600 0c66.284 0 112.5-46.216 112.5-112.5l0-487.5zM362 437l337.5 187.5-337.5 187.5 0-374.999z" p-id="4292" fill="rgb(255,255,255,.5)"></path></svg>
              <div class="tips" style="background: rgb(0,0,0,.2);color:rgb(255,255,255,.7); font-size: small;font-weight: light; height: 50px; width: 100px; line-height: 50px; position: absolute; margin-left: 30px; margin-top: 10px; text-align: center; border-radius: 4px; z-index: 999;">视频分析</div>
            </div>
            <div style="margin-top: 20px;" class="iconwrap" @click="toSomewhere('up')">
              <svg t="1713428306742" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6600" width="40" height="40"><path d="M938.666667 917.333333H85.333333A64 64 0 0 1 21.333333 853.333333V170.666667A64 64 0 0 1 85.333333 106.666667h853.333334A64 64 0 0 1 1002.666667 170.666667v682.666666a64 64 0 0 1-64 64z m-789.333334-128h725.333334v-554.666666h-725.333334v554.666666z" fill="rgb(255,255,255,.5)" p-id="6601"></path><path d="M597.333333 746.666667a64 64 0 0 1-64-64V341.333333A64 64 0 0 1 597.333333 277.333333h85.333334c82.346667 0 149.333333 66.986667 149.333333 149.333334v42.666666c0 82.346667-66.986667 149.333333-149.333333 149.333334h-21.333334V682.666667a64 64 0 0 1-64 64z m64-256h21.333334a21.333333 21.333333 0 0 0 21.333333-21.333334v-42.666666a21.333333 21.333333 0 0 0-21.333333-21.333334h-21.333334v85.333334zM341.333333 746.666667c-82.346667 0-149.333333-66.986667-149.333333-149.333334V341.333333a64 64 0 1 1 128 0v256a21.333333 21.333333 0 0 0 42.666667 0V341.333333a64 64 0 1 1 128 0v256c0 82.346667-66.986667 149.333333-149.333334 149.333334z" fill="rgb(255,255,255,.5)" p-id="6602"></path></svg>
              <div class="tips" style="background: rgb(0,0,0,.2);color:rgb(255,255,255,.7); font-size: small;font-weight: light; height: 50px; width: 100px; line-height: 50px; position: absolute; margin-left: 30px; margin-top: 10px; text-align: center; border-radius: 4px; z-index: 999;">up主分析</div>
            </div>
            <div style="margin-top: 20px;" class="iconwrap" @click="toSomewhere('div')">
              <svg t="1713749796833" class="icon" viewBox="0 0 1068 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5165" width="40" height="40"><path d="M534.26087 93.094957c102.578087 0 186.501565 83.789913 186.501565 186.189913 0 102.4-83.923478 186.167652-186.501565 186.167652-102.578087 0-186.501565-83.767652-186.501566-186.167652S431.682783 93.094957 534.26087 93.094957z m0-58.189914c-135.212522 0-244.780522 109.389913-244.780522 244.379827 0 134.967652 109.568 244.357565 244.780522 244.357565 135.212522 0 244.780522-109.389913 244.780521-244.357565 0-134.989913-109.568-244.379826-244.780521-244.379827zM266.150957 558.547478c102.578087 0 186.501565 83.789913 186.501565 186.189913 0 102.4-83.923478 186.167652-186.501565 186.167652-102.578087 0-186.501565-83.767652-186.501566-186.167652s83.923478-186.189913 186.501566-186.189913z m0-58.189913C130.938435 500.357565 21.370435 609.769739 21.370435 744.759652c0 134.967652 109.568 244.357565 244.780522 244.357565 135.234783 0 244.802783-109.389913 244.802782-244.357565 0-134.989913-109.568-244.357565-244.802782-244.357565z m536.219826 58.189913c102.578087 0 186.501565 83.789913 186.501565 186.189913 0 102.4-83.923478 186.167652-186.501565 186.167652-102.578087 0-186.523826-83.767652-186.523826-186.167652s83.923478-186.189913 186.523826-186.189913z m0-58.189913c-135.234783 0-244.802783 109.389913-244.802783 244.379826 0 134.967652 109.568 244.357565 244.802783 244.357566 135.212522 0 244.780522-109.389913 244.780521-244.357566 0-134.989913-109.568-244.357565-244.780521-244.357565z" fill="rgb(255,255,255,.5)" p-id="5166"></path></svg>
              <!-- <svg t="1713428878133" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="7765" width="40" height="40"><path d="M800 128H224C134.4 128 64 198.4 64 288v448c0 89.6 70.4 160 160 160h576c89.6 0 160-70.4 160-160V288c0-89.6-70.4-160-160-160z m96 608c0 54.4-41.6 96-96 96H224c-54.4 0-96-41.6-96-96V288c0-54.4 41.6-96 96-96h576c54.4 0 96 41.6 96 96v448z" p-id="7766" fill="rgb(255,255,255,.5)"></path><path d="M240 384h64v64h-64zM368 384h384v64h-384zM432 576h352v64h-352zM304 576h64v64h-64z" p-id="7767" fill="rgb(255,255,255,.5)"></path></svg> -->
              <div class="tips" style="background: rgb(0,0,0,.2);color:rgb(255,255,255,.7); font-size: small;font-weight: light; height: 50px; width: 100px; line-height: 50px; position: absolute; margin-left: 30px; margin-top: 10px; text-align: center; border-radius: 4px; z-index: 999;">分区分析</div>
            </div>
            <div style="margin-top: 20px; padding-bottom: 20px;" class="iconwrap" @click="toSomewhere('suisan')">
              <svg t="1715481609953" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4297" width="40" height="40"><path d="M344.3 928.4H832c30.8 0 55.7-24.7 55.7-55.4v-69.3c23.1 0 41.8-18.6 41.8-41.6V429.6c0-30.6-25-55.4-55.7-55.4H655.3c1.6-50.1-1.2-148.7-42.8-207-27.5-38.5-76.6-64.6-76.6-64.6-28.8-10.7-70.8 5.4-70.8 36 0 0 14.4 106.4-24 171.5-16.8 28.3-37.2 49.3-55 64.1H149.3c-30.8 0-55.8 24.8-55.8 55.4V873c0 30.7 24.9 55.4 55.8 55.4h195z m0-498.8V873H197.5c-26.7 0-48.3-19.8-48.3-44.4V473.9c0-24.5 21.6-44.3 48.3-44.3h146.8z m376.2 110.8c0 15.3 12.5 27.7 27.9 27.7h125.4v69.4H748.4c-15.4 0-27.9 12.3-27.9 27.8 0 15.2 12.5 27.7 27.9 27.7h125.4v55.5H748.4c-15.4 0-27.9 12.3-27.9 27.6s12.5 27.8 27.9 27.8H832v24.9c0 24.7-21.7 44.5-48.4 44.5H400V429.4c7.1-4.5 71.8-64.4 78.4-74.3 40.9-61.5 41.8-165.4 41.8-165.4 0-30.6-3.6-30.7 25.3-20 0 0 54.6 84 49.4 204.5-0.5 10.4-0.1 28.3 5 38.1 6.6 12.5 13.4 17.3 44.1 17.3h181.4c26.7 0 48.3 19.9 48.3 44.3v38.9H748.3c-15.3-0.2-27.8 12.4-27.8 27.6zM218.9 762c0 15.4 12.5 27.8 27.9 27.8 15.4 0 27.9-12.3 27.9-27.8 0-15.3-12.4-27.7-27.9-27.7-15.4 0.1-27.9 12.4-27.9 27.7z m0 0" p-id="4298" fill="rgb(255,255,255,.5)"></path></svg>
              <div class="tips" style="background: rgb(0,0,0,.2);color:rgb(255,255,255,.7); font-size: small;font-weight: light; height: 50px; width: 100px; line-height: 50px; position: absolute; margin-left: 30px; margin-top: 10px; text-align: center; border-radius: 4px; z-index: 999;">猜您喜欢</div>
            </div>
          </div>
          <div class="others">
            <div class="monji" style="padding-left: 15px; margin-top: 20px;">Others</div>
            <div style="margin-top: 15px; margin-left: 2px;" class="iconwrap" @click="toSomewhere('history')">
              <svg t="1713429242675" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="8789" width="40" height="40"><path d="M480 0C214.9 0 0 214.9 0 480s214.9 480 480 480 480-214.9 480-480S745.1 0 480 0z m0 896C250.6 896 64 709.4 64 480S250.6 64 480 64s416 186.6 416 416-186.6 416-416 416z" fill="rgb(255,255,255,.5)" p-id="8790"></path><path d="M512 192h-64v320h320v-64H512z" fill="rgb(255,255,255,.5)" p-id="8791"></path></svg>
              <div class="tips" style="background: rgb(0,0,0,.2);color:rgb(255,255,255,.7); font-size: small;font-weight: light; height: 50px; width: 100px; line-height: 50px; position: absolute; margin-left: 30px; margin-top: 10px; text-align: center; border-radius: 4px; z-index: 999;">历史记录</div>
            </div>
            <div style="margin-top: 10px;" @click="toSomewhere('login')" class="iconwrap">
              <svg t="1713429804764" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="9795" width="40" height="40"><path d="M814 65.9H265.7c-80.5 0-146 65.5-146 146V320c0 19.9 16.1 36 36 36s36-16.1 36-36V211.9c0-40.8 33.2-74 74-74H814c40.8 0 74 33.2 74 74v602.6c0 40.8-33.2 74-74 74H265.7c-40.8 0-74-33.2-74-74V704.2c0-19.9-16.1-36-36-36s-36 16.1-36 36v110.3c0 80.5 65.5 146 146 146H814c80.5 0 146-65.5 146-146V211.9c0-80.5-65.5-146-146-146z" p-id="9796" fill="rgb(255,255,255,.5)"></path><path d="M549.7 680.5c-13.5 14.6-12.6 37.4 2 50.9 6.9 6.4 15.7 9.6 24.4 9.6 9.7 0 19.4-3.9 26.5-11.6l177.4-192c6.5-7 9.6-15.9 9.5-24.8 0.1-8.8-3.1-17.7-9.5-24.8l-177.4-192c-13.5-14.6-36.3-15.5-50.9-2-14.6 13.5-15.5 36.3-2 50.9l121.6 131.6H100c-19.9 0-36 16.1-36 36s16.1 36 36 36h571.8L549.7 680.5z" p-id="9797" fill="rgb(255,255,255,.5)"></path></svg>
              <div class="tips" style="background: rgb(0,0,0,.2);color:rgb(255,255,255,.7); font-size: small;font-weight: light; height: 50px; width: 100px; line-height: 50px; position: absolute; margin-left: 30px; margin-top: 10px; text-align: center; border-radius: 4px; z-index: 999;">退出登录</div>
            </div>
          </div>
        </div>
      </div>

    </div>
</template>

<script>
export default {
  name: 'bar',
  props: {},
  methods:{
    toSomewhere(next){
      if(this.$route.name != next){
        if(next == 'login'){
        localStorage.removeItem('username')
        this.$emit('logout')
        this.$message.success("退出成功")
      }
      this.$router.push({ name:next})
      }
    },
  }
}
</script>


<style scoped>
.leftBar{
  position: absolute;
  width: 100px;
  height: 700px;
  margin-left: 10px;
  margin-top: 20px;
  background: rgba(0, 0, 0, 0.2);
}
.info,.tools{
  width: 70px;
  margin-left: 15px;
  margin-top: 20px;
  border-bottom: 1px solid rgb(255,255,255,.3);
}
.monji{
  font-size: 14px;
  font-weight: light;
  color: rgb(255,255,255,.5);
  padding-left: 8px;
  margin-top: 10px;
}
.img{
  margin-left: 15px;
  margin-top: 15px;
  transition: all .4s;
}
.icon{
  margin-left: 15px;
  margin-top: 15px;
  transition: all .4s;
}

.info:hover{
  cursor: pointer;
}

.info .img:hover{
  transform: scale(1.2);
}

.icon:hover{
  cursor: pointer;
  transform: scale(1.2);
}
.icon:hover path{
  fill: rgb(255,255,255,.8);
}

.tips{
  display: none;
}

.iconwrap:hover .tips{
  display: inline-block;
}
</style>