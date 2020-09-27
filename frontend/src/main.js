import 'bootstrap/dist/css/bootstrap.css';
import 'vue-select/dist/vue-select.css';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vSelect from 'vue-select';

Vue.use(BootstrapVue);
Vue.component('v-select', vSelect);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
