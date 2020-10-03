<template>
  <div max-width="800px">
    <vue-topprogress ref="topProgress"></vue-topprogress>
       <table class="table">
          <thead>
            <tr>
              <th scope="col">Message</th>
              <th scope="col">Last modified</th>
              <th scope="col">Created at</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in messages" :key="item.id">
              <td>
                <div v-if="item.edit">
                  <input 
                    v-model = "item.message"
                    @blur="item.edit = false; $emit('update'); editMessage(item)"
                    @keyup.enter="item.edit = false; $emit('update'); editMessage(item)"
                  >
                  <button @click="item.edit = false; $emit('update'); editMessage(item)">OK</button>
                  <button @click="item.edit = false; $emit('update')">X</button>
                </div>
                <label
                  v-if="!item.edit"
                  @click="item.edit = true; $emit('update');"
                  href="#">
                {{ item.message }}</label>
              </td>
              <td>{{ item.last_modified_at }}</td>
              <td>{{ item.created_at }}</td>
              <td>
                <a @click="deleteMessage(item.id)" href="#">Delete</a>
              </td>
            </tr>
          </tbody>
        </table> 
        <input v-model.lazy="newMessage" default="Add new message"/><button @click="addMessage">Add</button>
  </div>
</template>

<style>
</style>

<script>
import axios from 'axios';                                
import { vueTopprogress } from 'vue-top-progress'

const api_url = `http://${process.env.VUE_APP_API_ENDPOINT}:5000`;

export default {
  name: 'Messages',
  data() {
    return {
      messages: [],
      newMessage: '',
      editedMessageId: null,
    };
  },
  components: {
    vueTopprogress
  },
  methods: {
      editMessage: function (item) {
        let url = `${api_url}/messages/${item.id}`  
        console.log(url)
        axios.post(url, {id: item.id, message: item.message})
          .then((res) => {
            if (!res.data.status == 'Success') console.log('error')
            this.getMessages();
            this.$refs.topProgress.done();
          })
          .catch((error) => {
            console.log(error);
          })
      },
      async getMessages() {
        let url = `${api_url}/messages`  
        await axios.get(url)
          .then((res) => {
            this.messages = res.data;
            this.$refs.topProgress.done()
          })
          .catch((error) => {
            console.log(error);
          })
      },
      async deleteMessage(messageId) {
          const url = `${api_url}/messages/${messageId}`
          this.$refs.topProgress.start()
          await axios.delete(url)
            .then(function(response){
                console.log(response.data);
                this.$refs.topProgress.done()
            })
            .catch(function(error) {
                console.log(error);
            })
          await this.getMessages()
      },
      async addMessage()  {
          const url = `${api_url}/messages`
          await axios.post(url, {message: this.newMessage})
            .then(function(response){
                console.log(response.data);
                this.$refs.topProgress.done()
            })
            .catch(function(error) {
                console.log(error);
            })
          await this.getMessages()
      }
  },
  mounted() {
    this.getMessages()
  },
  directives: {
    focus: {
      inserted (el) {
        el.focus()
      }
    }
  }
};
</script>
