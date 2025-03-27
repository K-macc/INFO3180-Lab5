<template>
      <footer class="mt-5">
          <div class="container">
              <p>Copyright &copy {{ year }} Flask Inc.</p>
          </div>
      </footer>
</template>

<script setup>
import { ref } from "vue";

const year = (new Date).getFullYear();
</script>

<style scoped>

.container {
  display: flex;
  justify-content: flex-start; /* Align the content inside the container to the left */
  width: 100%;
  margin-left:700px;
  color: black;
}

</style>




