import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

if (process.env.NODE_ENV === 'production') {
  document.addEventListener('contextmenu', e => e.preventDefault())
}

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
