<template>
  <div class="title">{{ title }} 共{{ detailData.length }}張</div>
  <div class="button-group">
    <!-- <el-button>
      <a :href="href" target="_blank">PTT 連結</a>
    </el-button> -->
    <a :href="href" class="el-button el-button--primary" target="_blank">PTT 連結</a>
    <el-button>自動撥放</el-button>
    <el-button>Default</el-button>
    <el-button>Default</el-button>
  </div>
  <el-carousel
    v-if="detailData.length > 0"
    :interval="4000"
    type="card"
    height="500px"
  >
    <el-carousel-item v-for="index in detailData.length" :key="index">
      <img :src="detailData[index - 1]" class="image" />
    </el-carousel-item>
  </el-carousel>

  <!-- <el-row v-if="detailData.length > 0" :gutter="20">
      <el-col
        v-for="index in detailData.length "
        :key="index"
        :xs="24"
        :sm="12"
        :md="10"
        :lg="8"
        :xl="6"
      >
        <el-card>
          <img :src="detailData[index-1]" class="image" />
        </el-card>
      </el-col>
    </el-row> -->
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

a:hover { text-decoration: none !important ; }

.image {
  width: 100%;
  height: 500px;
  margin: 0 auto;
  object-fit: cover;
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
