<template>
  <div id="app">
    <Header />
    <Navigation />
    <main>
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Navigation from './components/Navigation.vue'
import Footer from './components/Footer.vue'
</script>

<style>
/* Global styles are imported in main.js */
</style>
