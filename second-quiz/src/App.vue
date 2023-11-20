<template>
  <div>
    <header class="page-header"> Consulting Natality 2016 - 2018 </header>
    <div class = "main-container">
      <div class="container-sec">
        <Header title="Query form"/>
        <Form @toggle-save-query = "toggleSaveQuery" @submit="submission"/>
        <div v-show="showSaveQuery">
          <FormSave @toggle-cancel-query = "toggleCancelQuery" @submitSaveQuery="saveQuery"/>
        </div>
        <Queries :queries="queries"/>
      </div>
      <div class="container-sec">
        <h2 class="title"> Welcome </h2>

        <p class="welcome-text">
            Welcome to the <span class="highlight">World Births Visualization</span> platform! 
            Here, you can explore the World Births Dataset by filling out the form with your specific parameters 
            such as age range, weight range, and weeks. Once you submit the form, 
            a dynamic <span class="highlight">pie chart</span> will be generated, providing a visual representation 
            of birth data from <span class="highlight">2016 to 2018</span> based on your selected criteria. 
            Additionally, you can save your submission by clicking on the "<span class="highlight">Save Query</span>" button and
            filling up the form. Also below those forms, you can find a list of saved queries 
            with details about each query, allowing you to revisit and compare different sets of birth data. 
            Explore the fascinating world of global births with an intuitive and interactive visualization tool.
        </p>

        <h2 class="title"> Pie Chart </h2>

        <MainChart :info_chart="info_chart"/>
      </div>
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Form from './components/Form.vue'
import FormSave from './components/FormSave.vue'
import MainChart from './components/MainChart.vue'
import Queries from './components/Queries.vue'

//Define as a global variable the values of the query so that they can be used in the save query
// Default values
var WeeksFrom = 35;
var WeeksTo = 40;
var AgeFrom = 25;
var AgeTo = 34;
var WeightFrom = 3000;
var WeightTo = 3500;

export default {
  name: 'App',
  components: {
    Header,
    Form,
    FormSave,
    MainChart,
    Queries
  },
  data () {
    return {
      showSaveQuery: false,
      info_chart: '',
      queries: []
    }
  },
  async created() {
    // Fetch queries from database
    this.queries = await this.fetchQueries();
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
          WeeksFrom = parseInt(query.WeeksFrom);
          WeeksTo = parseInt(query.WeeksTo);
          AgeFrom = parseInt(query.AgeFrom);
          AgeTo = parseInt(query.AgeTo);
          WeightFrom = parseInt(query.WeightFrom);
          WeightTo = parseInt(query.WeightTo);

          // Fetch data from API
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
    },
    async saveQuery(User){
      const res = await fetch('api/queries', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          User: {
            Username: User.Username,
            Name: User.Name,
            Comment: User.Comment
          },
          Query: {
            WeeksFrom: WeeksFrom,
            WeeksTo: WeeksTo,
            AgeFrom: AgeFrom,
            AgeTo: AgeTo,
            WeightFrom: WeightFrom,
            WeightTo: WeightTo
          }
        })
      })

      const data = await res.json();

      // Save the query in the database
      this.queries = [...this.queries, data];
      this.showSaveQuery = false;
    },
    async fetchQueries(){
      // Fetch queries from database
      const res = await fetch('api/queries');
      const data = await res.json();
      return data;
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
}

.page-header {
  background-color: #3ca64c;
  color: #fff;
  padding: 20px;
  text-align: center;
  font-size: 1.5em;
  font-weight: bold;
}

.welcome-text {
    font-family: 'Arial', sans-serif;
    font-size: 18px;
    line-height: 1.5;
    color: #333;
}

.highlight {
    color: #327d3d;
    font-weight: bold;
}

.title {
    text-align: center;
    color: #333; 
    font-family: 'Arial', sans-serif; 
    font-size: 2em; 
    margin-top: 30px;
    margin-bottom: 30px; 
}
</style>
