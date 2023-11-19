<template>
    <!-- Form with Username, name and comment-->
    <form @submit = "onSubmit"  class = "SaveQuery">
        <div class = "FormSaveQuery">
            <div class="form-group">
                <label>Username</label>
                <div>
                    <input type="text" v-model="Username" name = "Username" placeholder="Username" />
                </div>
            </div>
            <div class="form-group">
                <label>Name</label>
                <div>
                    <input type="text" v-model="Name" name = "Name" placeholder="Name" />
                </div>
            </div>
            <div class="form-group">
                <label>Comment</label>
                <div>
                    <input type="text" v-model="Comment" name = "Comment" placeholder="Comment" />
                </div>
            </div>
            <div class="button-container">
                <input type = "submit" value = "Save Query" class="btn btn-primary"/>
                <button @click="onClick()" class="btn btn-red"> Cancel </button>
            </div>
        </div>
    </form>
</template>

<script>


export default {
    name: 'FormSave',
    data () {
        return {
            Username: '',
            Name: '',
            Comment: ''
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault();

            if(this.Username == ""){
                alert("Username is required");
            }
            if (this.Name == ""){
                alert("Name is required");
            }
            if (this.Comment == ""){
                alert("Comment is required");
            }
            
            const query = {
                Username: this.Username,
                Name: this.Name,
                Comment: this.Comment
            }
            this.$emit('submitSaveQuery', query);
            this.Username = '';
            this.Name = '';
            this.Comment = '';
        },
        onClick() {
            this.$emit('toggle-cancel-query');
        }
    }
}
</script>

<style scoped>
.SaveQuery {
    max-width: 400px;
    margin: 20px auto;
    padding: 20px;
    background-color: #f4f4f4;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.FormSaveQuery {
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}

input[type="text"] {
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
    justify-content: space-around; /* Adjust as needed */
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

.btn-red {
    background-color: rgb(210, 46, 60); /* Orange color */
}

.btn-red:hover {
    background: #ff002f;
}
</style>