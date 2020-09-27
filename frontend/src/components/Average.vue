<template>
  <div max-width="800px">
    <div class="flex-parent">
      <label class="flex-child">Категория</label>
      <v-select
        class="flex-child"
        label="name"
        :options="categories"
        v-model="selectedCategory"
        @input="onCategoryChange"
      />
    </div>
    <div class="flex-parent">
      <label class="flex-child">Кузов</label>
      <v-select
        class="flex-child"
        label="name"
        :options="bodystyles"
        v-model="selectedBodystyle"
        :reduce="name => name.value"
      />
    </div>
    <div class="flex-parent">
      <label class="flex-child">Марка</label>
      <v-select
        class="flex-child"
        label="name"
        :options="marks"
        v-model="selectedMark"
        @input="onMarkChange"
      />
    </div>
    <div class="flex-parent">
      <label class="flex-child">Модель</label>
      <v-select
        class="flex-child"
        label="name"
        :options="models"
        v-model="selectedModel"
        :reduce="name => name.value"
      />
    </div>
    <div class="flex-parent">
      <label class="flex-child">Коробка передач</label>
      <v-select
        class="flex-child"
        label="name"
        multiple
        :options="gearboxes"
        v-model="selectedGearbox"
        :reduce="name => name.value"
      />
    </div>
    <div class="flex-parent">
      <label class="flex-child">Топливо</label>
      <v-select
        class="flex-child"
        label="name"
        multiple
        :options="fuels"
        v-model="selectedFuel"
        :reduce="name => name.value"
      />
    </div>
    <div class="flex-parent">
      <label class="flex-child">Цвет</label>
      <v-select
        class="flex-child"
        label="name"
        :options="colors"
        v-model="selectedColor"
        :reduce="name => name.value"
      />
    </div>
    <div class="flex-parent">
      <label class="flex-child">Начальный год</label>
      <v-select
        class="flex-child"
        label="name"
        :options="years"
        v-model="selectedStartYear"
        :reduce="name => name.value"
      />
    </div>
    <div class="flex-parent">
      <label class="flex-child">Конечный год</label>
      <v-select
        class="flex-child"
        label="name"
        :options="years"
        v-model="selectedEndYear"
        :reduce="name => name.value"
      />
    </div>
    <div class="flex-parent">
      <label class="flex-child">Область</label>
      <v-select
        class="flex-child"
        label="name"
        :options="states"
        v-model="selectedState"
        @input="onStateChange"
      />
    </div>
    <div class="flex-parent">
      <label class="flex-child">Город</label>
      <v-select
        class="flex-child"
        label="name"
        :options="cities"
        v-model="selectedCity"
        :reduce="name => name.value"
      />
    </div>
      <button v-on:click=calculate>Рассчет средней цены</button>
      <br>
      <div v-if="calculated">
        <p>Всего объявлений: {{ total }}</p>
        <p>Средняя цена: {{ arithmeticMean }}</p>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">
                Ссылка на <a href="https://auto.ria.com">auto.ria.com</a>
              </th>
              <th scope="col">Цена</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in classifiedsLimited" :key="item.url">
              <td><a :href="item.url" target="_blank">{{ item.url }}</a></td>
              <td>{{ item.price }}</td>
            </tr>
          </tbody>
        </table> 
        <button @click="limit -= 10">Показать меньше</button>
        <button @click="limit += 10">Показать больше</button>
      </div>
  </div>
</template>

<style>
.inline-block-child {
  display: inline-block;
}
.flex-parent {
  display: flex;
}
.flex-child {
  flex: 1;
}
</style>

<script>
import axios from 'axios';

const api_url = process.env.VUE_APP_API_ENDPOINT;

export default {
  name: 'Average',
  data() {
    return {
      categories: [],
      bodystyles: [],
      marks: [],
      models: [],
      gearboxes: [],
      driverTypes: [],
      states: [],
      cities: [],
      fuels: [],
      colors: [],
      years: [],
      average: {},
      classifieds: [],
      calculated: false,
      limit: 10,
      total: 0,
      arithmeticMean: 0,
      selectedCategory: '',
      selectedCategoryId: '',
      selectedBodystyle: '',
      selectedState: '',
      selectedStateId: '',
      selectedGearbox: '',
      selectedModel: '',
      selectedMark: '',
      selectedMarkId: '',
      selectedCity: '',
      selectedFuel: '',
      selectedColor: '',
      selectedStartYear: '',
      selectedEndYear: '',
    };
  },
  computed: {
    classifiedsLimited() {
      return this.limit? this.classifieds.slice(0, this.limit) : this.classifieds;
    },
  },
  methods: {
      getGenericInfo() {
        let categories_url = `${api_url}/categories`  
        axios.get(categories_url)
          .then((res) => {
            this.categories = res.data;
          })
          .catch((error) => {
            console.log(error);
          })
        let states_url = `${api_url}/states`
        axios.get(states_url)
          .then((res) => {
            this.states = res.data;
          })
          .catch((error) => {
            console.log(error);
          })
        let colors_url = `${api_url}/colors`
        axios.get(colors_url)
          .then((res) => {
            this.colors = res.data;
          })
          .catch((error) => {
            console.log(error);
          })
        let fuels_url = `${api_url}/fuels`
        axios.get(fuels_url)
          .then((res) => {
            this.fuels = res.data;
          })
          .catch((error) => {
            console.log(error);
          })
      },
      onCategoryChange(event) {
        this.selectedCategoryId = event.value;
        let url = `${api_url}/categories/${this.selectedCategoryId}`
        axios.get(url)
          .then((res) => {
            this.bodystyles = res.data.bodystyles;
            this.marks = res.data.marks;
            this.gearboxes = res.data.gearboxes;
            this.driverTypes = res.data.driverTypes;
          })
          .catch((error) => {
            console.log(error);
          })
      },
      onStateChange(event) {
        this.selectedStateId = event.value;
        let url = `${api_url}/states/${this.selectedStateId}/cities`
        axios.get(url)
          .then((res) => {
              this.cities = res.data;
          })
          .catch((error) => {
            console.log(error);
          })
      },
      onMarkChange(event) {
        this.selectedMarkId = event.value;
        let url = `${api_url}/categories/${this.selectedCategoryId}/marks/${this.selectedMarkId}/models`
        axios.get(url)
          .then((res) => {
              this.models = res.data;
          })
          .catch((error) => {
            console.log(error);
          })
      },
      calculate() {
        this.limit = 10;
        this.classifieds = [];
        this.average = 0;
        this.total = 0;
        this.arithmeticMean = 0;
        let url = `${api_url}/average`
        let components = {
            category: this.selectedCategoryId,
            mark: this.selectedMarkId,
            model: this.selectedModel,
            bodystyle: this.selectedBodystyle,
            startYear: this.selectedStartYear,
            endYear: this.selectedEndYear,
            state: this.selectedStateId,
            city: this.selectedCity,
            fuels: this.selectedFuel,
            color: this.selectedColor,
            gears: this.selectedGearbox,
            driver_type: this.selectedDriverType,
        }
        const ret = [];
        for (let d in components) {
            if (components[d] instanceof Array && components[d].length == 0) {
                continue;
            }
            if (components[d]) {
               ret.push(encodeURIComponent(d) + '=' + encodeURIComponent(components[d]));
            }
        }
        let querystring = ret.join('&');
        let average_url = `${url}?${querystring}`
        axios.get(average_url)
          .then((res) => {
              this.average = JSON.parse(res.data);
              this.total = this.average.total;
              this.arithmeticMean = this.average.arithmeticMean.toFixed(2);
              let ids = this.average.classifieds
              let prices = this.average.prices
              let classifieds = []
              for (let i = 0; i < ids.length; i += 1) {
                  let url = `https://auto.ria.com/auto__${ids[i]}.html`
                  classifieds.push({url: url, price: prices[i].toFixed(2)})
              }
              this.classifieds = classifieds;
          })
          .catch((error) => {
            console.log(error);
          })
          this.calculated = true;
      },
  },
  created() {
    this.getGenericInfo()
    let year = new Date().getFullYear();
    for (let i = year - 90; i <= year; i += 1) {
       this.years[year - i] = i;  
    }
  },
};
</script>
