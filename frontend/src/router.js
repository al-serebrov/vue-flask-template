import Vue from 'vue';
import Router from 'vue-router';
import Messages from './components/Messages.vue';
import HelloWorld from './components/HelloWorld.vue';
import About from './components/About.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Messages',
      component: Messages,
    },
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld,
    },
    {
      path: '/about',
      name: 'About',
      component: About,
    }
  ],
});
