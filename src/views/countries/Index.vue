<template>
  <div class="countries-index">
    <div class="breadcrumb">
      <router-link to="/">Home</router-link> / Countries
    </div>

    <section>
      <h2>European Railway Systems by Country</h2>
      <p>Explore detailed information about railway systems across Europe. Each country has its own unique characteristics, ticket types, and travel tips.</p>
    </section>

    <section>
      <div class="card-grid">
        <div class="card" v-for="country in countries" :key="country.code">
          <h3>{{ country.flag }} {{ country.name }}</h3>
          <p>{{ country.description }}</p>
          <p><strong>Operator:</strong> {{ country.operator }}</p>
          <p>
            <router-link v-if="country.link" :to="`/countries/${country.link}`">
              View {{ country.name }} Guide →
            </router-link>
            <a v-else href="#">View {{ country.name }} Guide →</a>
          </p>
        </div>
      </div>
    </section>

    <section>
      <div class="info-box">
        <h4>🌍 Cross-Border Travel</h4>
        <p>Many European trains cross borders seamlessly. Popular international routes include:</p>
        <ul>
          <li>Paris - Brussels - Amsterdam (Thalys)</li>
          <li>Paris - London (Eurostar)</li>
          <li>Munich - Venice</li>
          <li>Barcelona - Paris</li>
          <li>Vienna - Prague - Berlin</li>
        </ul>
        <p>Make sure to check visa requirements and passport control procedures for international journeys.</p>
      </div>
    </section>
  </div>
</template>

<script setup>
const countries = [
  {
    code: 'FR',
    flag: '🇫🇷',
    name: 'France',
    description: 'Home to the TGV high-speed network, connecting major cities at speeds up to 320 km/h.',
    operator: 'SNCF',
    link: 'france'
  },
  {
    code: 'DE',
    flag: '🇩🇪',
    name: 'Germany',
    description: 'Extensive rail network with ICE high-speed trains and excellent connections throughout Central Europe.',
    operator: 'Deutsche Bahn (DB)',
    link: 'germany'
  },
  {
    code: 'IT',
    flag: '🇮🇹',
    name: 'Italy',
    description: 'Scenic routes with Frecciarossa high-speed trains connecting Rome, Milan, Venice, and Naples.',
    operator: 'Trenitalia, Italo',
    link: 'italy'
  },
  {
    code: 'ES',
    flag: '🇪🇸',
    name: 'Spain',
    description: 'Modern AVE high-speed network covering major cities and tourist destinations.',
    operator: 'Renfe',
    link: null
  },
  {
    code: 'CH',
    flag: '🇨🇭',
    name: 'Switzerland',
    description: 'World-renowned for punctuality and stunning alpine scenery. Home to scenic routes like Glacier Express.',
    operator: 'SBB CFF FFS',
    link: null
  },
  {
    code: 'GB',
    flag: '🇬🇧',
    name: 'United Kingdom',
    description: 'Extensive network with Eurostar connections to mainland Europe via Channel Tunnel.',
    operator: 'Multiple operators',
    link: null
  },
  {
    code: 'NL',
    flag: '🇳🇱',
    name: 'Netherlands',
    description: 'Efficient rail network connecting Amsterdam, Rotterdam, The Hague, and beyond.',
    operator: 'NS (Nederlandse Spoorwegen)',
    link: 'netherlands'
  },
  {
    code: 'AT',
    flag: '🇦🇹',
    name: 'Austria',
    description: 'Beautiful alpine routes with excellent connections to neighboring countries.',
    operator: 'ÖBB',
    link: null
  },
  {
    code: 'BE',
    flag: '🇧🇪',
    name: 'Belgium',
    description: 'Central European hub with connections to France, Netherlands, Germany, and Luxembourg.',
    operator: 'SNCB/NMBS',
    link: 'belgium'
  },
  {
    code: 'CZ',
    flag: '🇨🇿',
    name: 'Czech Republic',
    description: 'Affordable travel with beautiful routes through historic cities and countryside.',
    operator: 'České dráhy (ČD)',
    link: null
  },
  {
    code: 'PT',
    flag: '🇵🇹',
    name: 'Portugal',
    description: 'Scenic coastal routes and connections to Spain via high-speed trains.',
    operator: 'CP (Comboios de Portugal)',
    link: null
  },
  {
    code: 'SE',
    flag: '🇸🇪',
    name: 'Sweden',
    description: 'Efficient Scandinavian rail network with modern trains and beautiful northern landscapes.',
    operator: 'SJ (Statens Järnvägar)',
    link: null
  }
]
</script>

<style scoped>
/* All styles in global CSS */
</style>
