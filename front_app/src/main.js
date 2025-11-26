import Vue from 'vue'
import App from './App.vue'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import vue_router from 'vue-router'
import router from "@/assets/js/router";

import echarts from 'echarts'
import 'animate.css'


Vue.config.productionTip = false
Vue.prototype.$echarts = echarts
Vue.use(vue_router)
Vue.use(ElementUI)


const app = new Vue({
  render: h => h(App),
  router
})

app.$mount('#app')
