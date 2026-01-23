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

# **Implementation: Interactive Visual System**

> Milestone 4: From Prototype to Working Visualization for Jersey City Citi Bike Analysis

<div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #0e4378; margin: 20px 0;">
<strong>Group:</strong> 11  <br/>
<strong>GitHub Repository:</strong> <a href="https://github.com/tsaichen1o/jc-citibike-vis">https://github.com/tsaichen1o/jc-citibike-vis</a>
</div>

The system follows the **Information Seeking Mantra**: *Overview first, zoom and filter, then details-on-demand*. The interface is structured into three coordinated zones:
- **Center:** A geographic map visualizing spatial flow.
- **Bottom:** A time-series chart for temporal trends and interactive filtering.
- **Side:** A dynamic ranking chart for station-level performance and connectivity analysis.

## Requirement 1: Views & Encodings
The implementation successfully encodes the data abstraction through coordinated visual marks and channels:

* **Spatial View (Map):** Station locations are encoded as `points` (position). Flows are implemented as `curved arcs`, where `line width` and `opacity` represent trip volume (magnitude), facilitating the identification of major transit corridors.
* **Temporal View (Line Chart):** Uses `position (vertical)` for trip counts and `position (horizontal)` for the 24-hour cycle. `Color hue` (Blue for Members, Orange for Casual) effectively distinguishes user demographics.
* **Ranking View (Bar Chart):** Utilizes `length` and `aligned vertical position`—the most effective channels for quantitative comparison—to rank station popularity and flow balance.

## Requirement 2: Interactions that Matter
We have implemented interactive features that enable direct task completion without ornamental clutter:

* **Brushing & Filtering:** Users can drag a selection box across the time-series chart. This `brush` interaction triggers an instant update of the Map and Bar Chart, allowing users to isolate specific periods like the morning rush hour.
* **Details-on-Demand:** Hovering over any visual mark (stations, arcs, or line nodes) reveals precise statistics via `tooltips`. Clicking a station expands a `detailed info panel` with balance metrics and peak usage data.
* **Search & Auto-Complete:** A search bar allows users to locate specific stations instantly, automatically centering the map and highlighting the station across all views.
* **Temporal Animation:** A "Play" button provides an automated walkthrough of the 24-hour cycle, visualizing the dynamic pulse of the city's bike flow.

## Requirement 3: State & Coordination
Centralized state management ensures the system remains synchronized:

* **Linked Views:** Selecting a station on the map or ranking list updates the entire dashboard. The line chart adapts to show that station's specific temporal profile, while the map filters to its "1-hop neighborhood" (direct connections).
* **Visible Active States:** The current filters are explicitly stated in a "Time Range" badge at the top. Selected stations are highlighted with a distinct `accent color` and increased `marker size` to maintain user context.
* **Global Reset:** A "Reset All" button returns the system to the global overview state, ensuring a clear path for exploratory re-navigation.

## 4. Quality Bar (Self-Check)

Our implementation has been evaluated against rigorous quality standards to ensure a professional and user-centric experience.

### Task Efficiency (≤ 3 Steps Principle)
The dashboard is designed for high operational efficiency, allowing users to extract insights with minimal friction. Primary tasks meet the requirement of being completed in three or fewer deliberate actions:
* **Task 1: Identifying Peak Hour Distributions:** A user can understand temporal trends in a single step by observing the pre-rendered 24-hour line chart.
* **Task 2: Analyzing Station Connectivity:** A user can explore a specific station's network in two steps: first, by searching for or clicking a station, and second, by observing the highlighted flow lines on the map. 
Both workflows demonstrate that the interface adheres to high-efficiency interaction standards.

### Clarity of System State
The system ensures that the active state—including what is filtered, selected, or sorted—is always obvious to the user. We achieve this through dynamic UI elements and descriptive labeling:
* **Dynamic Titling:** The Bar Chart title updates based on user selection. For example, it defaults to "Top 10 Popular Stations" (sorted in descending order of total traffic) and changes to reflect specific "Destinations" or "Origins" when a station is active.
* **Instructional Cues:** The temporal view is titled "24-Hour Ride Trends (Drag to filter time range)," providing an explicit hint that helps users utilize the timeline filter more effectively and intuitively.
* **Visual Highlighting:** Selected elements on the map and bar chart change color and size, providing immediate visual confirmation of the current focus.

### Performance & Responsiveness
To provide a fluid user experience, the system targets instant feedback (under 200 ms) for all common interactions. This is achieved through:
* **Efficient Data Handling:** The code utilizes D3’s data-binding (Join) patterns and hardware-accelerated Transition animations.
* **Asynchronous Updates:** All view modifications are driven through an asynchronous `updateCharts` function. Even with thousands of data points, the filtering logic remains highly responsive, ensuring the UI does not hang during data processing.

### Robustness & Edge Cases
The design includes specific measures to handle data scale and visual complexity:
* **Scaling Constraints:** The ranking chart is strictly limited to the "Top 10" items. This avoids UI crowding and ensures legibility even when the dataset contains hundreds of unique stations.
* **Visual De-cluttering:** The geographic map utilizes a "Bundled Arcs" design. By curving and grouping lines, the system significantly reduces visual chaos and overlap in high-density areas (such as downtown transport hubs), making the underlying patterns easier to discern.

<!-- <div style="page-break-after: always; visibility: hidden"> 
\pagebreak
</div>

### <span id="task1" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #34495E; border-bottom: 1px solid #BDC3C7; padding-bottom: 4px; display: block;">Task 1: Compare Distributions (Member vs. Casual Trends)</span>
The system enables users to identify behavioral differences between user groups. By observing the line chart, users can see that Members peak during commute hours (8 AM/5 PM), while Casual users show a smoother distribution throughout the day.

### <span id="task2" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #34495E; border-bottom: 1px solid #BDC3C7; padding-bottom: 4px; display: block;">Task 2: Summarize Flows (OD Connectivity)</span>
Using the curved arc map, the system reveals geographic patterns. Users can identify major routes (e.g., residential areas to transit hubs) through line thickness, with transparency handling high-density overlap.

### <span id="task3" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #34495E; border-bottom: 1px solid #BDC3C7; padding-bottom: 4px; display: block;">Task 3: Rank Stations (Identify Top Hubs)</span>
The bar chart reorders dynamically based on user filters. It helps planners identify which stations are the primary "sinks" or "sources" of bike traffic at any given time.

### <span id="task4" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #34495E; border-bottom: 1px solid #BDC3C7; padding-bottom: 4px; display: block;">Task 4: Analyze Connectivity (1-Hop Neighborhoods)</span>
When a station is selected, the map isolates its immediate network. This removes background noise and shows the specific "reach" of a station, helping to evaluate local network resilience.

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak
</div>

## <span id="project-vision" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #2C3E50; border-bottom: 2px solid #0e4378; padding-bottom: 8px; display: block;">Storyboard: Optimizing the Morning Commute</span>

**1. Global Overview:**
An urban planner opens the dashboard to see the full month's data. The initial view shows high density around Grove St and Newport.

<div style="text-align: center;">
  <img src="docs/pics/1.png" style="width: 60%;" alt="Dashboard Overview">
</div>

**2. Temporal Filtering:**
The planner notices a Member spike at 8 AM and brushes this range on the line chart. The map updates to show only rush-hour flows.

<div style="text-align: center;">
  <img src="docs/pics/2.png" style="width: 60%;" alt="Time Brush Filtering">
</div>

**3. Identifying Hubs:**
The Bar Chart reorders, revealing "Grove St PATH" as the top destination. The planner clicks this bar to isolate the station on the map.

<div style="text-align: center;">
  <img src="docs/pics/3.png" style="width: 60%;" alt="Station Ranking and Selection">
</div>

**4. Discovering Insights:**
By isolating Grove St's 1-hop neighborhood, the planner identifies a heavy flow from residential Hamilton Park, but a lack of connectivity from newer developments, suggesting a site for a new station.

<div style="text-align: center;">
  <img src="docs/pics/4.png" style="width: 60%;" alt="1-Hop Network Analysis">
</div> -->
</div>