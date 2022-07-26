import ImageDetail from "@/components/ImageDetail.vue"
import CardList from "@/components/CardList.vue";
import { createWebHashHistory, createRouter } from 'vue-router'

const routes = [
    { path: '/', name: 'home', component: CardList },
    { path: '/Detail', name: 'Detail', component: ImageDetail },
  ]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
    })

export default router;