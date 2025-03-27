<script setup>
import MovieForm from '@/components/MovieForm.vue';

const handleRefreshPage = (reload) => {
    reload.value = true;
    setTimeout(() => {
        location.reload();
    }, 5000); // Reload after 3 seconds
};

const flashMessage = (error) => {
    setTimeout(() => {
        error.value = [];
  }, 5000);
}
</script>

<template>
    <div class="movie-form-view">
        <h1>Add a New Movie</h1>
        <MovieForm @refreshPage="handleRefreshPage" @flashMessage="flashMessage"/>
    </div>
</template>

<style scoped>
.movie-form-view {
    margin-left: 50px;
    width: 94%;
}

h1 {
    font-family: 'Montserrat', sans-serif;
    font-weight: bold;
}
</style>
