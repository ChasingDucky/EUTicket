<template>
  <div class="main-content">
    <!-- Breadcrumb Navigation -->
    <div class="breadcrumb">
      <router-link to="/">Home</router-link> / Popular Routes
    </div>

    <!-- Introduction Section -->
    <section>
      <h2>Iconic European Train Journeys</h2>
      <p>Discover Europe's most scenic, convenient, and popular railway routes - from high-speed city connections to legendary scenic journeys through the Alps.</p>
    </section>

    <!-- High-Speed City Connections -->
    <section>
      <h2>High-Speed City Connections</h2>
      <div class="card-grid">
        <div class="card">
          <h3>🇫🇷🇬🇧 Paris - London</h3>
          <p><strong>Duration:</strong> 2h15<br>
          <strong>Operator:</strong> Eurostar<br>
          <strong>Price from:</strong> €50</p>
          <p>Travel under the English Channel via the Channel Tunnel. Passport control at departure station.</p>
        </div>

        <div class="card">
          <h3>🇩🇪🇫🇷 Frankfurt - Paris</h3>
          <p><strong>Duration:</strong> 3h50<br>
          <strong>Operator:</strong> ICE/TGV<br>
          <strong>Price from:</strong> €40</p>
          <p>Direct high-speed connection through picturesque Rhine Valley.</p>
        </div>

        <div class="card">
          <h3>🇳🇱🇫🇷 Amsterdam - Paris</h3>
          <p><strong>Duration:</strong> 3h20<br>
          <strong>Operator:</strong> Thalys<br>
          <strong>Price from:</strong> €35</p>
          <p>Popular route via Brussels. Book early for best prices.</p>
        </div>

        <div class="card">
          <h3>🇩🇪🇦🇹 Munich - Vienna</h3>
          <p><strong>Duration:</strong> 4h00<br>
          <strong>Operator:</strong> Railjet<br>
          <strong>Price from:</strong> €30</p>
          <p>Comfortable journey through Bavarian and Austrian countryside.</p>
        </div>

        <div class="card">
          <h3>🇮🇹🇮🇹 Rome - Milan</h3>
          <p><strong>Duration:</strong> 3h00<br>
          <strong>Operator:</strong> Frecciarossa/Italo<br>
          <strong>Price from:</strong> €30</p>
          <p>Italy's busiest high-speed route. Two competing operators mean competitive prices.</p>
        </div>

        <div class="card">
          <h3>🇪🇸🇪🇸 Madrid - Barcelona</h3>
          <p><strong>Duration:</strong> 2h30<br>
          <strong>Operator:</strong> Renfe AVE<br>
          <strong>Price from:</strong> €35</p>
          <p>Spain's flagship high-speed route. Much faster than flying with check-in.</p>
        </div>
      </div>
    </section>

    <!-- Scenic & Legendary Routes -->
    <section>
      <h2>Scenic & Legendary Routes</h2>
      <div class="card-grid">
        <div class="card">
          <h3>🏔️ Glacier Express</h3>
          <p><strong>Route:</strong> Zermatt - St. Moritz (Switzerland)<br>
          <strong>Duration:</strong> 8h<br>
          <strong>Price from:</strong> CHF 152 + reservation</p>
          <p>The slowest express train in the world! Panoramic windows showcase Alpine beauty through 291 bridges and 91 tunnels.</p>
        </div>

        <div class="card">
          <h3>🌄 Bernina Express</h3>
          <p><strong>Route:</strong> Chur - Tirano (Switzerland-Italy)<br>
          <strong>Duration:</strong> 4h<br>
          <strong>Price from:</strong> CHF 62 + reservation</p>
          <p>UNESCO World Heritage route. Crosses the Alps at 2,253m without tunnels or cog wheels.</p>
        </div>

        <div class="card">
          <h3>🚂 Venice Simplon-Orient-Express</h3>
          <p><strong>Route:</strong> London/Venice/Paris/etc.<br>
          <strong>Duration:</strong> Varies<br>
          <strong>Price from:</strong> £2,500+</p>
          <p>Luxury 1920s-style train. The ultimate splurge for a once-in-a-lifetime experience.</p>
        </div>

        <div class="card">
          <h3>🌊 Bergen Railway</h3>
          <p><strong>Route:</strong> Oslo - Bergen (Norway)<br>
          <strong>Duration:</strong> 7h<br>
          <strong>Price from:</strong> NOK 299</p>
          <p>Norway's most scenic route crossing the mountain plateau at 1,237m.</p>
        </div>

        <div class="card">
          <h3>🏰 Rhine Valley</h3>
          <p><strong>Route:</strong> Mainz - Koblenz (Germany)<br>
          <strong>Duration:</strong> 1h30<br>
          <strong>Price from:</strong> €20</p>
          <p>Castles, vineyards, and the Lorelei rock. Take regional trains for best views.</p>
        </div>

        <div class="card">
          <h3>🌅 Cinque Terre Coastal</h3>
          <p><strong>Route:</strong> La Spezia - Levanto (Italy)<br>
          <strong>Duration:</strong> 30 min<br>
          <strong>Price from:</strong> €5</p>
          <p>Mediterranean coastline with colorful villages. Get the Cinque Terre Card for unlimited trains.</p>
        </div>
      </div>
    </section>

    <!-- Night Train Routes -->
    <section>
      <h2>Night Train Routes</h2>
      <div class="content-page">
        <h3>Why Night Trains?</h3>
        <ul>
          <li>Save on accommodation costs</li>
          <li>Wake up in a new city</li>
          <li>Environmentally friendly</li>
          <li>Romantic travel experience</li>
        </ul>

        <h3>Popular Night Train Routes</h3>
        <table>
          <thead>
            <tr>
              <th>Route</th>
              <th>Operator</th>
              <th>Duration</th>
              <th>Price From</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Vienna - Venice</td>
              <td>ÖBB Nightjet</td>
              <td>11h</td>
              <td>€29 (seat), €50 (couchette), €90 (sleeper)</td>
            </tr>
            <tr>
              <td>Paris - Venice</td>
              <td>Thello (discontinued 2021)</td>
              <td>-</td>
              <td>Check alternatives</td>
            </tr>
            <tr>
              <td>Munich - Rome</td>
              <td>ÖBB Nightjet</td>
              <td>12h</td>
              <td>€29 (seat), €90 (sleeper)</td>
            </tr>
            <tr>
              <td>Berlin - Stockholm</td>
              <td>Snälltåget</td>
              <td>18h</td>
              <td>€35</td>
            </tr>
            <tr>
              <td>Vienna - Brussels</td>
              <td>ÖBB Nightjet</td>
              <td>14h</td>
              <td>€29 (seat), €90 (sleeper)</td>
            </tr>
          </tbody>
        </table>

        <div class="info-box tip">
          <h4>💡 Night Train Tips</h4>
          <ul>
            <li><strong>Book early:</strong> Sleeper compartments sell out quickly</li>
            <li><strong>Choose your accommodation:</strong> Seats (cheapest), couchettes (6-bed), sleepers (1-3 bed)</li>
            <li><strong>Bring essentials:</strong> Toiletries, eye mask, earplugs</li>
            <li><strong>Lock your compartment:</strong> Safety first</li>
            <li><strong>Breakfast available:</strong> Most night trains offer breakfast service</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Cross-Border Routes -->
    <section>
      <h2>Cross-Border Routes</h2>
      <div class="card-grid">
        <div class="card">
          <h3>🇨🇿🇦🇹🇭🇺 Prague - Vienna - Budapest</h3>
          <p>The classic Central European triangle. Each leg takes 4-5 hours with beautiful countryside.</p>
        </div>

        <div class="card">
          <h3>🇩🇪🇨🇭🇮🇹 Munich - Zurich - Milan</h3>
          <p>Alpine journey connecting three countries. Perfect for Switzerland stopover.</p>
        </div>

        <div class="card">
          <h3>🇫🇷🇪🇸 Paris - Barcelona</h3>
          <p>High-speed through southern France. Direct connection or via Montpellier for coastal views.</p>
        </div>

        <div class="card">
          <h3>🇳🇱🇧🇪🇫🇷 Amsterdam - Brussels - Paris</h3>
          <p>The Thalys corridor. One of Europe's busiest high-speed routes.</p>
        </div>
      </div>
    </section>

    <!-- Classic Multi-Country Itineraries -->
    <section>
      <h2>Classic Multi-Country Itineraries</h2>
      <div class="content-page">
        <h3>2-Week Grand Tour</h3>
        <p><strong>London → Paris → Amsterdam → Berlin → Prague → Vienna → Venice → Rome</strong></p>
        <ul>
          <li>Distance: ~3,500 km</li>
          <li>Estimated cost: €400-600 (point-to-point advance) or €520 (Eurail pass 10 days)</li>
          <li>Best time: April-October</li>
        </ul>

        <h3>1-Week Western Europe</h3>
        <p><strong>Paris → Brussels → Amsterdam → Cologne → Frankfurt → Zurich → Paris</strong></p>
        <ul>
          <li>Distance: ~2,000 km</li>
          <li>Estimated cost: €250-400</li>
          <li>Perfect for first-time visitors</li>
        </ul>

        <h3>10-Day Mediterranean</h3>
        <p><strong>Barcelona → Nice → Milan → Venice → Florence → Rome</strong></p>
        <ul>
          <li>Distance: ~2,200 km</li>
          <li>Estimated cost: €300-450</li>
          <li>Best time: May-June, September-October</li>
        </ul>
      </div>
    </section>

    <!-- Useful Tools -->
    <section>
      <div class="info-box">
        <h4>📱 Useful Route Planning Tools</h4>
        <ul>
          <li><strong>Deutsche Bahn (bahn.com):</strong> Best pan-European journey planner</li>
          <li><strong>Rome2rio:</strong> Compare train, bus, and flight options</li>
          <li><strong>Seat61:</strong> Detailed route information and booking advice</li>
          <li><strong>Rail Planner App:</strong> Official Eurail/Interrail route planning</li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script setup>
// No reactive data needed for this view
</script>

<style scoped>
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.breadcrumb {
  margin-bottom: 2rem;
  color: #666;
  font-size: 0.9rem;
}

.breadcrumb a {
  color: #0066cc;
  text-decoration: none;
}

.breadcrumb a:hover {
  text-decoration: underline;
}

section {
  margin-bottom: 2rem;
}

section h2 {
  color: #333;
  font-size: 1.8rem;
  margin-bottom: 1rem;
  border-bottom: 2px solid #0066cc;
  padding-bottom: 0.5rem;
}

section p {
  color: #666;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1rem;
}

.card {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

.card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.card h3 {
  color: #0066cc;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.card p {
  font-size: 0.95rem;
  margin-bottom: 0.5rem;
  color: #666;
  line-height: 1.6;
}

.card ul {
  margin-left: 1.5rem;
  margin-bottom: 1rem;
  color: #666;
}

.card li {
  margin-bottom: 0.3rem;
}

.content-page {
  background: #f9f9f9;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.content-page h3 {
  color: #333;
  font-size: 1.1rem;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
}

.content-page h3:first-child {
  margin-top: 0;
}

.content-page p {
  color: #666;
  margin-bottom: 0.5rem;
  font-weight: normal;
}

.content-page ul {
  margin-left: 1.5rem;
  margin-bottom: 1rem;
  color: #666;
}

.content-page li {
  margin-bottom: 0.3rem;
  line-height: 1.5;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1rem;
  background: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow: hidden;
}

table th {
  background-color: #0066cc;
  color: white;
  padding: 1rem;
  text-align: left;
  font-weight: bold;
}

table td {
  padding: 1rem;
  border-bottom: 1px solid #ddd;
  color: #666;
}

table tbody tr:hover {
  background-color: #f5f5f5;
}

.info-box {
  background: #e8f4f8;
  border-left: 4px solid #0066cc;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  border-radius: 4px;
}

.info-box.tip {
  background: #f0f8e8;
  border-left-color: #66cc00;
}

.info-box h4 {
  color: #333;
  margin-bottom: 0.5rem;
  font-size: 1rem;
}

.info-box p {
  color: #666;
  margin-bottom: 0.5rem;
}

.info-box ul {
  margin-left: 1.5rem;
  color: #666;
}

.info-box li {
  margin-bottom: 0.3rem;
  line-height: 1.5;
}
</style>
