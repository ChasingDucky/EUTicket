<template>
  <header>
    <div class="container">
      <h1>EUTicketWiki</h1>
      <p>{{ subtitle }}</p>
    </div>
  </header>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const subtitle = computed(() => {
  const subtitles = {
    '/': 'Your Complete Guide to European Railway Travel',
    '/countries': 'European Railway Country Guides',
    '/tickets': 'European Railway Tickets & Passes',
    '/routes': 'Popular European Railway Routes',
    '/tips': 'European Railway Travel Tips'
  }

  // Check if route path starts with any of the keys
  for (const [path, text] of Object.entries(subtitles)) {
    if (route.path === path || route.path.startsWith(path + '/')) {
      return text
    }
  }

  return 'Your Complete Guide to European Railway Travel'
})
</script>

<style scoped>
/* Header styles are in global CSS */
</style>
