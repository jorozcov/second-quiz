<template>
    <header class="header">
        <h1 class="header-title">{{ title }}</h1>
    </header>
</template>

<script>
export default {
    name: 'Header',
    props: {
        title: String
    }
}
</script>

<style scoped>
.header {
    padding: 20px; /* Header padding */
    text-align: center; /* Center align the text */
}

.header-title {
    margin: 0; /* Remove default margin for the h1 element */
    font-size: 24px; /* Adjust the font size as needed */
    color: #333; /* Text color */
}
</style>