<template>
  <div class = "main-container">
    <div class="container-sec">
      <Header title="Query for County Natality"/>
      <Form @toggle-save-query = "toggleSaveQuery" @submit="submission"/>
      <div v-show="showSaveQuery">
        <FormSave @toggle-cancel-query = "toggleCancelQuery"/>
      </div>
    </div>
    <div class="container-sec">
      <MainChart :info_chart="info_chart"/>
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Form from './components/Form.vue'
import FormSave from './components/FormSave.vue'
import MainChart from './components/MainChart.vue'

export default {
  name: 'App',
  components: {
    Header,
    Form,
    FormSave,
    MainChart
  },
  data () {
    return {
      showSaveQuery: false,
      info_chart: ''
    }
  },
  methods: {
    toggleSaveQuery() {
      this.showSaveQuery = true;
    },
    toggleCancelQuery() {
      this.showSaveQuery = false;
    },
    submission(query) {
      try {
        // Check if all required values are defined
        if (
          query.WeeksFrom !== undefined &&
          query.WeeksTo !== undefined &&
          query.AgeFrom !== undefined &&
          query.AgeTo !== undefined &&
          query.WeightFrom !== undefined &&
          query.WeightTo !== undefined
        ) {
          // Convert values to integers
          const WeeksFrom = parseInt(query.WeeksFrom);
          const WeeksTo = parseInt(query.WeeksTo);
          const AgeFrom = parseInt(query.AgeFrom);
          const AgeTo = parseInt(query.AgeTo);
          const WeightFrom = parseInt(query.WeightFrom);
          const WeightTo = parseInt(query.WeightTo);

          fetch(`http://localhost:8000/${WeeksFrom}_${WeeksTo}_${AgeFrom}_${AgeTo}_${WeightFrom}_${WeightTo}`)
            .then(response => response.json())
            .then(data => {
              this.info_chart = data;
              console.log(this.info_chart);
            });
        } else {
          
        }
      } catch (err) {
        console.log(err);
      }
    }
  },
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Poppins', sans-serif;
}

.main-container {
  max-width: 100%;
  margin: 70px auto;
  overflow: auto;
  display: flex;
}

.container-sec {
    flex: 1;
    padding: 20px; /* Adjust padding as needed */
    border: 1px solid #ccc; /* Optional: Add a border for visual separation */
  }
</style>
