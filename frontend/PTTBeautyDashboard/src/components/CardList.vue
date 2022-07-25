<template>
  <el-row justify="space-around">
    <el-col v-for="(item, index) in pttData" :key="index" :xs="24" :sm="12" :md="6" :lg="6" :xl="6">
      <el-card>
        <img :src="item.urls[0]" class="image" />
        <div style="padding: 14px">
          <span>{{ item.title }}</span>
          <!--<div class="bottom">
            <time class="time">{{ currentDate }}</time>
            <el-button text class="button">Operating</el-button>
          </div>-->
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import {getAllImage} from "@/api/image.js"

const pttData = ref([]);
const getData = function(){
  getAllImage().then((response)=>{
    console.log(response.data);
    pttData.value = response.data.msg;
  }).catch().finally();
}

onMounted(() => {
  getData();
  console.log(pttData);
});
</script>

<style>
.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 200px;
  height: 300px;
  /*display: block;*/
  object-fit: cover;
}
</style>
