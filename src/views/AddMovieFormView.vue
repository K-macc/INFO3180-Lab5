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
        <h2>ADD A NEW MOVIE</h2>
        <MovieForm @refreshPage="handleRefreshPage"/>
    </div>
</template>

<style scoped>
.movie-form-view {
    margin-left: 10px;
    width: 99%;
}

h2 {
    font-family: 'Lato','Montserrat','Poppins';
}
</style>
