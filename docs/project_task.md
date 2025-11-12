<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

/* Typography base */
* { font-family: 'Montserrat', sans-serif !important; }

html, body {
    font-family: 'Montserrat', sans-serif !important;
    font-size: 14px; /* Slightly larger for readability */
    line-height: 1.35;
}

h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    margin-top: 14px;
    margin-bottom: 8px;
}

h1 { font-size: 26px !important; }
h2 { font-size: 22px !important; }

p, span, div, li, blockquote, pre {
    font-size: 14px;
}

code {
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace !important;
    color: green;
    background-color: #f8f9fa;
    padding: 1px 3px;
    border-radius: 3px;
}

a, a:hover, a:visited { font-family: 'Montserrat', sans-serif !important; }
strong, b, em, i { font-family: 'Montserrat', sans-serif !important; }

ul, ol, dl {
    padding-left: 20px;
    margin-top: 4px;
    margin-bottom: 4px;
}

/* Compact table layout */
table {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    font-size: 5px; /* Extra compact table text */
}

th, td {
    padding: 0; /* Ultra-tight padding */
    border: 1px solid #e5e7eb;
    vertical-align: top;
    word-break: break-word;
    font-size: 5px; /* Ensure cells use compact size */
    line-height: 1;
}

/* Reduce horizontal padding specifically for header cells */
th {
    padding: 0; /* No extra padding on headers */
}

/* Trim spacing of the info box without touching content */
div[style*="border-left: 4px solid #0e4378"] {
    padding: 10px !important;
    margin: 12px 0 !important;
    border-radius: 6px !important;
}
</style>

<img src="pics/tum_logo.svg" alt="TUM Logo" width="60" align="right">

<div style="font-family: 'Montserrat', sans-serif;">

# **Project Task Analysis**

> Project Task for Citi Bike Trip Histories

<div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #0e4378; margin: 20px 0;">
<strong>Group:</strong> 11  <br/>
</div>

## <span id="domain-situation" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #2C3E50; border-bottom: 2px solid #0e4378; padding-bottom: 8px; display: block;">A. Domain Situation: User Stories</span>

Here are five user stories speculating on the tasks of typical users for the Citi Bike dataset. The overarching theme is **"Understanding and optimizing Citi Bike usage patterns and operational efficiency in NYC."**

1.  **Persona:** Sarah, a marketing analyst for Citi Bike.
    * **Task/Question:** Sarah is planning a new campaign to convert "casual" riders into "member" riders. To target this campaign effectively, she needs to know: **"How do member and casual users differ in their riding activity across hours of the day and days of the week?"**

2.  **Persona:** Chen, an urban planner for the NYC Department of Transportation (DOT).
    * **Task/Question:** Chen is evaluating the impact of existing bike lanes and assessing the need for new ones. He needs to understand traffic flow and requires an answer to: **"What are the most common origin-destination routes based on geographic coordinates? Which routes are most popular during peak commuter hours?"**

3.  **Persona:** Alex, an operations manager for Citi Bike (similar to the "Max" example).
    * **Task/Question:** Alex is responsible for "rebalancing" stations—moving bikes from full stations to empty ones. He needs to optimize his truck routes and schedules. His daily question is: **"Which stations are the most popular start stations and end stations? What is the net inflow/outflow of bikes for the top 20 busiest stations during morning (7-10 AM) and evening (5-7 PM) rush hours?"** (Uses `start_station_id` and `end_station_id`).

4.  **Persona:** Priya, a data quality analyst for the Citi Bike tech team.
    * **Task/Question:** Priya must monitor the system for data errors or anomalous usage that could indicate software bugs or bike malfunctions. She needs to address the known issue of outliers. Her task is to ask: **"What is the distribution of trip durations? Are there significant numbers of trips that are too short (< 60 seconds) or too long (> 24 hours), and how are these outliers distributed across different `rideable_type`s?"**

5.  **Persona:** David, a fleet maintenance supervisor for Citi Bike.
    * **Task/Question:** David manages the maintenance schedules for different bike models. He knows that electric bikes (`rideable_type`) have different usage patterns and can be parked anywhere, leading to missing end station data. He needs to know: **"How does the usage of electric bikes differ from classic bikes in terms of average trip duration and common parking zones (using `end_lat`, `end_lng`), especially for trips that do not end at a designated station?"**

---

## <span id="task-abstraction" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #2C3E50; border-bottom: 2px solid #0e4378; padding-bottom: 8px; display: block;">B. Task Abstraction</span>

Here is a task abstraction for two of the user stories.

### User Story 1: Marketing Analysis

> **Story:** "Sarah (Marketing) needs to know: 'How do member and casual users differ in their riding activity across hours of the day and days of the week?'"

**Abstraction:**
* **High level:** **Discover**. (The user is asking "how" things differ, which is exploratory, similar to Scenario 6: "How do... distributions differ?").
* **Mid/Search:** **Lookup**. (She knows the two groups she wants to compare: 'member' and 'casual'. This matches Scenario 6).
* **Low/Query:** **Compare**. (The keyword "differ" maps directly to this action).
* **Target:** **Distributions** (by group).
* **Final:** **Compare distributions**.

### User Story 2: Urban Planning

> **Story:** "Chen (Urban Planner) needs to know: 'What
are the most common origin-destination routes based on geographic coordinates?
Which routes are most popular during peak commuter hours?'"

**Abstraction:**
* **High level:** **Discover**. (The user is asking "what" or "which" are the "most", which is an exploratory discovery task, similar to Scenario 4: "...which directories account for the most total size?").
* **Mid/Search:** **Explore**. (The user does not know the target in advance; they are exploring the entire set to find the top items).
* **Low/Query:** **Summarize (Rank)**. (The solutions file uses "Rank" for "most" or "highest". The goal is to aggregate all trips and rank the resulting routes).
* **Target:** **Paths** (or Routes).
* **Final:** **Rank routes**. (Following the pattern of Scenario 4: "Rank directories").


<!-- ### User Story 3: Operations Management

> **Story:** "Alex (Ops) needs to know: 'Which stations are the most popular... and what is the net inflow/outflow...?'"

**Abstraction (for "most popular"):**
* **High level:** **Discover**. (Similar to Story 2, asking "which" are "most").
* **Mid/Search:** **Explore**. (Looking for unknown top items within the whole set, similar to Scenario 9: "Which pages have the highest...").
* **Low/Query:** **Summarize (Rank)**. (The goal is to rank stations by popularity/count).
* **Target:** **Nodes (Stations)**.
* **Final:** **Rank stations**.

### User Story 4: Data Quality

> **Story:** "Priya (DQ) needs to know: '...Are there significant numbers of... outliers...?'"

**Abstraction:**
* **High level:** **Discover**. (This is a classic discovery task, directly matching Scenario 10: "...which machines show outlier temperatures?").
* **Mid/Search:** **Explore**. (Priya must search through the data (e.g., all logs) to find unknown outliers).
* **Low/Query:** **Identify**. (The goal is to identify specific items that are outliers).
* **Target:** **Outliers**.
* **Final:** **Identify outliers**.

### User Story 5: Fleet Maintenance

> **Story:** "David (Maintenance) needs to know: 'How does the usage of electric bikes differ from classic bikes...?'"

**Abstraction:**
* **High level:** **Discover**. (This is the same "how do they differ" structure as Story 1 and Scenario 6).
* **Mid/Search:** **Lookup**. (He knows the two groups to compare: 'electric' and 'classic').
* **Low/Query:** **Compare**. (The keyword is "differ").
* **Target:** **Distributions** (or Trends).
* **Final:** **Compare distributions**. -->
  

</div>