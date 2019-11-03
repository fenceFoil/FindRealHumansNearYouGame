import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Profile from '../views/Profile.vue'
import Results from '../views/Results.vue'
import PickupLine from '../views/PickupLine.vue'
import Swipe from '../views/Swipe.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/pickupline',
    name: 'pickupline',
    component: PickupLine
  },
  {
    path: '/results',
    name: 'results',
    component: Results
  },
  {
    path: '/swipe',
    name: 'swipe',
    component: Swipe
  }
]

const router = new VueRouter({
  routes
})

export default router
