<template>
  <ul>
    <li v-for="category in categories" :key="category.name">{{ category.name }}</li>
  </ul>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Categories',
  data() {
    return {
      categories: [],
    };
  },
  methods: {
      getCategories() {
        const path = 'http://localhost:5000/categories';
        axios.get(path)
          .then((res) => {
            this.categories = res.data;
          })
          .catch((error) => {
            console.log(error);
          })
      },
  },
  created() {
    this.getCategories()
  }
};
</script>
