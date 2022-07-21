<template>
  <el-row justify="space-around">
    <el-col v-for="(item, index) in pttData" :key="index" :xs="24" :sm="12" :md="6" :lg="6" :xl="6">
      <el-card>
        <img :src="item.url" class="image" />
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

const currentDate = ref(new Date());
const pttData = ref([
  { title: "[正妹] 黑色", url: "https://i.imgur.com/BTvLUuI.jpg" },
  { title: "[正妹] 內雙", url: "https://imgur.com/2Dz23O" },
  { title: "[正妹] 金曲新人", url: "https://i.imgur.com/qitZ48X.gif" },
  { title: "[正妹] 八蜜凛", url: "https://i.imgur.com/DDL0c57.jpg" },
  { title: "[正妹] 朴恩斌", url: "https://i.imgur.com/RkmEdO0.jpg" },
  {
    title: "[正妹] aespa Karina Winter",
    url: "https://i.imgur.com/KfpE9Yu.jpg",
  },
  { title: "[正妹] 除毛師", url: "https://i.imgur.com/VTWAlXI.jpg" },
  { title: "[正妹] 目不轉睛", url: "https://i.imgur.com/TPaLRPj.jpg" },
  { title: "[正妹] Lyliana Wray", url: "https://i.imgur.com/JmpIQuz.jpg" },
  { title: "[正妹] 逗貓的女孩", url: "https://i.imgur.com/t0FtGJO.jpg" },
]);

onMounted(() => {
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
