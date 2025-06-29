import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/catalog',
      name: 'catalog',
      component: () => import('@/views/CatalogView.vue'),
    },
    {
      path: '/filters',
      name: 'filters',
      component: () => import('@/views/FiltersView.vue'),
    },
    {
      path: '/title/:id',
      name: 'titleDetail',
      props: true,
      component: () => import('@/views/TitleDetailView.vue')
    },
  ],
})

export default router
