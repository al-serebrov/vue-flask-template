import Vue from 'vue';
import Router from 'vue-router';
import Average from './components/Average.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Average',
      component: Average,
    },
  ],
});
