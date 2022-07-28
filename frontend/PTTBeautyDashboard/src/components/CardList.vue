<template>
  <p class="update-time">更新時間: {{now}}</p>
  <el-row :gutter="20">
    <el-col
      v-for="(item, index) in pttData"
      :key="index"
      :xs="24"
      :sm="12"
      :md="10"
      :lg="8"
      :xl="6"
    >
      <el-card>
        <img :src="item.urls[0]" class="image" />

        <div style="padding: 14px">
          <a :href="item.href" target="_blank"
            ><span>{{ item.title }}</span></a
          >
          <div class="bottom">
            <time class="time">照片日期：{{ item.date }}</time>
            <a
              href="#/Detail"
              class="button el-button el-button--primary"
              @click="goDetail(item.beautyId, item.title, item.href)"
              >more</a
            >
            <!-- <el-button text type="primary" class="button" @click="goDetail">more</el-button> -->
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup>
import { ref, reactive, onMounted, watch } from "vue";
import { getAllImage } from "@/api/image.js";
import { useRouter, useRoute } from "vue-router";
import moment from 'moment';

// getAllImage
const pttData = ref([]);
const now = ref('')
const getData = function () {
  getAllImage()
    .then((response) => {
      console.log(response.data);
      pttData.value = response.data.msg;
      now.value = moment().format('YYYY-MM-DD HH:mm:ss')
      
    })
    .catch()
    .finally();
};

// goDetail
const router = useRouter();
const route = useRoute();

const goDetail = function (id, title, href) {
  router.push({
    name: "Detail",
    params: {
      imageId: id,
      title: title,
      href: href
    },
  });
};

onMounted(() => {
  getData();
});

</script>

<style scoped>
.time {
  font-size: 16px;
  /* font-weight: bold; */
  color: rgb(15, 15, 15);
}
.update-time{
  display:flex;
  justify-content: flex-end;
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
  font-size: 16px !important;
}

.image {
  width: 100%;
  height: 300px;
  margin: 0 auto;
  /* display: block; */
  object-fit: contain;
}
</style>
