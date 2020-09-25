import Vue from 'vue';
import Router from 'vue-router';
import Categories from './components/Categories.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Categories',
      component: Categories,
    },
  ],
});
