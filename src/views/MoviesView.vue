<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

const errors = ref([]);

const fetchMovies = () => {

    fetch('/api/v1/movies', {
        method: 'GET'
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            if (data.errors){
                errors.value = data.errors;
            } else{
                movies.value = data.movies;
            }
        })
        .catch(function (error) {
            errors.value = ["An unexpected error occurred."];
            console.error("Fetch error: ", error);
        });
    
}

onMounted(() => {
    fetchMovies(); 
    });

</script>



<template>

<div class="movie-list">
    <h2>Movies</h2>
    <div v-if="movies.length === 0">Loading movies...</div>
    <div v-else class="movies-listed">
        <div v-for="movie in movies" :key="movie.id" class="movie">
            <img v-if="movie.poster" :src="`http://localhost:5173${movie.poster}`" alt="Movie Poster" class="movie-img" width="450">
            <div class="text-content">
                <h2 class="movie-title">{{ movie.title }}</h2> 
                <p class="movie-description">{{ movie.description }}</p>
            </div>
        </div>
    </div>
</div>

</template>


<style scoped>
h2 {
    text-align: left;
    margin-left: 50px;
}

.movie-list {
  text-align: left;
}

.movies-listed {
  display: grid;
  grid-template-rows: repeat(3, 1fr); /* Create three rows per column */
  grid-template-columns: repeat(3, 1fr); /* Create three columns per row */
  gap: 20px; /* Space between the items */
  width: 650px;
  margin-left: 50px;
}
.movie {
  display: grid;
  grid-template-columns: 190px 1fr; /* Image takes up 190px, text takes the remaining space */
  align-items: flex-start;  /* Align the content to the top */
  border: 1px solid #ddd;
  border-radius: 8px;
  background: #fff;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  width: 450px;
  height: 250px;
}

.movie-img {
  width: 170px; 
  height: 250px;
}

.movie-title {
  font-size: 20px;
  margin-bottom: 10px;
  font-weight: bold;
  text-align: left; 
  margin-left: 0px; /* Explicitly align the title to the left */
}

.movie-description {
  font-size: 15px;
  color: black;
  text-align: left;  /* Align text to the left */
  margin-top: 10px;  /* Add some space between the title and description */
}

.text-content {
    width: 250px;
    padding-top: 10px;
    text-align: left;
    justify-content: left;
}
</style>