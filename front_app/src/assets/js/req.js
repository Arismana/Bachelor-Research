//重写axios
import axios from "axios"
import nprogress from 'nprogress' // 引入进度条
import 'nprogress/nprogress.css' //引入进度条样式

//console.log(nprogress) //nprogress对象中含有 start done 等方法

const req = axios.create({
    baseURL:'/api',
    timeout:120000
})

//配置请求拦截器
req.interceptors.request.use(config => {
    nprogress.start()
    config.headers = {}
    return config
})
//配置响应拦截器
req.interceptors.response.use(
    res => {
        nprogress.done()
        return res.data
    },
    err => {
        return Promise.reject(new Error(err.message))
    }
)

export default req