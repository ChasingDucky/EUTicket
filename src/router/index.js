import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/Home.vue')
    },
    {
      path: '/countries',
      name: 'countries',
      component: () => import('../views/countries/Index.vue')
    },
    {
      path: '/countries/france',
      name: 'countries-france',
      component: () => import('../views/countries/France.vue')
    },
    {
      path: '/countries/germany',
      name: 'countries-germany',
      component: () => import('../views/countries/Germany.vue')
    },
    {
      path: '/tickets',
      name: 'tickets',
      component: () => import('../views/tickets/Index.vue')
    },
    {
      path: '/routes',
      name: 'routes',
      component: () => import('../views/routes/Index.vue')
    },
    {
      path: '/tips',
      name: 'tips',
      component: () => import('../views/tips/Index.vue')
    }
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router
