<template>
  <q-page class="flex flex-center">
    <div class="p-4 bg-blue-500 text-white rounded-lg">
      <h1 class="text-xl font-bold">Hello, Tailwind with Quasar!</h1>
      <p class="text-base">This is a Quasar app using Tailwind CSS.</p>
    </div>
    <!-- <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    > -->
    <q-btn @click="getData()" label="get flask data"></q-btn>
    <div v-if="message" class="p-4 bg-blue-500">{{message}}</div>
    
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';
// import axios from 'axios';
export default defineComponent({
  name: 'IndexPage',
  data(){
    return{
      message:null,
    }
  },
  methods:{
    getData(){
      this.$axios.get('get_data/')
      .then(((response) =>{
        if(response.data.ok){
            this.message=response.data.message
        }
      }))
      .catch((err)=>{
        console.log(err,"error ")
      })
    }
  }
});
</script>
