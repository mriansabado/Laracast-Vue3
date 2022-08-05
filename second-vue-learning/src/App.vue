<script>
  export default {
    data() {
      return {
        text: ''
      }
    }
  }
</script>

<template>
<div id="main-container">
  <div id="input-section">
    <input v-model="text" placeholder="Type here" />
  </div>
  <div id="output-section">
    <h1>{{ text }}</h1>
  </div>
</div>
</template>

<style scoped>
#main-container {
  background-color: pink;
  height: 400px;
}

#input-section {
  background-color: lightblue;
  height: 200px;

}

#output-section {
  background-color: bisque;
  height: 400px;
}

h1 {
  font-size: 200px;
}

</style>
