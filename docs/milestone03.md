<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Montserrat', sans-serif !important;
}

body, html {
    font-family: 'Montserrat', sans-serif !important;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 600;
}

p, span, div, li, td, th, blockquote, pre {
    font-family: 'Montserrat', sans-serif !important;
}

code {
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace !important;
    color: green;
    background-color: #f8f9fa;
    padding: 2px 4px;
    border-radius: 3px;
}

a, a:hover, a:visited {
    font-family: 'Montserrat', sans-serif !important;
}

strong, b, em, i {
    font-family: 'Montserrat', sans-serif !important;
}

ul, ol, dl {
    font-family: 'Montserrat', sans-serif !important;
}

table {
    font-family: 'Montserrat', sans-serif !important;
}

input, textarea, select, button {
    font-family: 'Montserrat', sans-serif !important;
}
</style>

<img src="pics/tum_logo.svg" alt="TUM Logo" width="60" align="right">

<div style="font-family: 'Montserrat', sans-serif;">

# **Prototyping Our Design**

> Prototyping Design for the Jersey City Citi Bike Analysis

<div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #0e4378; margin: 20px 0;">
<strong>Group:</strong> 11  <br/>
<strong>GitHub Repository:</strong> <a href="https://github.com/tsaichen1o/jc-citibike-vis">https://github.com/tsaichen1o/jc-citibike-vis</a>

</div>
Our dashboard will follow the rule: Overview first, zoom and filter, details on demand.

-   Center: A Geographic Map of Jersey City (Spatial context).
-   Bottom: A Time-Series Chart (Temporal context & filtering).
-   Side: A Ranking Chart (Details & filtering).

### <span id="who-is-it-for" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #34495E; border-bottom: 1px solid #BDC3C7; padding-bottom: 4px; display: block;">Task 1: Compare Distributions (Member vs. Casual Trends)</span>

**Goal:** Understand how riding behavior differs between user groups over time.

-   **Design Option A (Small Multiples):** Two vertically stacked area charts (one for Member, one for Casual).
    -   Good for seeing the individual "shape" of the day, but makes precise comparison of magnitude at specific hours difficult due to spatial separation.
-   **Design Option B (Baseline):** Superimposed Multi-Line Chart
    -   **Idiom:** A line chart with two lines plotted on the same axes.
    -   **Marks:** `Lines`.
    -   **Channels:**
        -   `Position (Vertical)`: Number of trips (Magnitude).
        -   `Position (Horizontal)`: Time of day (0-24h).
        -   `Color Hue`: User type (e.g., Blue for Member, Orange for Casual).
    -   **Interaction: Brushing**. The user can drag a selection box over a time range (e.g., 7-10 AM) to filter the Map and Bar Chart.
    -   Superposition allows for the most precise comparison of values. We can instantly see when casual riders might overtake members (e.g., weekends vs weekdays) or distinct commute peaks.

### <span id="who-is-it-for" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #34495E; border-bottom: 1px solid #BDC3C7; padding-bottom: 4px; display: block;">Task 2: Summarize Flows (OD Connectivity)</span>

**Goal:** Identify major geographic routes (OD Connectivity). Since we lack GPS traces, we visualize direct Origin-Destination (OD) connections (1-hop), not street-level paths.

-   **Design Option A (Straight Line Connection):** Straight lines connecting start and end stations.
    -   Creates a "hairball" effect in dense areas (like Grove St), causing high occlusion and making directionality hard to see.
-   **Design Option B (Baseline):** Bundled Arc Map
    -   **Idiom:** A geographic map with curved links.
    -   **Marks:** `Lines` (Curved Arcs).
    -   **Channels:**
        -   `Width`: Volume of trips on this route (Quantitative).
        -   `Opacity`: Lower opacity for less frequent routes to reduce clutter.
        -   `Curvature`: To bundle similar routes visually.
    -   **Interaction: Linked Filtering**. The map updates to show only flows corresponding to the time selected in Task 1.
    -   Curving the lines reduces occlusion over the central station nodes. By weighting thickness, the "major arteries" of the city commute become immediately visible against background noise.

### <span id="who-is-it-for" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #34495E; border-bottom: 1px solid #BDC3C7; padding-bottom: 4px; display: block;">Task 3: Rank Stations (Identify Top Hubs)</span>

**Goal:** Identify the most popular start and end points.

-   **Design Option A (Word Cloud):** Station names sized by trip count.
    -   Visually interesting but poor for ranking tasks. Long station names make it unreadable and precise comparison impossible.
-   **Design Option B (Baseline):** Ordered Bar Chart
    -   **Idiom:** Horizontal Bar Chart.
    -   **Marks:** `Lines` (Bars).
    -   **Channels:**
        -   `Length`: Total Trip Count (Quantitative).
        -   `Position (Vertical)`: Rank order (Ordinal).
    -   **Interaction: Selection (Highlighting)**. Clicking a bar filters the Map (Task 2) to show only trips related to that station.
    -   Aligned position and length are the most effective channels for comparing quantitative data. Horizontal alignment accommodates long station names.

### <span id="who-is-it-for" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #34495E; border-bottom: 1px solid #BDC3C7; padding-bottom: 4px; display: block;">Task 4: Analyze Connectivity (1-Hop Neighborhoods)</span>

**Goal:** Identify which stations act as central "hubs" and visualize their immediate connectivity range.

-   **Design Option A (Matrix View):** An adjacency matrix showing connections between all pairs of stations.
    -   With hundreds of stations, the matrix becomes too large to read effectively, losing the vital spatial context needed for urban planning.
-   **Design Option B (Baseline):** Node-Link Highlight (Star Plot on Map)
    -   **Idiom:** A spatial node-link diagram that focuses on a single selected node.
    -   **Marks:** `Points` (Stations) and `Lines` (Links).
    -   **Channels:**
        -   `Color Hue`: Distinguishes the selected "Origin" station from its connected "Destinations".
        -   `Line Width`: Flow volume to each specific destination.
    -   **Interaction: Click Selection**. Clicking a station isolates its "1-hop neighborhood"—showing only the direct links radiating from it, hiding all other background noise.
    -   This design directly addresses the "1-hop" constraint. Instead of showing a messy full network, it allows users to inspect the specific "fingerprint" of connectivity for any single station, revealing whether it is a local hub or a long-distance connector.

## <span id="project-vision" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #2C3E50; border-bottom: 2px solid #0e4378; padding-bottom: 8px; display: block;">Storyboard: Optimizing the Morning Commute</span>

> User: BardiC (Urban Planner) <br/>
> Goal: Determine if the current infrastructure supports the morning rush hour flow into the financial district.

**1. Overview**
BardiC opens the dashboard. She sees the Map showing flows for the entire month (messy) and the Line Chart showing the 24-hour cycle.

<div style="text-align: center;">
  <img src="pics/1.png" style="width: 60%;">
</div>

**2. Narrow Scope (Filtering)**
She notices a sharp spike in the "Member" line (Blue) on the Line Chart between 7:00 AM and 9:00 AM. She uses the Select tool to select this specific time window.

<div style="text-align: center;">
  <img src="pics/2.png" style="width: 60%;">
</div>

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak
</div>

**3. Inspect Details (Linked Update)**
The Flow Map automatically updates. The messy web of lines disappears, revealing thick arcs moving from residential areas (Hamilton Park) towards the transport hub (Grove St PATH). The Bar Chart reorders to show "Grove St" as the #1 destination.

<div style="text-align: center;">
  <img src="pics/3.png" style="width: 60%;">
</div>

**4. Capture Insight (Service Gaps)**
She clicks "Grove St" on the Bar Chart to isolate it. The map filters to show only the 1-hop connections for Grove St. She sees that while it receives traffic from everywhere, there is a missing link from a new residential development in the west, indicating a potential need for a new connecting bike lane.

<div style="text-align: center;">
  <img src="pics/4.png" style="width: 60%;">
</div>
</div>
