import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

localStorage.setItem('resturl', '')
//localStorage.setItem('resturl', '44.224.175.124')

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
