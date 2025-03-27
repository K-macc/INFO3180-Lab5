<script setup>
import { ref, onMounted, defineEmits } from 'vue';

const emit = defineEmits(['refreshPage']);

let csrf_token = ref("");

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log("CSRF Token: ",data);
            csrf_token.value = data.csrf_token;
        })
        .catch((error) => {
            console.log("Error: ",error);
        });
}

onMounted(() => {
    getCsrfToken();
});

const title = ref('');
const description = ref('');
const poster = ref(null);
const success_message = ref('');
const errors = ref([]);
const reload = ref(false);

const handleFileChange = (event) => {
    poster.value = event.target.files[0];
};

const saveMovie = () => {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    errors.value = [];
    success_message.value = '';

    fetch('/api/v1/movies', {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            if (data.errors){
                errors.value = data.errors;
                emit('flashMessage',errors);
            } else{
                success_message.value = "Movie Successfully Added";
                title.value = '';
                description.value = '';
                poster.value = null;
                emit('refreshPage');
            }
        })
        .catch(function (error) {
            emit('refreshPage');
            console.error("Fetch error: ", error);
        });
}

</script>



<template>
    <div class="movie-form-div">

        <transition name="fade">
            <div v-if="!reload">
                <div v-if="success_message" class="success-message">
                    {{ success_message }}
                </div>
            </div>
        </transition>

        <transition name="fade">
            <div v-if="errors.length" class="error-message">
                <ul>
                    <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
                </ul>
            </div>
        </transition>

        <form id="movieForm" @submit.prevent="saveMovie" class="movie-form" enctype="multipart/form-data">
            <div class="form-group mb-3">
                <label for="title" class="form-label">Title</label>
                <input id="title" type="text" name="title" v-model="title" class="form-control" />
            </div>
    
            <div class="form-group mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea id="description" name="description" v-model="description" class="form-control" ></textarea>
            </div>
    
            <div class="form-group mb-3">
                <div class ="poster">
                    <label for="poster" class="form-label">Poster</label>
                    <label for="poster-type" class="form-label poster-type">(PNG,JPG,JPEG)</label>
                </div>
                <input id="poster" name="poster" type="file" @change="handleFileChange" accept="image/png, image/jpeg"  class="form-control" />
            </div>
    
        <button type="submit" name="submit" class="btn btn-primary">Submit</button>
        </form>

    </div>
  </template>

<style scoped>
.success-message {
    color: green;
    background-color: #d4edda;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    margin-left: 10px;
    width: 99%;
}

.error-message {
    color: red;
    background-color: #f8d7da;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
}

.fade-leave-active {
  transition: opacity 1s ease-in-out;
}

.fade-leave-to {
  opacity: 0;
}

textarea {
    width: 100%; 
    height: 200px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

textarea:hover {
    border-color: #888; /* Darker border on hover */
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2); /* Slight glow effect */
}

input {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc; 
}

input:hover {
    border-color: #888; /* Darker border on hover */
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2); /* Slight glow effect */
}

label {
    font-weight: bold;
    font-family: "Georgia", "Times New Roman", serif;
    font-size: 18px;
    padding-top: 10px;
}

.form-control {
    font-family: 'Helvetica','Roboto','Open Sans';
}

.poster-type {
    font-size: 14px;
    margin-left: 10px;
}

.btn-primary {
    margin-top: 30px;
    width: 100px;
}
</style>