<script setup>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import CardList from "./components/CardList.vue";


// // 建立Router
// import { ref, computed } from 'vue'

// const currentPath = ref(window.location.hash)

// window.addEventListener('hashchange', () => {
//   currentPath.value = window.location.hash
// })

// const currentView = computed(() => {
//   return routes[currentPath.value.slice(1) || '/'] || NotFound
// })


</script>

<template>
  <div>
    <el-header height="80px">
      <Header />
    </el-header>
    <el-container>
      <el-main>
        <!-- <CardList /> -->
        <!-- <component :is="currentView" /> -->
        <router-view></router-view>
      </el-main>
      <el-footer>
        <Footer />
      </el-footer>
    </el-container>
  </div>
</template>

<style>
body {
  
  overflow-y: scroll;
  overflow-x: hidden;
  
}
.el-header {
  height: 80px;
  --el-header-height: 80px;
  background-color: #25ad9bdd;
  /* position: relative; */
  display: flex;
  justify-content: flex-start;
}
.el-container {
  height: calc(100vh - 100px);
  background: #EEEEEE;
}

.el-footer {
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

@media (max-width: 390px) {
  .el-footer {
  height: 100px !important;
}
}
</style>
