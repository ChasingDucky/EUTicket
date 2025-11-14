<template>
  <div class="home">
    <section>
      <h2>Welcome to EUTicketWiki</h2>
      <p>Your comprehensive resource for traveling Europe by train. Whether you're planning a multi-country adventure or a single journey, we've got you covered with essential information about tickets, routes, and practical travel tips.</p>
    </section>

    <section>
      <h2>Quick Start Guide</h2>
      <div class="card-grid">
        <div class="card">
          <h3>🌍 Choose Your Destination</h3>
          <p>Explore railway systems across Europe:</p>
          <ul>
            <li><router-link to="/countries/france">France</router-link></li>
            <li><router-link to="/countries/germany">Germany</router-link></li>
            <li><a href="#">Italy</a></li>
            <li><a href="#">Spain</a></li>
            <li><a href="#">Switzerland</a></li>
            <li><a href="#">Netherlands</a></li>
            <li><a href="#">Austria</a></li>
            <li><a href="#">United Kingdom</a></li>
          </ul>
        </div>

        <div class="card">
          <h3>🎫 Ticket Options</h3>
          <p>Find the right ticket for your journey:</p>
          <ul>
            <li><a href="#">Single & Return Tickets</a></li>
            <li><a href="#">Eurail Pass</a></li>
            <li><a href="#">Interrail Pass</a></li>
            <li><a href="#">Advance Booking Tips</a></li>
            <li><a href="#">Where to Book</a></li>
          </ul>
        </div>

        <div class="card">
          <h3>🚆 Classic Routes</h3>
          <p>Explore Europe's most scenic train journeys:</p>
          <ul>
            <li><a href="#">Paris - London (Eurostar)</a></li>
            <li><a href="#">Glacier Express (Switzerland)</a></li>
            <li><a href="#">Venice Simplon-Orient-Express</a></li>
            <li><a href="#">Bernina Express</a></li>
            <li><a href="#">Major City Connections</a></li>
          </ul>
        </div>

        <div class="card">
          <h3>💡 Travel Tips</h3>
          <p>Make the most of your train travel:</p>
          <ul>
            <li><a href="#">Seat Reservations</a></li>
            <li><a href="#">Luggage Guidelines</a></li>
            <li><a href="#">Navigating Stations</a></li>
            <li><a href="#">Money-Saving Tips</a></li>
            <li><a href="#">First-Time Traveler Guide</a></li>
          </ul>
        </div>
      </div>
    </section>

    <section>
      <h2>Why Travel Europe by Train?</h2>
      <div class="card-grid">
        <div class="card">
          <h3>🌿 Eco-Friendly</h3>
          <p>Trains produce significantly less CO2 per passenger than flying, making them the greenest way to explore Europe.</p>
        </div>

        <div class="card">
          <h3>🏙️ City Center to City Center</h3>
          <p>Train stations are typically located in city centers, saving time and money on airport transfers.</p>
        </div>

        <div class="card">
          <h3>🎒 Luggage Freedom</h3>
          <p>No strict luggage limits or extra fees. Bring what you need for your journey.</p>
        </div>

        <div class="card">
          <h3>🌄 Scenic Views</h3>
          <p>Enjoy breathtaking landscapes through large windows as you travel through Europe's diverse regions.</p>
        </div>

        <div class="card">
          <h3>📱 Stay Connected</h3>
          <p>Most trains offer free WiFi, power outlets, and comfortable seating for working or relaxing.</p>
        </div>

        <div class="card">
          <h3>🗺️ Flexible Travel</h3>
          <p>With extensive rail networks, you can easily change plans and explore off-the-beaten-path destinations.</p>
        </div>
      </div>
    </section>

    <section>
      <h2>Featured Resources</h2>
      <div class="info-box">
        <h4>📚 Essential Reading</h4>
        <p>Before you travel, check out these comprehensive guides:</p>
        <ul>
          <li><a href="#">Rail Pass Comparison Guide</a> - Which pass is right for you?</li>
          <li><a href="#">Trip Planning Guide</a> - How to plan your European rail adventure</li>
          <li><a href="#">Cross-Border Travel</a> - Tips for international journeys</li>
        </ul>
      </div>

      <div class="info-box tip">
        <h4>💰 Money-Saving Tip</h4>
        <p>Book tickets 60-90 days in advance for the best prices on high-speed trains. Many European rail operators release advance tickets with significant discounts!</p>
      </div>

      <div class="info-box warning">
        <h4>⚠️ Important Notice</h4>
        <p>Always check current travel requirements, visa regulations, and COVID-19 restrictions before traveling. Rail schedules and prices are subject to change.</p>
      </div>
    </section>

    <section>
      <h2>Major European Rail Operators</h2>
      <div class="content-page">
        <table>
          <thead>
            <tr>
              <th>Country</th>
              <th>Operator</th>
              <th>Website</th>
              <th>Notes</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>France</td>
              <td>SNCF</td>
              <td><a href="https://www.sncf.com" target="_blank">sncf.com</a></td>
              <td>TGV high-speed trains</td>
            </tr>
            <tr>
              <td>Germany</td>
              <td>Deutsche Bahn</td>
              <td><a href="https://www.bahn.com" target="_blank">bahn.com</a></td>
              <td>ICE high-speed network</td>
            </tr>
            <tr>
              <td>Italy</td>
              <td>Trenitalia</td>
              <td><a href="https://www.trenitalia.com" target="_blank">trenitalia.com</a></td>
              <td>Frecciarossa trains</td>
            </tr>
            <tr>
              <td>Spain</td>
              <td>Renfe</td>
              <td><a href="https://www.renfe.com" target="_blank">renfe.com</a></td>
              <td>AVE high-speed trains</td>
            </tr>
            <tr>
              <td>UK</td>
              <td>National Rail</td>
              <td><a href="https://www.nationalrail.co.uk" target="_blank">nationalrail.co.uk</a></td>
              <td>Multiple operators</td>
            </tr>
            <tr>
              <td>Switzerland</td>
              <td>SBB CFF FFS</td>
              <td><a href="https://www.sbb.ch" target="_blank">sbb.ch</a></td>
              <td>Known for punctuality</td>
            </tr>
            <tr>
              <td>Netherlands</td>
              <td>NS (Nederlandse Spoorwegen)</td>
              <td><a href="https://www.ns.nl" target="_blank">ns.nl</a></td>
              <td>Extensive network</td>
            </tr>
            <tr>
              <td>Austria</td>
              <td>ÖBB</td>
              <td><a href="https://www.oebb.at" target="_blank">oebb.at</a></td>
              <td>Railjet trains</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>
</template>

<script setup>
// No script needed for this component
</script>

<style scoped>
/* All styles are in global CSS */
</style>
