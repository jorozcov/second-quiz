<template>
    <div>
    <form @submit="onSubmit" class = "query">
    
        <div class="form-group">
            <label>Avarage Mother's Age Range (25 - 34)</label>
            <div class="input-group">
                <input type="number" v-model="AgeFrom" name = "AgeFrom" min="0" placeholder="From" />
                <input type="number" v-model="AgeTo" name = "AgeTo" min="0" placeholder="To" />
            </div>
        </div>

        <div class="form-group">
            <label>Avarage Birth Weight Range (3000 - 3500)</label>
            <div class="input-group">
                <input type="number" v-model="WeightFrom" name = "WeightFrom" min="0" placeholder="From" />
                <input type="number" v-model="WeightTo" name = "WeightTo" min="0" placeholder="To" />
            </div>
        </div>

        <div class="form-group">
            <label>Avarage Gestational Age Weeks Range (35 - 40)</label>
            <div class="input-group">
                <input type="number" v-model="WeeksFrom" name = "WeeksFrom" placeholder="From" />
                <input type="number" v-model="WeeksTo" name = "WeeksTo" placeholder="To" />
            </div>
        </div>

        <div class="button-container">
            <input type = "submit" value = "Submit Query" class="btn btn-primary"/>
        </div>

    </form>
    <div class="button-container">
        <button @click="onClick()" class="btn btn-orange"> Save Query </button>
        <button @click="Clear()" class="btn btn-red"> Clear </button>
    </div>
    </div>

</template>

<script>
export default {
    name: 'Form',
    data () {
        return {
            AgeFrom: '',
            AgeTo: '',
            WeightFrom: '',
            WeightTo: '',
            WeeksFrom: '',
            WeeksTo: '',
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault();

            //Set default values according to the database (min and max)
            if (this.WeeksFrom == ""){
                this.WeeksFrom = 35;
            }

            if (this.WeeksTo == ""){
                this.WeeksTo = 40;
            }

            if (this.AgeFrom == ""){
                this.AgeFrom = 25;
            }

            if (this.AgeTo == ""){
                this.AgeTo = 34;
            }

            if (this.WeightFrom == ""){
                this.WeightFrom = 3000;
            }

            if (this.WeightTo == ""){
                this.WeightTo = 3500;
            }

            //Arise alert if there is any invalid input
            if(this.WeeksFrom > this.WeeksTo){
                alert('Weeks From must be less than Weeks To');
                return;
            }

            if(this.AgeFrom > this.AgeTo){
                alert('Age From must be less than Age To');
                return;
            }

            if(this.WeightFrom > this.WeightTo){
                alert('Weight From must be less than Weight To');
                return;
            }

            //Create query object
            const query = {
                WeeksFrom: this.WeeksFrom,
                WeeksTo: this.WeeksTo,
                AgeFrom: this.AgeFrom,
                AgeTo: this.AgeTo,
                WeightFrom: this.WeightFrom,
                WeightTo: this.WeightTo
            }
            
            //Pass query object to the parent component
            this.$emit('submit', query);
        },
        onClick() {
            //Toggle the save query form
            this.$emit('toggle-save-query');
        },
        Clear() {
            //Clear all the fields
            this.WeeksFrom = '';
            this.WeeksTo = '';
            this.AgeFrom = '';
            this.AgeTo = '';
            this.WeightFrom = '';
            this.WeightTo = '';
        }
    }
}
</script>

<style scoped>
    /* Basic styling for the form container */
.query {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f4f4f4;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Styling for form groups */
.form-group {
    margin-bottom: 15px;
}

.input-group {
        display: flex;
        gap: 10px; /* Adjust the gap as needed */
}

/* Styling for labels */
label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Styling for input and select elements */
input[type="number"],
select {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Styling for buttons */
.button-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    justify-content: space-evenly; /* Adjust as needed */
}
.btn {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    padding: 10px 15px;
}

.btn-primary {
    background-color: #4CAF50;
    color: white;
}
.btn-primary:hover {
    background-color: #2f7332;
}

.btn-orange {
    background-color: #FFA500; /* Orange color */
}

.btn-orange:hover {
    background: #ff9100;
}

.btn-red {
    background-color: rgb(210, 46, 60); 
}

.btn-red:hover {
    background: #ff002f;
}

/* Additional styling for better spacing and alignment */
form {
    display: flex;
    flex-direction: column;
}

/* Optional: Add some spacing between the input fields */
.form-group div {
    display: flex;
    justify-content: space-between;
}

/* Optional: Adjust the overall spacing of the form */
.query {
    margin-top: 30px;
}

</style>