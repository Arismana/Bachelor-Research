<template>
    <div class="history">
      <div class="title" style="height: 50px; line-height: 50px; color: rgb(255,255,240,.8); padding-left: 5px; font-size: 24px; font-weight: bolder; border-bottom: 1px solid rgb(255,255,255,.2); background: rgb(255,255,255,.1);">搜索记录</div>
      <el-table :data="history" style="width: 100%;" :row-class-name="tableRowClassName" :header-cell-style="{background:'#999999',color:'#606266'}">
        <el-table-column prop="username" label="用户"></el-table-column>
        <el-table-column prop="type" label="内容类型"></el-table-column>
        <el-table-column prop="sid" label="搜索内容"></el-table-column>
        <el-table-column prop="time" label="时间"></el-table-column>
        <el-table-column prop="state" label="状态"></el-table-column>
      </el-table>
      <el-pagination background layout="prev, pager, next" :total="length" @current-change="handleCurrentChange">
      </el-pagination>
   </div>
</template>

<script>
import {getHistory,getHisNums} from '@/assets/js/api'
export default {
  name: 'history',
  data(){
    return{
      history:[],
      length:0
    }
  },
  props: {},
  mounted(){
    this.getHistory()
    this.getHisNums()
  },
  methods:{
    async getHistory(){
      this.history = await getHistory(localStorage.getItem('username'),1)
    },
    tableRowClassName({row, rowIndex}) {
        if (row.state == '啥也木搜到') return 'nothing-row'
        else if(row.state == '完成') return 'success-row'
        else if(row.state == '出错了' || row.state == '超时') return 'error-row'
        return 'warning-row'
    },
    async handleCurrentChange(pageNumber){
        this.history = await getHistory(localStorage.getItem('username'),pageNumber)
    },
    async getHisNums(){
        let length = await getHisNums(localStorage.getItem('username'))
        this.length = 10 * (length / 12)
    }
  },
  activated(){
    this.getHistory()
    this.getHisNums()
  },
  deactivated(){
    this.history = []
  }
}
</script>

<style>
.history{
  position: absolute;
  width: 1400px;
  height: 700px;
  right: 20px;
  top: 20px;
	z-index: 0;
}
.el-table .warning-row {
  background: #FCF3CF;
}
.el-table .success-row {
  background: #ABEBC6;
}
.el-table .error-row {
  background: #FF6A6A;
}
.el-table .nothing-row {
  background: white;
}
</style>