<script setup>
import CardList from "./components/CardList.vue";
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
</script>

<template>
  <!--<header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>-->
  <div>
    <el-header height="80px">
      <Header />
    </el-header>
    <el-container>
      <el-main>
        <CardList />
      </el-main>
      <el-footer>
        <Footer />
      </el-footer>
    </el-container>
  </div>
</template>

<style>
/*@import './assets/base.css';*/
body {
  height: 100%;
  overflow: hidden;
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
  height: calc(100vh - 80px);
}

.el-footer {
  background: #EEEEEE;
  display: flex;
  justify-content: flex-start;
}

/* .el-main {
  position: absolute;
  left: 200px;
  right: 0;
  top: 64px;
  bottom: 0;
  overflow-y: scroll;
} */

/*#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;

  font-weight: normal;
}

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

a,
.green {
  text-decoration: none;
  color: hsla(160, 100%, 37%, 1);
  transition: 0.4s;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}

@media (min-width: 1024px) {
  body {
    display: flex;
    place-items: center;
  }

  #app {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0 2rem;
  }

  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  .logo {
    margin: 0 2rem 0 0;
  }
}*/
</style>
