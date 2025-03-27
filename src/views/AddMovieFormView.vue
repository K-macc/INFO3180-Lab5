<script setup>
import MovieForm from '@/components/MovieForm.vue';

const handleRefreshPage = () => {
    setTimeout(() => {
        window.location.reload();
    }, 3000); // Reload after 3 seconds
};
</script>

<template>
    <div class="movie-form-view">
        <h1>Add a New Movie</h1>
        <MovieForm @refreshPage="handleRefreshPage"/>
    </div>
</template>

<style scoped>
.movie-form-view {
    margin-left: 10px;
    width: 99%;
}
</style>
