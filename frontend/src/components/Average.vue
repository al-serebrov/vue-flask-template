<template>
  <div>
      <select name="categories" @change="onCategoryChange($event)" v-model="selectedCategory">
        <option disabled value="" selected hidden>Категория</option>
        <option
            v-for="category in categories"
            :key="category.name"
            :value="category.value"
        >{{ category.name }}</option>
      </select>
      <select name="bodystyles" v-model="selectedBodystyle">
        <option disabled value="" selected hidden>Кузов</option>
        <option
            v-for="bodystyle in bodystyles"
            :key="bodystyle.name"
            :value="bodystyle.value"
        >{{ bodystyle.name }}</option>
      </select>
      <select name="marks" @change="onMarkChange($event)" v-model="selectedMark">
        <option disabled value="" selected hidden>Марка</option>
        <option
            v-for="mark in marks"
            :key="mark.name"
            :value="mark.value"
        >{{ mark.name }}</option>
      </select>
      <select name="models" v-model="selectedModel">
        <option disabled value="" selected hidden>Модель</option>
        <option
            v-for="model in models"
            :key="model.name"
            :value="model.value"
        >{{ model.name }}</option>
      </select>
      <select name="gearboxes" v-model="selectedGearbox">
        <option disabled value="" selected hidden>Коробка передач</option>
        <option
            v-for="gearbox in gearboxes"
            :key="gearbox.name"
            :value="gearbox.value"
        >{{ gearbox.name }}</option>
      </select>
      <select name="fuels" v-model="selectedFuel">
        <option disabled value="" selected hidden>Топливо</option>
        <option
            v-for="fuel in fuels"
            :key="fuel.name"
            :value="fuel.value"
        >{{ fuel.name }}</option>
      </select>
      <select name="colors" v-model="selectedColor">
        <option disabled value="" selected hidden>Цвет</option>
        <option
            v-for="color in colors"
            :key="color.name"
            :value="color.value"
        >{{ color.name }}</option>
      </select>
      <select name="yearStart" v-model="selectedStartYear">
        <option disabled value="" selected hidden>Начальный год</option>
        <option
            v-for="year in years"
            :key="year"
            :value="year"
        >{{ year }}</option>
      </select>
      <select name="yearEnd" v-model="selectedEndYear">
        <option disabled value="" selected hidden>Конечный год</option>
        <option
            v-for="year in years"
            :key="year"
            :value="year"
        >{{ year }}</option>
      </select>
      <select name="states" @change="onStateChange($event)" v-model="selectedState">
        <option disabled value="" selected hidden>Область</option>
        <option
            v-for="state in states"
            :key="state.name"
            :value="state.value"
        >{{ state.name }}</option>
      </select>
      <select name="cities" v-model="selectedCity">
        <option disabled value="" selected hidden>Город</option>
        <option
            v-for="city in cities"
            :key="city.name"
            :value="city.value"
        >{{ city.name }}</option>
      </select>
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

<script>
import axios from 'axios';

const api_url = 'http://localhost:5000'

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
      selectedBodystyle: '',
      selectedState: '',
      selectedGearbox: '',
      selectedModel: '',
      selectedMark: '',
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
        this.selectedCategory = event.target.value;
        let url = `${api_url}/categories/${this.selectedCategory}`
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
        let selectedState = event.target.value;
        let url = `${api_url}/states/${selectedState}/cities`
        axios.get(url)
          .then((res) => {
              this.cities = res.data;
          })
          .catch((error) => {
            console.log(error);
          })
      },
      onMarkChange(event) {
        let selectedMark = event.target.value
        let url = `${api_url}/categories/${this.selectedCategory}/marks/${selectedMark}/models`
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
        let url = `${api_url}/average`
        let components = {
            category: this.selectedCategory,
            mark: this.selectedMark,
            model: this.selectedModel,
            bodystyle: this.selectedBodystyle,
            startYear: this.selectedStartYear,
            endYear: this.selectedEndYear,
            state: this.selectedState,
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
