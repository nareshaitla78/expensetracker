<template>
  <q-page>
    <!-- ECharts chart render -->
    <ECharts :option="getchartdata" style="width: 100%; height: 400px;" />
    <q-btn @click="getData()" label="Get Flask Data"></q-btn>
    <div v-if="message">{{ message }}</div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';
import * as echarts from 'echarts';  // Import echarts globally
import VueECharts from 'vue-echarts'; // Import vue-echarts component

export default defineComponent({
  name: 'IndexPage',
  components: {
    ECharts: VueECharts,  // Correct registration of ECharts component
  },
  data() {
    return {
      message: null,  // Data that holds the message from Flask
    };
  },
  methods: {
    getData() {
      this.$axios
        .get('get_data/')
        .then((response) => {
          if (response.data.ok) {
            this.message = response.data.message;
          }
        })
        .catch((err) => {
          console.log(err, 'error');
        });
    },
  },
  computed: {
    getchartdata() {
      let options= {
        tooltip:{
          show:true,
          formatter:function(params){
            return params.name+"-"+params.value+"%"
          }
        },
        xAxis: [
        {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        }
        ],
        yAxis: [{
          type: 'value',
        }],
        series: [
          {
            data: [120, 200, 150, 80, 70, 110, 130],
            type: 'bar',
          },
        ],
      };
      return options
    },
  },
});
</script>
