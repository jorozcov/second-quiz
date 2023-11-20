<template>
    <div class="container">
        <h2 class="title">Saved Queries</h2>
        <div v-for="(query, i) in queries" :key="i">
            <Query :queryUser="query.User" :query="query.Query" />
        </div>
    </div>
</template>

<script>

import Query from './Query.vue'

export default {
    name: 'Queries',
    components: {
        Query
    },
    props: {
        // Array of queries from App.vue
        queries: Array
    }
}   
</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    
    
    margin-top: 30px;
}

.title {
    color: #000000;
    font-size: 1.5em;
    margin: 0 auto;
}

</style>