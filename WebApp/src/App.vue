<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <Header />

  <RouterView />
</template>

<style>
body {
  margin: 0;
  padding: 0;
}
</style>
