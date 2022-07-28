<template>
  <div class="title">{{ title }} 共{{ detailData.length }}張</div>
  <div class="button-group">
    <!-- <el-button>
      <a :href="href" target="_blank">PTT 連結</a>
    </el-button> -->
    <a :href="href" class="el-button" target="_blank">PTT 連結</a>
    
    <el-button>下載照片</el-button>
    <el-button @click="auto = !auto" :type="auto ? 'success' : 'default'"
      >自動播放</el-button
    >
  </div>
  <el-carousel
    v-if="detailData.length > 0"
    :interval="4000"
    type="card"
    height="500px"
    :autoplay="auto"
  >
    <el-carousel-item v-for="index in detailData.length" :key="index">
      <img :src="detailData[index - 1]" class="image" />
    </el-carousel-item>
  </el-carousel>
</template>

<script setup>
import { getImageByID } from "@/api/image.js";
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

const route = useRoute();
const title = ref(route.params.title);
const href = ref(route.params.href);
const detailData = ref([]);
const getImage = function (imageId) {
  getImageByID(imageId)
    .then((response) => {
      detailData.value = response.data.msg;
    })
    .catch()
    .finally();
};

onMounted(() => {
  getImage(route.params.imageId);
});

const auto = ref(true);
</script>

<style scoped>
.title {
  font-size: 36px;
  margin-bottom: 10px;
}
.button-group {
  display: flex;
  margin-bottom: 30px;
}

a {
  text-decoration: none !important;
}

a:hover {
  text-decoration: none !important ;
}

.image {
  width: 100%;
  height: 500px;
  margin: 0 auto;
  object-fit: contain;
}

@media (max-width: 390px) {
  .image {
    width: 100%;
    height: 80%;
    margin: 0 auto;
    object-fit: cover;
  }
}
</style>
