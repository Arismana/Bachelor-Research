import VueRouter from "vue-router"

import Login from '@/components/Login.vue'
import register from '@/components/register.vue'
import main from '@/components/main.vue'
import up from '@/components/up.vue'
import video from '@/components/video.vue'
import info from '@/components/info.vue'
import history from '@/components/history.vue'
import div from '@/components/divisions.vue'
import suisan from '@/components/suisan.vue'

const router = new VueRouter({
    routes:[
        {
            name:'login',
            path:'/login',
            component:Login,
            meta:{
                index:1
            }
        },
        {
            name:'register',
            path:'/register',
            component:register,
            meta:{
                index:2
            }
        },
        {
            name:'main',
            path:'/main',
            component:main,
            meta:{
                index:3
            }
        },
        {
            name:'up',
            path:'/up',
            component:up,
            meta:{
                index:5
            }
        },
        {
            name:'video',
            path:'/video',
            component:video,
            meta:{
                index:4
            }
        },
        {
            name:'info',
            path:'/info',
            component:info,
            meta:{
                index:6
            }
        },
        {
            name:'history',
            path:'/history',
            component:history,
            meta:{
                index:7
            }
        },
        {
            name:'div',
            path:'/div',
            component:div
        },
        {
            name:'suisan',
            path:'/suisan',
            component:suisan
        },
        {
            path:'*',
            redirect:'/login' //重定向到home路由页
        }
    ],
    scrollBehavior() { //控制路由跳转之后，来到新页面的位置
        return {y:0} //呈现页面顶部
    }
})

export default router