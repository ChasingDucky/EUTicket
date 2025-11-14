<template>
  <div class="content-page">
    <div class="breadcrumb">
      <router-link to="/">Home</router-link> / <router-link to="/countries">Countries</router-link> / France
    </div>

    <h1>🇫🇷 France Railway Travel Guide</h1>

    <h2>Overview</h2>
    <p>France boasts one of Europe's most extensive and efficient high-speed rail networks. The TGV (Train à Grande Vitesse) has revolutionized train travel since 1981, connecting major cities at speeds up to 320 km/h. With the introduction of OUIGO (low-cost TGV) and excellent regional networks, France offers options for every budget and travel style. From the iconic Paris-Lyon route to scenic coastal journeys, French trains combine speed, comfort, and style.</p>

    <div class="info-box">
      <h4>📊 Quick Facts</h4>
      <ul>
        <li><strong>Rail Network:</strong> 28,000+ km of track</li>
        <li><strong>High-Speed Network:</strong> 2,800+ km of TGV lines</li>
        <li><strong>Annual Passengers:</strong> 1+ billion journeys</li>
        <li><strong>TGV Speed Record:</strong> 574.8 km/h (2007, world record)</li>
        <li><strong>Operational Speed:</strong> Up to 320 km/h on main lines</li>
        <li><strong>Stations:</strong> 3,000+ stations nationwide</li>
      </ul>
    </div>

    <h2>Railway Operator</h2>

    <h3>SNCF (Société Nationale des Chemins de fer Français)</h3>
    <p><strong>France's national railway company - Europe's TGV pioneer</strong></p>
    <ul>
      <li>Official Website: <a href="https://www.sncf.com" target="_blank">sncf.com</a> (French interface)</li>
      <li>English Booking: <a href="https://www.sncf-connect.com" target="_blank">sncf-connect.com</a></li>
      <li>App: SNCF Connect (iOS & Android) - booking, tickets, real-time info</li>
      <li>Customer Service: 3635 (from France) or +33 184943635 (international)</li>
      <li>English Support: Available via website chat and phone</li>
    </ul>

    <h2>Complete Train Types Guide</h2>

    <h3>TGV inOui - Premium High-Speed Service</h3>
    <div class="info-box">
      <p><strong>SNCF's flagship high-speed brand (launched 2017)</strong></p>
      <ul>
        <li><strong>Speed:</strong> Up to 320 km/h (199 mph)</li>
        <li><strong>Routes:</strong> All major TGV lines (Paris-Lyon, Paris-Marseille, Paris-Bordeaux, etc.)</li>
        <li><strong>Classes:</strong> Seconde (2nd class), Première (1st class)</li>
        <li><strong>Amenities:</strong>
          <ul>
            <li>Free WiFi (on most trains)</li>
            <li>Power outlets at every seat</li>
            <li>Bar car (except OUIGO)</li>
            <li>Air conditioning</li>
            <li>Spacious luggage areas</li>
            <li>Family spaces with baby changing</li>
            <li>Quiet zones (Espace Silence)</li>
            <li>Wheelchair accessible</li>
          </ul>
        </li>
        <li><strong>Première Class Extra Perks:</strong>
          <ul>
            <li>Wider seats with more legroom</li>
            <li>Complimentary hot beverage and snack</li>
            <li>Newspapers/magazines</li>
            <li>Access to lounges at major stations</li>
          </ul>
        </li>
        <li><strong>Reservation:</strong> Always mandatory, included in price</li>
      </ul>
    </div>

    <h3>OUIGO - Low-Cost High-Speed</h3>
    <div class="info-box tip">
      <p><strong>SNCF's budget brand - same TGV trains and speeds, fewer services</strong></p>
      <ul>
        <li><strong>Speed:</strong> Up to 320 km/h (same as TGV inOui)</li>
        <li><strong>Routes:</strong> Major cities (Paris, Lyon, Marseille, Bordeaux, Montpellier, etc.)</li>
        <li><strong>Price:</strong> From €10! (Book 4-6 months ahead)</li>
        <li><strong>What's Different:</strong>
          <ul>
            <li>Single class seating (equivalent to 2nd class)</li>
            <li>NO bar car - bring your own food/drinks</li>
            <li>Luggage restrictions: 1 small bag (55x35x25cm) FREE, larger bags €5 extra</li>
            <li>Seat selection: €3 extra (random assignment otherwise)</li>
            <li>Power outlets: €2 extra for "XL comfort" seats</li>
            <li>Departs from secondary stations (Paris-Marne-la-Vallée, Lyon Part-Dieu, etc.)</li>
          </ul>
        </li>
        <li><strong>Check-in:</strong> Must check in online 30 min - 4 hours before departure (or €5 fee)</li>
        <li><strong>Best For:</strong> Budget travelers willing to sacrifice some comfort</li>
        <li><strong>Booking:</strong> Separate website <a href="https://www.ouigo.com" target="_blank">ouigo.com</a></li>
      </ul>
    </div>

    <div class="info-box warning">
      <h4>⚠️ OUIGO Important Notes</h4>
      <ul>
        <li>OUIGO often departs from different stations than regular TGV</li>
        <li>Paris OUIGO trains often use Marne-la-Vallée (Disneyland) station, 35 min from Paris center</li>
        <li>Strict luggage policy - oversized/extra bags €40 at station!</li>
        <li>Must arrive 30 min early, late arrival = can't board</li>
      </ul>
    </div>

    <h3>TGV Lyria - France-Switzerland</h3>
    <ul>
      <li><strong>Joint SNCF-SBB operation</strong></li>
      <li><strong>Routes:</strong> Paris-Geneva, Paris-Lausanne, Paris-Zurich, Paris-Basel, Lyon-Geneva</li>
      <li><strong>Classes:</strong> Standard, Standard 1ère (1st class), Business 1ère</li>
      <li><strong>Special:</strong> Swiss-French bilingual service, Swiss chocolate on board</li>
    </ul>

    <h3>Intercités - Long-Distance Conventional</h3>
    <ul>
      <li><strong>Speed:</strong> Up to 200 km/h</li>
      <li><strong>Routes:</strong> Connects cities not on TGV network (e.g., Paris-Clermont-Ferrand, Paris-Limoges)</li>
      <li><strong>Cost:</strong> 30-50% cheaper than TGV</li>
      <li><strong>Types:</strong>
        <ul>
          <li><strong>Intercités (IC):</strong> Daytime trains, some with dining car</li>
          <li><strong>Intercités de Nuit (night trains):</strong> Overnight services with couchettes and sleepers</li>
        </ul>
      </li>
      <li><strong>Reservation:</strong> Mandatory on most routes</li>
    </ul>

    <h3>TER (Transport Express Régional) - Regional Trains</h3>
    <ul>
      <li><strong>Speed:</strong> 80-160 km/h</li>
      <li><strong>Coverage:</strong> Regional and local routes in all 12 regions</li>
      <li><strong>Frequency:</strong> Very frequent on popular routes</li>
      <li><strong>Cost:</strong> Very affordable (€5-20 for most journeys)</li>
      <li><strong>Reservation:</strong> NOT required - first-come, first-served</li>
      <li><strong>Perfect for:</strong> Day trips, exploring regions, Provence, Brittany, Normandy</li>
      <li><strong>Regional Passes:</strong> Many regions offer unlimited day/weekend passes</li>
    </ul>

    <h3>Transilien - Paris Region</h3>
    <ul>
      <li><strong>Coverage:</strong> Paris and Île-de-France suburbs</li>
      <li><strong>Types:</strong> Lines H, J, K, L, N, P, R, U</li>
      <li><strong>Integration:</strong> Works with Paris metro/bus tickets (zones)</li>
      <li><strong>Frequency:</strong> Every 10-30 minutes</li>
      <li><strong>Use:</strong> Commuting, Versailles, airports</li>
    </ul>

    <h2>Complete Ticket Price Guide - SNCF</h2>

    <h3>TGV inOui Fare Types</h3>

    <h4>Prem's - From €16</h4>
    <table>
      <thead>
        <tr>
          <th>Feature</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Price Range</strong></td>
          <td>€16 - €80 (varies by route and demand)</td>
        </tr>
        <tr>
          <td><strong>Booking Window</strong></td>
          <td>Released 4-6 months ahead, limited quantity</td>
        </tr>
        <tr>
          <td><strong>Train Binding</strong></td>
          <td>✅ Yes - must take specific train</td>
        </tr>
        <tr>
          <td><strong>Changes</strong></td>
          <td>❌ Not allowed</td>
        </tr>
        <tr>
          <td><strong>Refund</strong></td>
          <td>❌ Non-refundable</td>
        </tr>
        <tr>
          <td><strong>Exchange</strong></td>
          <td>❌ Non-exchangeable</td>
        </tr>
        <tr>
          <td><strong>Best For</strong></td>
          <td>Budget travelers with completely fixed plans</td>
        </tr>
      </tbody>
    </table>

    <h4>Seconde (2nd Class Standard)</h4>
    <table>
      <thead>
        <tr>
          <th>Feature</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Price Range</strong></td>
          <td>€35 - €120+</td>
        </tr>
        <tr>
          <td><strong>Train Binding</strong></td>
          <td>✅ Yes - for specific train booked</td>
        </tr>
        <tr>
          <td><strong>Changes</strong></td>
          <td>✅ Allowed with €15 fee (before departure)</td>
        </tr>
        <tr>
          <td><strong>Refund</strong></td>
          <td>✅ Yes, with deduction (typically 15-30%)</td>
        </tr>
        <tr>
          <td><strong>Flexibility</strong></td>
          <td>Moderate - can change for fee</td>
        </tr>
      </tbody>
    </table>

    <h4>Première (1st Class Standard)</h4>
    <table>
      <thead>
        <tr>
          <th>Feature</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Price Range</strong></td>
          <td>€50 - €180+ (typically 1.5-2x Seconde price)</td>
        </tr>
        <tr>
          <td><strong>Extra Benefits</strong></td>
          <td>Wider seats, complimentary refreshments, lounge access</td>
        </tr>
        <tr>
          <td><strong>Changes/Refund</strong></td>
          <td>Same as Seconde (€15 change fee, partial refund)</td>
        </tr>
      </tbody>
    </table>

    <h4>Flex (Fully Flexible)</h4>
    <table>
      <thead>
        <tr>
          <th>Feature</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Price Range</strong></td>
          <td>€70 - €200+ (2nd class), €100 - €280+ (1st class)</td>
        </tr>
        <tr>
          <td><strong>Train Binding</strong></td>
          <td>❌ No - valid on any train same day same route</td>
        </tr>
        <tr>
          <td><strong>Changes</strong></td>
          <td>✅ Free unlimited changes (before departure)</td>
        </tr>
        <tr>
          <td><strong>Refund</strong></td>
          <td>✅ Full refund (minus small admin fee ~€15)</td>
        </tr>
        <tr>
          <td><strong>Best For</strong></td>
          <td>Business travelers, last-minute bookers, uncertain schedules</td>
        </tr>
      </tbody>
    </table>

    <h3>OUIGO Pricing</h3>
    <table>
      <thead>
        <tr>
          <th>Component</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Base Ticket</strong></td>
          <td>€10 - €49 (depends on route and booking time)</td>
        </tr>
        <tr>
          <td><strong>Standard Bag (55x35x25cm)</strong></td>
          <td>FREE (1 per person)</td>
        </tr>
        <tr>
          <td><strong>Large Bag (55x35x25cm)</strong></td>
          <td>€5 online, €40 at station</td>
        </tr>
        <tr>
          <td><strong>XL Bag (30kg max)</strong></td>
          <td>€5 online, €40 at station</td>
        </tr>
        <tr>
          <td><strong>Seat Selection</strong></td>
          <td>€3 (random if not selected)</td>
        </tr>
        <tr>
          <td><strong>XL Comfort Seat (power outlet)</strong></td>
          <td>€7</td>
        </tr>
        <tr>
          <td><strong>Changes</strong></td>
          <td>€10 (if allowed by fare type)</td>
        </tr>
      </tbody>
    </table>

    <h3>Price Comparison: Real Route Examples</h3>
    <table>
      <thead>
        <tr>
          <th>Route</th>
          <th>OUIGO</th>
          <th>Prem's</th>
          <th>Seconde</th>
          <th>Flex Seconde</th>
          <th>Duration</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Paris - Lyon</strong></td>
          <td>€10 - €29</td>
          <td>€16 - €35</td>
          <td>€45 - €75</td>
          <td>€95 - €120</td>
          <td>2h 00m</td>
        </tr>
        <tr>
          <td><strong>Paris - Marseille</strong></td>
          <td>€16 - €39</td>
          <td>€25 - €49</td>
          <td>€65 - €105</td>
          <td>€130 - €165</td>
          <td>3h 15m</td>
        </tr>
        <tr>
          <td><strong>Paris - Bordeaux</strong></td>
          <td>€10 - €35</td>
          <td>€16 - €39</td>
          <td>€50 - €85</td>
          <td>€105 - €135</td>
          <td>2h 05m</td>
        </tr>
        <tr>
          <td><strong>Paris - Nice</strong></td>
          <td>€19 - €49</td>
          <td>€29 - €59</td>
          <td>€80 - €130</td>
          <td>€160 - €200</td>
          <td>5h 30m</td>
        </tr>
        <tr>
          <td><strong>Paris - Strasbourg</strong></td>
          <td>€10 - €29</td>
          <td>€16 - €35</td>
          <td>€45 - €75</td>
          <td>€90 - €115</td>
          <td>1h 45m</td>
        </tr>
        <tr>
          <td><strong>Paris - Lille</strong></td>
          <td>Not served</td>
          <td>€13 - €25</td>
          <td>€35 - €55</td>
          <td>€70 - €85</td>
          <td>1h 00m</td>
        </tr>
        <tr>
          <td><strong>Lyon - Marseille</strong></td>
          <td>€10 - €25</td>
          <td>€13 - €29</td>
          <td>€35 - €60</td>
          <td>€75 - €95</td>
          <td>1h 40m</td>
        </tr>
        <tr>
          <td><strong>Paris - Rennes</strong></td>
          <td>€10 - €29</td>
          <td>€16 - €32</td>
          <td>€40 - €65</td>
          <td>€85 - €105</td>
          <td>1h 30m</td>
        </tr>
      </tbody>
    </table>

    <div class="info-box warning">
      <h4>⚠️ Important Pricing Notes</h4>
      <ul>
        <li><strong>Prem's = Limited Seats:</strong> Released in batches, sell out fast</li>
        <li><strong>Book 3-4 months ahead:</strong> Best Prem's availability</li>
        <li><strong>Prices increase:</strong> As trains fill up, only expensive seats left</li>
        <li><strong>Friday evening premium:</strong> 20-30% more expensive</li>
        <li><strong>Sunday afternoon premium:</strong> Returning travelers = higher prices</li>
        <li><strong>OUIGO stations:</strong> Check departure location carefully!</li>
      </ul>
    </div>

    <h2>Discount Cards & Programs</h2>

    <h3>Carte Avantage - Adult Discount Card</h3>
    <table>
      <thead>
        <tr>
          <th>Card Type</th>
          <th>Cost</th>
          <th>Age</th>
          <th>Discount</th>
          <th>Break-Even</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Carte Jeune</strong></td>
          <td>€50/year</td>
          <td>12-27</td>
          <td>30% off TGV/Intercités</td>
          <td>~€167 in tickets</td>
        </tr>
        <tr>
          <td><strong>Carte Avantage</strong></td>
          <td>€49/year</td>
          <td>Adults</td>
          <td>30% off TGV/Intercités</td>
          <td>~€163 in tickets</td>
        </tr>
        <tr>
          <td><strong>Carte Senior+</strong></td>
          <td>€49/year</td>
          <td>60+</td>
          <td>30% off + extra benefits</td>
          <td>~€163 in tickets</td>
        </tr>
        <tr>
          <td><strong>Carte Famille Nombreuse</strong></td>
          <td>FREE</td>
          <td>3+ children</td>
          <td>30-75% off (family)</td>
          <td>Immediate savings</td>
        </tr>
      </tbody>
    </table>

    <h3>Card Benefits Details</h3>

    <h4>Carte Jeune (12-27 years)</h4>
    <div class="info-box">
      <ul>
        <li><strong>Discount:</strong> 30% on TGV inOui, OUIGO, Intercités</li>
        <li><strong>Applies to:</strong> Prem's, Seconde, Première fares</li>
        <li><strong>Restrictions:</strong> Limited seats per train (blue/white periods)</li>
        <li><strong>Extra:</strong> Works on TER trains in some regions</li>
        <li><strong>Best For:</strong> Students making 2-3+ long trips/year</li>
        <li><strong>Example:</strong> Paris-Marseille €65 → €45.50 (save €19.50)</li>
      </ul>
    </div>

    <h4>Carte Avantage (Adults)</h4>
    <ul>
      <li>30% discount on TGV and Intercités</li>
      <li>Applies to companion travelers too (up to 3 people)</li>
      <li>Kids travel for €9 with cardholder</li>
      <li>Weekend and holiday discounts</li>
    </ul>

    <h4>Carte Senior+ (60+)</h4>
    <ul>
      <li>30% discount on all TGV and Intercités</li>
      <li>Up to 60% discount on blue period days</li>
      <li>Companion gets 30% discount too</li>
      <li>Priority boarding on some trains</li>
    </ul>

    <h4>Carte Famille Nombreuse (Large Families)</h4>
    <ul>
      <li><strong>FREE card</strong> from government if you have 3+ children</li>
      <li>30% discount for parents</li>
      <li>30-75% discount for children (depending on age)</li>
      <li>All family members get discounts</li>
      <li>Unbeatable value for family travel</li>
    </ul>

    <h3>TGV Max - Unlimited Travel Subscription</h3>
    <div class="info-box tip">
      <h4>🎟️ Unlimited TGV for Young People</h4>
      <p><strong>Cost:</strong> €79/month or €869/year</p>
      <p><strong>Age:</strong> 16-27 years old</p>
      <p><strong>What's Included:</strong></p>
      <ul>
        <li>Unlimited TGV inOui journeys</li>
        <li>Book up to 7 days ahead (30 days for some routes)</li>
        <li>Subject to seat availability</li>
        <li>2nd class only</li>
        <li>Perfect for frequent travelers or gap year exploring France</li>
      </ul>
      <p><strong>Break-Even:</strong> 2-3 long-distance trips per month</p>
      <p><strong>Catch:</strong> Limited seats available per train, book early</p>
    </div>

    <h2>Detailed Route Information</h2>

    <h3>Paris - Lyon (France's Busiest Route)</h3>
    <table>
      <thead>
        <tr>
          <th>Train Type</th>
          <th>Duration</th>
          <th>Frequency</th>
          <th>From</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>TGV inOui</td>
          <td>1h 56m</td>
          <td>Every 30-60 min</td>
          <td>€16 (Prem's)</td>
          <td>From Paris Gare de Lyon</td>
        </tr>
        <tr>
          <td>OUIGO</td>
          <td>2h 00m</td>
          <td>6-8 daily</td>
          <td>€10</td>
          <td>From Paris Bercy or Marne-la-Vallée</td>
        </tr>
      </tbody>
    </table>

    <p><strong>Typical Daily Schedule:</strong></p>
    <ul>
      <li>First TGV: 06:00</li>
      <li>Peak hours: 07:00-09:00, 17:00-20:00 (most expensive)</li>
      <li>Off-peak (cheapest): 10:00-12:00, 14:00-16:00</li>
      <li>Last TGV: 22:00</li>
      <li>30+ trains daily</li>
    </ul>

    <h3>Paris - Marseille</h3>
    <table>
      <thead>
        <tr>
          <th>Train</th>
          <th>Duration</th>
          <th>From</th>
          <th>Frequency</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>TGV inOui Direct</td>
          <td>3h 15m</td>
          <td>€25</td>
          <td>Every 1-2 hours</td>
        </tr>
        <tr>
          <td>OUIGO</td>
          <td>3h 20m</td>
          <td>€16</td>
          <td>4-6 daily</td>
        </tr>
      </tbody>
    </table>

    <h3>Paris - Bordeaux (New High-Speed Line 2017)</h3>
    <table>
      <thead>
        <tr>
          <th>Train</th>
          <th>Duration</th>
          <th>From</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>TGV inOui</td>
          <td>2h 05m</td>
          <td>€16</td>
          <td>Was 3h 30m before 2017!</td>
        </tr>
        <tr>
          <td>OUIGO</td>
          <td>2h 10m</td>
          <td>€10</td>
          <td>Great value on this route</td>
        </tr>
      </tbody>
    </table>

    <h3>Paris - Nice (Mediterranean Connection)</h3>
    <table>
      <thead>
        <tr>
          <th>Train</th>
          <th>Duration</th>
          <th>From</th>
          <th>Frequency</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>TGV inOui Direct</td>
          <td>5h 30m</td>
          <td>€29</td>
          <td>Several daily</td>
        </tr>
        <tr>
          <td>Via Lyon</td>
          <td>6h 00m</td>
          <td>€25</td>
          <td>More departures</td>
        </tr>
        <tr>
          <td>OUIGO</td>
          <td>5h 45m</td>
          <td>€19</td>
          <td>2-3 daily</td>
        </tr>
      </tbody>
    </table>

    <h3>Paris - Strasbourg (Gateway to Germany)</h3>
    <table>
      <thead>
        <tr>
          <th>Train</th>
          <th>Duration</th>
          <th>From</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>TGV inOui</td>
          <td>1h 45m</td>
          <td>€16</td>
          <td>From Paris Est station</td>
        </tr>
        <tr>
          <td>OUIGO</td>
          <td>1h 50m</td>
          <td>€10</td>
          <td>Limited service</td>
        </tr>
      </tbody>
    </table>

    <h2>The 7 Paris Stations - Complete Guide</h2>

    <div class="info-box warning">
      <h4>⚠️ CRITICAL: Paris Has 7 Major Train Stations!</h4>
      <p>Each serves different destinations. Make ABSOLUTELY SURE you know which station your train departs from. Travel time between stations: 30-60 minutes!</p>
    </div>

    <h3>1. Gare du Nord - Northern France, Belgium, UK, Netherlands</h3>
    <ul>
      <li><strong>Destinations:</strong> Lille, Brussels, Amsterdam, London (Eurostar)</li>
      <li><strong>Trains:</strong> Eurostar, Thalys, TGV inOui, Intercités</li>
      <li><strong>Metro:</strong> Lines 4, 5</li>
      <li><strong>RER:</strong> Lines B, D, E</li>
      <li><strong>Note:</strong> Europe's busiest station - arrive 20-30 min early</li>
      <li><strong>Eurostar:</strong> Special check-in 45-60 min before departure (UK border control)</li>
    </ul>

    <h3>2. Gare de Lyon - Southeast France, Switzerland, Italy</h3>
    <ul>
      <li><strong>Destinations:</strong> Lyon, Marseille, Nice, Dijon, Geneva, Milan</li>
      <li><strong>Trains:</strong> TGV inOui, TGV Lyria, Intercités</li>
      <li><strong>Metro:</strong> Lines 1, 14</li>
      <li><strong>RER:</strong> Lines A, D</li>
      <li><strong>Famous:</strong> Le Train Bleu restaurant (beautiful Belle Époque)</li>
    </ul>

    <h3>3. Gare Montparnasse - West & Southwest France</h3>
    <ul>
      <li><strong>Destinations:</strong> Bordeaux, Nantes, Rennes, Brittany, Tours</li>
      <li><strong>Trains:</strong> TGV inOui, OUIGO, Intercités</li>
      <li><strong>Metro:</strong> Lines 4, 6, 12, 13</li>
      <li><strong>Modern:</strong> Rebuilt 1969, very modern and organized</li>
    </ul>

    <h3>4. Gare de l'Est - Eastern France, Germany, Luxembourg</h3>
    <ul>
      <li><strong>Destinations:</strong> Strasbourg, Reims, Nancy, Frankfurt, Munich</li>
      <li><strong>Trains:</strong> TGV inOui, ICE (German trains), Intercités</li>
      <li><strong>Metro:</strong> Lines 4, 5, 7</li>
      <li><strong>Historic:</strong> Built 1849, beautiful architecture</li>
    </ul>

    <h3>5. Gare Saint-Lazare - Normandy</h3>
    <ul>
      <li><strong>Destinations:</strong> Rouen, Le Havre, Caen, Vernon (Giverny)</li>
      <li><strong>Trains:</strong> Intercités, TER</li>
      <li><strong>Metro:</strong> Lines 3, 12, 13, 14</li>
      <li><strong>Art:</strong> Famous from Monet's paintings</li>
      <li><strong>Versailles:</strong> Nearby Transilien L to Versailles</li>
    </ul>

    <h3>6. Gare d'Austerlitz - Southwest France, Spain</h3>
    <ul>
      <li><strong>Destinations:</strong> Toulouse, Orléans, some overnight trains</li>
      <li><strong>Trains:</strong> Intercités, Intercités de Nuit, some TER</li>
      <li><strong>Metro:</strong> Lines 5, 10</li>
      <li><strong>RER:</strong> Line C</li>
      <li><strong>Note:</strong> Many services moved to Montparnasse; check your station!</li>
    </ul>

    <h3>7. Gare de Bercy - OUIGO, Italy</h3>
    <ul>
      <li><strong>Destinations:</strong> OUIGO departures, some Italian trains</li>
      <li><strong>Metro:</strong> Line 6, 14</li>
      <li><strong>Note:</strong> Smaller station, mainly OUIGO low-cost services</li>
      <li><strong>Location:</strong> Southeast Paris, near Bercy Village</li>
    </ul>

    <h3>Station Transfer Times (Approximate)</h3>
    <table>
      <thead>
        <tr>
          <th>From → To</th>
          <th>Best Method</th>
          <th>Time</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Gare du Nord → Gare de Lyon</td>
          <td>Metro Line 5</td>
          <td>25 min</td>
        </tr>
        <tr>
          <td>Gare du Nord → Montparnasse</td>
          <td>Metro Line 4</td>
          <td>35 min</td>
        </tr>
        <tr>
          <td>Gare de Lyon → Montparnasse</td>
          <td>Metro Line 14 + 6</td>
          <td>40 min</td>
        </tr>
        <tr>
          <td>Any → Any (taxi)</td>
          <td>Taxi/Uber</td>
          <td>15-30 min (traffic dependent)</td>
        </tr>
      </tbody>
    </table>

    <h2>Regional Travel - TER Trains</h2>

    <h3>Provence & Côte d'Azur</h3>
    <p><strong>Scenic coastal and lavender field routes:</strong></p>
    <table>
      <thead>
        <tr>
          <th>Route</th>
          <th>Duration</th>
          <th>Cost</th>
          <th>Frequency</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Marseille - Nice</td>
          <td>2h 30m</td>
          <td>€24</td>
          <td>Hourly</td>
        </tr>
        <tr>
          <td>Nice - Monaco</td>
          <td>20 min</td>
          <td>€4.50</td>
          <td>Every 20 min</td>
        </tr>
        <tr>
          <td>Nice - Cannes</td>
          <td>30 min</td>
          <td>€7</td>
          <td>Every 30 min</td>
        </tr>
        <tr>
          <td>Avignon - Arles</td>
          <td>20 min</td>
          <td>€8</td>
          <td>Every 1-2 hours</td>
        </tr>
      </tbody>
    </table>

    <h3>Loire Valley</h3>
    <table>
      <thead>
        <tr>
          <th>Route</th>
          <th>Duration</th>
          <th>Cost</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Tours - Blois</td>
          <td>35 min</td>
          <td>€11</td>
        </tr>
        <tr>
          <td>Tours - Amboise</td>
          <td>20 min</td>
          <td>€6</td>
        </tr>
        <tr>
          <td>Orléans - Blois</td>
          <td>40 min</td>
          <td>€12</td>
        </tr>
      </tbody>
    </table>

    <h3>Brittany</h3>
    <table>
      <thead>
        <tr>
          <th>Route</th>
          <th>Duration</th>
          <th>Cost</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Rennes - Saint-Malo</td>
          <td>1h 00m</td>
          <td>€15</td>
        </tr>
        <tr>
          <td>Nantes - Saint-Nazaire</td>
          <td>45 min</td>
          <td>€10</td>
        </tr>
        <tr>
          <td>Quimper - Brest</td>
          <td>1h 10m</td>
          <td>€16</td>
        </tr>
      </tbody>
    </table>

    <h3>Regional Day Passes</h3>
    <table>
      <thead>
        <tr>
          <th>Region</th>
          <th>Pass Name</th>
          <th>Cost</th>
          <th>Coverage</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Provence</td>
          <td>TER Sud Day Pass</td>
          <td>€24</td>
          <td>Unlimited TER in PACA region</td>
        </tr>
        <tr>
          <td>Brittany</td>
          <td>TER Bretagne Weekend</td>
          <td>€15</td>
          <td>Weekends only, unlimited</td>
        </tr>
        <tr>
          <td>Normandy</td>
          <td>TER Normandie Day</td>
          <td>€20</td>
          <td>All TER trains in region</td>
        </tr>
      </tbody>
    </table>

    <h2>International Connections from France</h2>

    <h3>Eurostar - France to UK</h3>
    <table>
      <thead>
        <tr>
          <th>Route</th>
          <th>Duration</th>
          <th>From</th>
          <th>Frequency</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Paris - London</td>
          <td>2h 15m</td>
          <td>€58</td>
          <td>15-20 daily</td>
        </tr>
        <tr>
          <td>Lille - London</td>
          <td>1h 20m</td>
          <td>€48</td>
          <td>5-8 daily</td>
        </tr>
        <tr>
          <td>Lyon - London</td>
          <td>4h 40m</td>
          <td>€79</td>
          <td>1-2 daily (seasonal)</td>
        </tr>
      </tbody>
    </table>

    <p><strong>Eurostar Tips:</strong></p>
    <ul>
      <li>Arrive 45-60 min before departure (UK border control in Paris)</li>
      <li>Security screening like airport</li>
      <li>Passport required (Brexit = stamping)</li>
      <li>Book 3-4 months ahead for €58 tickets</li>
      <li>Last-minute tickets can be €300+</li>
    </ul>

    <h3>Thalys - France to Belgium/Netherlands/Germany</h3>
    <table>
      <thead>
        <tr>
          <th>Route</th>
          <th>Duration</th>
          <th>From</th>
          <th>Frequency</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Paris - Brussels</td>
          <td>1h 22m</td>
          <td>€29</td>
          <td>Every 1-2 hours</td>
        </tr>
        <tr>
          <td>Paris - Amsterdam</td>
          <td>3h 20m</td>
          <td>€35</td>
          <td>8-10 daily</td>
        </tr>
        <tr>
          <td>Paris - Cologne</td>
          <td>3h 20m</td>
          <td>€39</td>
          <td>6-8 daily</td>
        </tr>
      </tbody>
    </table>

    <h3>TGV Lyria - France to Switzerland</h3>
    <table>
      <thead>
        <tr>
          <th>Route</th>
          <th>Duration</th>
          <th>From</th>
          <th>Frequency</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Paris - Geneva</td>
          <td>3h 05m</td>
          <td>€29</td>
          <td>8-10 daily</td>
        </tr>
        <tr>
          <td>Paris - Zurich</td>
          <td>4h 05m</td>
          <td>€39</td>
          <td>6-8 daily</td>
        </tr>
        <tr>
          <td>Paris - Lausanne</td>
          <td>3h 40m</td>
          <td>€35</td>
          <td>6-8 daily</td>
        </tr>
        <tr>
          <td>Lyon - Geneva</td>
          <td>2h 00m</td>
          <td>€25</td>
          <td>Several daily</td>
        </tr>
      </tbody>
    </table>

    <h3>TGV to Spain & Italy</h3>
    <table>
      <thead>
        <tr>
          <th>Route</th>
          <th>Duration</th>
          <th>From</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Paris - Barcelona</td>
          <td>6h 30m</td>
          <td>€49</td>
          <td>2 daily direct</td>
        </tr>
        <tr>
          <td>Lyon - Barcelona</td>
          <td>5h 00m</td>
          <td>€39</td>
          <td>Scenic route</td>
        </tr>
        <tr>
          <td>Paris - Milan</td>
          <td>7h 00m</td>
          <td>€45</td>
          <td>2 daily via Lyon</td>
        </tr>
        <tr>
          <td>Marseille - Milan</td>
          <td>5h 30m</td>
          <td>€39</td>
          <td>Via Nice, scenic</td>
        </tr>
      </tbody>
    </table>

    <h2>Booking Strategy Guide</h2>

    <div class="info-box">
      <h4>📅 When to Book for Maximum Savings</h4>

      <p><strong>Booking Timeline:</strong></p>
      <ol>
        <li><strong>4-6 months ahead:</strong> Prem's and OUIGO tickets released - BEST PRICES</li>
        <li><strong>3 months ahead:</strong> Good Prem's selection remaining</li>
        <li><strong>1-2 months ahead:</strong> Limited Prem's, standard fares available</li>
        <li><strong>2-4 weeks ahead:</strong> Mainly standard and Flex fares, expensive</li>
        <li><strong>Last week:</strong> Expect 2-3x higher prices, limited availability</li>
        <li><strong>Day before/same day:</strong> Only Flex fares, very expensive</li>
      </ol>

      <p><strong>Best Travel Times (Cheapest):</strong></p>
      <ul>
        <li><strong>Time of day:</strong> Mid-morning (10:00-12:00), mid-afternoon (14:00-16:00)</li>
        <li><strong>Days:</strong> Tuesday, Wednesday, Thursday</li>
        <li><strong>Avoid:</strong> Friday evening, Sunday afternoon/evening</li>
        <li><strong>Seasonality:</strong> January-March (except school holidays) cheapest</li>
      </ul>

      <p><strong>Most Expensive Times:</strong></p>
      <ul>
        <li>Friday 17:00-21:00 (weekend departures)</li>
        <li>Sunday 16:00-22:00 (weekend returns)</li>
        <li>Peak summer: July-August</li>
        <li>School holidays: February, Easter, July-August, Christmas</li>
        <li>Public holidays and bridges (ponts)</li>
      </ul>

      <p><strong>Decision Tree:</strong></p>
      <ul>
        <li><strong>Budget priority, fixed plans?</strong> → OUIGO (book 4+ months ahead)</li>
        <li><strong>Comfort + price, fixed plans?</strong> → Prem's (book 3-4 months ahead)</li>
        <li><strong>Making 2+ trips, under 27/60+?</strong> → Buy discount card FIRST, then book</li>
        <li><strong>Uncertain schedule, need flexibility?</strong> → Seconde or Flex fare</li>
        <li><strong>Last minute, uncertain?</strong> → Flex fare (expensive but only option)</li>
        <li><strong>Regional/local travel?</strong> → TER trains (buy at station, no advance needed)</li>
        <li><strong>Under 27, travel a lot?</strong> → Consider TGV Max (€79/month unlimited)</li>
      </ul>
    </div>

    <h2>Real User Scenarios with Cost Breakdowns</h2>

    <h3>Scenario 1: Paris-Lyon-Marseille Triangle (1 Week)</h3>
    <p><strong>Itinerary:</strong> Paris → Lyon (2 nights) → Marseille (3 nights) → Paris</p>
    <table>
      <thead>
        <tr>
          <th>Option</th>
          <th>Details</th>
          <th>Total Cost</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>OUIGO (4 months ahead)</strong></td>
          <td>All 3 journeys OUIGO</td>
          <td>€30 (€10 + €10 + €10)</td>
        </tr>
        <tr>
          <td><strong>Prem's (3 months ahead)</strong></td>
          <td>All 3 journeys Prem's</td>
          <td>€54 (€16 + €13 + €25)</td>
        </tr>
        <tr>
          <td><strong>Seconde (1 month ahead)</strong></td>
          <td>Standard booking</td>
          <td>€170 (€55 + €45 + €70)</td>
        </tr>
        <tr>
          <td><strong>Last minute Flex</strong></td>
          <td>Booked 1 week before</td>
          <td>€340 (€120 + €85 + €135)</td>
        </tr>
        <tr>
          <td><strong>With Carte Jeune</strong></td>
          <td>€50 card + 30% off Seconde</td>
          <td>€169 (€50 + €119)</td>
        </tr>
      </tbody>
    </table>
    <p><strong>Winner:</strong> OUIGO advance booking saves €310 vs. last minute!</p>

    <h3>Scenario 2: Weekend in Bordeaux from Paris</h3>
    <p><strong>Trip:</strong> Friday evening departure, Sunday return</p>
    <table>
      <thead>
        <tr>
          <th>Booking Time</th>
          <th>Fare Type</th>
          <th>Friday Out</th>
          <th>Sunday Return</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>3 months ahead</td>
          <td>Prem's</td>
          <td>€25</td>
          <td>€29</td>
          <td>€54</td>
        </tr>
        <tr>
          <td>1 month ahead</td>
          <td>Seconde</td>
          <td>€75</td>
          <td>€85</td>
          <td>€160</td>
        </tr>
        <tr>
          <td>1 week ahead</td>
          <td>Flex</td>
          <td>€125</td>
          <td>€135</td>
          <td>€260</td>
        </tr>
        <tr>
          <td>3 months (OUIGO)</td>
          <td>Low-cost</td>
          <td>€16</td>
          <td>€19</td>
          <td>€35</td>
        </tr>
      </tbody>
    </table>
    <p><strong>Winner:</strong> OUIGO saves €225 vs. last-minute booking! (But check station locations)</p>

    <h3>Scenario 3: Tour de France (Paris-Lyon-Nice-Marseille-Paris, 2 Weeks)</h3>
    <p><strong>4 long-distance journeys</strong></p>
    <table>
      <thead>
        <tr>
          <th>Strategy</th>
          <th>Cost Breakdown</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>All OUIGO</td>
          <td>€10 + €19 + €10 + €16</td>
          <td>€55</td>
        </tr>
        <tr>
          <td>All Prem's</td>
          <td>€16 + €29 + €13 + €25</td>
          <td>€83</td>
        </tr>
        <tr>
          <td>All Seconde</td>
          <td>€55 + €80 + €35 + €70</td>
          <td>€240</td>
        </tr>
        <tr>
          <td>With Carte Jeune</td>
          <td>€50 + (€240 × 0.7)</td>
          <td>€218</td>
        </tr>
        <tr>
          <td>TGV Max (if 16-27)</td>
          <td>€79/month</td>
          <td>€79</td>
        </tr>
      </tbody>
    </table>
    <p><strong>Winner:</strong> OUIGO if comfortable with restrictions, TGV Max if qualify by age!</p>

    <h3>Scenario 4: Business Commute Paris-Lyon (Weekly)</h3>
    <p><strong>Travel:</strong> 2 round trips per week (8 journeys/month)</p>
    <table>
      <thead>
        <tr>
          <th>Option</th>
          <th>Monthly Cost</th>
          <th>Annual Cost</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Flex fare (no card)</td>
          <td>€880 (€110 × 8)</td>
          <td>€10,560</td>
        </tr>
        <tr>
          <td>Seconde advance booking</td>
          <td>€480 (€60 × 8)</td>
          <td>€5,760</td>
        </tr>
        <tr>
          <td>Seconde + Carte Avantage</td>
          <td>€336 + €4.08 (card)</td>
          <td>€4,081</td>
        </tr>
        <tr>
          <td>OUIGO advance (inflexible)</td>
          <td>€160 (€20 × 8)</td>
          <td>€1,920</td>
        </tr>
      </tbody>
    </table>
    <p><strong>Winner:</strong> Carte Avantage + advance booking saves €6,479/year vs. Flex!</p>

    <h2>Pro Tips from Frequent Travelers</h2>

    <div class="info-box tip">
      <h4>🎯 Insider Secrets</h4>

      <p><strong>Booking Hacks:</strong></p>
      <ul>
        <li><strong>Set SNCF price alerts:</strong> App notifies when prices drop</li>
        <li><strong>Tuesday morning magic:</strong> SNCF often releases promotions Tuesdays 08:00</li>
        <li><strong>Split tickets:</strong> Paris-Lyon + Lyon-Marseille can be cheaper than Paris-Marseille direct</li>
        <li><strong>OUIGO hidden gem:</strong> Marne-la-Vallée departures often €5-10 cheaper than Bercy</li>
        <li><strong>Last-minute same-day:</strong> Check OUIGO - sometimes €10 seats remain!</li>
        <li><strong>iDTGV (old):</strong> Now called OUIGO but some old tickets still valid</li>
      </ul>

      <p><strong>Station Survival:</strong></p>
      <ul>
        <li><strong>Paris station confusion:</strong> Arrive 30+ min early first time, stations are spread out</li>
        <li><strong>Gare de Lyon trick:</strong> Platforms announced last minute - stay alert!</li>
        <li><strong>Luggage:</strong> Overhead racks fill fast - board early on busy trains</li>
        <li><strong>Food:</strong> Buy before boarding - bar car prices 2-3x higher</li>
        <li><strong>Gare du Nord pickpockets:</strong> VERY common, watch your belongings!</li>
      </ul>

      <p><strong>On-Board Tips:</strong></p>
      <ul>
        <li><strong>Espace Silence:</strong> Quiet car - perfect for work/rest</li>
        <li><strong>Seat recline:</strong> Button on armrest, reclines far back</li>
        <li><strong>WiFi:</strong> Free but slow - download content beforehand</li>
        <li><strong>Première class snack:</strong> Hot drink + snack included, ask attendant</li>
        <li><strong>Power outlets:</strong> Between seats or under armrest</li>
      </ul>

      <p><strong>Delay Compensation:</strong></p>
      <ul>
        <li><strong>30-59 min delay:</strong> 25% refund (TGV only)</li>
        <li><strong>60-119 min:</strong> 50% refund</li>
        <li><strong>120+ min or cancellation:</strong> 75% refund</li>
        <li><strong>Claim online:</strong> SNCF Connect app or website within 2 months</li>
        <li><strong>Flex ticket:</strong> Can take any other train if delayed</li>
      </ul>

      <p><strong>Hidden Savings:</strong></p>
      <ul>
        <li><strong>Prem's batches:</strong> More released 30 days before departure - check again!</li>
        <li><strong>Last-minute deals:</strong> Sometimes Friday afternoon promotions for weekend travel</li>
        <li><strong>Return ticket:</strong> No discount (unlike UK) - book each way separately</li>
        <li><strong>Group travel (4+ people):</strong> Special rates available, book via station</li>
        <li><strong>Night trains:</strong> Save hotel cost - Paris-Nice overnight from €19</li>
      </ul>
    </div>

    <h2>Accessibility & Special Services</h2>
    <ul>
      <li><strong>Accès Plus:</strong> Free assistance service - book 24-48h ahead</li>
      <li><strong>Phone:</strong> 0890 640 650 or +33 890 640 650 (international)</li>
      <li><strong>Wheelchair spaces:</strong> All TGV inOui trains</li>
      <li><strong>Guide dogs:</strong> Travel free</li>
      <li><strong>Elevators:</strong> Major stations equipped</li>
      <li><strong>Priority boarding:</strong> Available with Carte Senior+</li>
      <li><strong>Visual/hearing assistance:</strong> Station staff trained</li>
    </ul>

    <h2>FAQs - France Rail Travel</h2>

    <details>
      <summary><strong>Do I need to book TGV tickets in advance?</strong></summary>
      <p><strong>Highly recommended!</strong> Prem's and OUIGO fares sell out fast and prices increase dramatically as trains fill. For TGV inOui, last-minute tickets can be 3-4x more expensive. Book 3-4 months ahead for best prices.<br><br><strong>TER regional trains:</strong> NO advance booking needed - buy at station same day.</p>
    </details>

    <details>
      <summary><strong>Should I choose OUIGO or TGV inOui?</strong></summary>
      <p><strong>OUIGO if:</strong> Budget priority, don't need bar car, okay with luggage restrictions, comfortable with secondary stations<br><br><strong>TGV inOui if:</strong> Value comfort, want central stations, need flexibility, prefer bar car, have multiple bags<br><br>Price difference: OUIGO typically 30-50% cheaper but with trade-offs.</p>
    </details>

    <details>
      <summary><strong>How do I know which Paris station to go to?</strong></summary>
      <p>Your ticket ALWAYS shows the station. Generally:<ul><li><strong>Gare du Nord:</strong> North (Lille, Brussels, London)</li><li><strong>Gare de Lyon:</strong> Southeast (Lyon, Marseille, Nice, Geneva)</li><li><strong>Montparnasse:</strong> West/Southwest (Bordeaux, Brittany)</li><li><strong>Gare de l'Est:</strong> East (Strasbourg, Germany)</li></ul>Allow 30-60 min to transfer between stations!</p>
    </details>

    <details>
      <summary><strong>Are discount cards worth it for tourists?</strong></summary>
      <p><strong>Carte Jeune/Senior+ (€49-50/year):</strong> Break-even at ~€165 in tickets. Worth it if making 2+ long-distance trips.<br><br><strong>TGV Max (€79/month, ages 16-27):</strong> Excellent value if making 3+ trips per month or touring France intensively.<br><br><strong>Calculate your routes:</strong> Add up ticket costs with 30% discount to see if card pays off.</p>
    </details>

    <details>
      <summary><strong>Can I get a refund if I miss my train?</strong></summary>
      <p>Depends on fare type:<ul><li><strong>Prem's:</strong> Non-refundable, non-changeable - ticket lost</li><li><strong>Seconde:</strong> Can change with €15 fee before departure, partial refund</li><li><strong>Flex:</strong> Full refund or take any other train same day</li><li><strong>OUIGO:</strong> Usually non-refundable, some allow changes with €10 fee</li></ul>If train is delayed/cancelled (SNCF's fault), all tickets can be used on next available train.</p>
    </details>

    <details>
      <summary><strong>How early should I arrive at the station?</strong></summary>
      <p><ul><li><strong>TGV inOui/OUIGO (domestic):</strong> 15-20 minutes</li><li><strong>Eurostar (London):</strong> 45-60 minutes (border control)</li><li><strong>TER regional trains:</strong> 5-10 minutes</li><li><strong>First time at Paris station:</strong> Add 10-15 minutes</li><li><strong>Gare du Nord (crowded):</strong> 25-30 minutes</li></ul></p>
    </details>

    <h2>Useful Apps & Websites</h2>
    <ul>
      <li><strong>SNCF Connect:</strong> Official app - booking, tickets, real-time (iOS & Android)</li>
      <li><strong>OUIGO:</strong> Separate app/website - <a href="https://www.ouigo.com" target="_blank">ouigo.com</a></li>
      <li><strong>Eurostar:</strong> <a href="https://www.eurostar.com" target="_blank">eurostar.com</a> - UK bookings</li>
      <li><strong>Thalys:</strong> <a href="https://www.thalys.com" target="_blank">thalys.com</a> - Belgium/Netherlands</li>
      <li><strong>Trainline:</strong> Third-party comparison (small fee)</li>
      <li><strong>Omio:</strong> Multi-modal comparison</li>
      <li><strong>TGV Lyria:</strong> <a href="https://www.tgv-lyria.com" target="_blank">tgv-lyria.com</a> - Switzerland</li>
    </ul>

    <div class="info-box">
      <h4>🎉 Final Tips for France Train Travel</h4>
      <p><strong>Remember:</strong></p>
      <ul>
        <li>Book TGV 3-4 months ahead for Prem's/OUIGO bargains</li>
        <li>Check which Paris station BEFORE you travel</li>
        <li>OUIGO = ultra-budget but check station location carefully</li>
        <li>Discount cards pay off quickly if making 2+ trips</li>
        <li>TER regional trains need no advance booking</li>
        <li>Gare du Nord = pickpocket central, watch belongings</li>
        <li>Friday evening & Sunday afternoon = premium prices</li>
        <li>Le Train Bleu at Gare de Lyon = must-see even if not eating</li>
        <li>TGV = world's best train experience, enjoy the ride! 🇫🇷</li>
      </ul>
    </div>

  </div>
</template>

<script setup>
// France railway guide component
</script>

<style scoped>
details {
  margin: 1rem 0;
  padding: 1rem;
  background-color: #f5f5f5;
  border-left: 4px solid var(--secondary-color);
  border-radius: 4px;
}

summary {
  cursor: pointer;
  font-weight: 600;
  color: var(--primary-color);
  padding: 0.5rem 0;
}

summary:hover {
  color: var(--secondary-color);
}

details[open] summary {
  margin-bottom: 1rem;
  border-bottom: 1px solid var(--border-color);
}

details p {
  margin-top: 0.5rem;
}

details ul {
  margin-left: 1.5rem;
  margin-top: 0.5rem;
}
</style>
