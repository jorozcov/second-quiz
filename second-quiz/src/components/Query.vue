<template>
    <div class="query-container">
        <h3>{{ queryUser.Name }}</h3>
        <p>Created by: {{ queryUser.Username }}</p>
        <p>Age: {{ query.AgeFrom }} - {{ query.AgeTo }}</p>
        <p>Weight: {{ query.WeightFrom }} - {{ query.WeightTo }}</p>
        <p>Weeks: {{ query.WeeksFrom }} - {{ query.WeeksTo }}</p>
        <p>Comment: {{ queryUser.Comment }}</p>
        <button @click="toggleUse(queryUser.Name)" class="btn btn-primary">Use</button>
    </div>
</template>

<script>
export default {
    name: 'Query',
    props: {
        queryUser: Object,
        query: Object
    },
    methods: {
        toggleUse(Name) {
            console.log(Name);
            this.$emit('toggle-use', Name);
        }
    }
};
</script>

<style scoped>
.query-container {
background-color: #f4f4f4;
padding: 20px;
border: 1px solid #ccc;
border-radius: 5px;
max-width: 400px;
margin: 0 auto;
margin-top: 20px;
}

h3 {
color: #333;
font-size: 1.1em;
margin-bottom: 10px;
}

p {
color: #555;
font-size: 0.9em;
margin: 8px 0;
}

.btn {
background-color: #327d3d; 
color: #fff;
border: none;
padding: 5px 10px;
border-radius: 5px;
cursor: pointer;
}
</style>
  