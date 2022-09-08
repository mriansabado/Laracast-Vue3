<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<section class="main-section">
  <div>
    <div>
      <h1>Search for Drink by Name</h1>
    </div>
    <div>
     <h1>More Information on ingredient</h1>
    </div>
    <div>
      <h1>Generate a Random Drink</h1>
    </div>
  </div>
  <div>
    <h1>Image Results Area</h1>
  </div>
  <div>
   <h1>Text Results Area</h1>
  </div>
 
</section>
</template>

<style>
.main-section {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  background-color: lightblue;
  height: auto;
}
</style>
