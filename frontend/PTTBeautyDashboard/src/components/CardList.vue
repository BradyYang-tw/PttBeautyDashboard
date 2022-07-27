<template>
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
import { ref, reactive, onMounted } from "vue";
import { getAllImage } from "@/api/image.js";
import { useRouter, useRoute } from "vue-router";
import.meta.env.DEV.VITE_SOME_KEY

// getAllImage
const pttData = ref([]);
const getData = function () {
  getAllImage()
    .then((response) => {
      console.log(response.data);
      pttData.value = response.data.msg;
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
  console.log("666666", import.meta.env.DEV.VITE_SOME_KEY);
});
</script>

<style scoped>
.time {
  font-size: 16px;
  /* font-weight: bold; */
  color: rgb(15, 15, 15);
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
