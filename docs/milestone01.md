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

# **Milestone 01**

> Data Abstraction for Citi Bike Trip Histories

<div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #0e4378; margin: 20px 0;">
<strong>Group:</strong> 11  <br/>
</div>

## <span id="project-vision" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #2C3E50; border-bottom: 2px solid #0e4378; padding-bottom: 8px; display: block;">A. Title & Source</span>

-   **Dataset Title:** Citi Bike NYC System Data (JC-202509-citibike-tripdata)
-   **Primary URL:** [https://citibikenyc.com/system-data](https://citibikenyc.com/system-data)
-   **Publisher/Author:** Citi Bike NYC
-   **Publication/Last Update Date:** Oct 6th 2025
-   **License/Usage Terms:** [NYCBS Data Use Policy](https://www.citibikenyc.com/data-sharing-policy)

## <span id="project-timeline--milestones" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #2C3E50; border-bottom: 2px solid #0e4378; padding-bottom: 8px; display: block;">B. Motivation</span>

This dataset shows city travel patterns and how people use shared bikes and stations. Its rich temporal and spatial dimension make it ideal for exploring behavioral patterns and optimizing transportation systems. Two questions we aim to explore are: (1) How do member and casual users differ in their riding activity across hours of the day? (2) What are the most common origin-destination routes based on geographic coordinates?

## <span id="system-architecture" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #2C3E50; border-bottom: 2px solid #0e4378; padding-bottom: 8px; display: block;">C. Scope & Granularity</span>

Our dataset contains about 100k records, each with 13 attributes. Every record represents a single bike trip. The `ride_id` serves as the unique identifier for each trip, while `start_station_id` and `end_station_id` are key fields for linking the start and end points of the journeys.

## <span id="methodology--approach" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #2C3E50; border-bottom: 2px solid #0e4378; padding-bottom: 8px; display: block;">D. Schema (Types & Ranges)</span>

|            | ride_id   | rideable_type        | started_at | ended_at | start_station_name | start_station_id | end_station_name | end_station_id | start_lat   | start_lng       | end_lat   | end_lng   | member_casual       |
| ---------- | --------- | -------------------- | ---------- | -------- | ------------------ | ---------------- | ---------------- | -------------- | ----------- | --------------- | --------- | --------- | ------------------- |
| **Role**   | ID/Key    | Attr.                | Attr.      | Attr.    | Attr.              | ID/Key           | Attr.            | ID/Key         | Attr.       | Attr.           | Attr.     | Attr.     | Attr.               |
| **Type**   | Cat.      | Cat.                 | Quant.     | Quant.   | Cat.               | Cat.             | Cat.             | Cat.           | Quant.      | Quant.          | Quant.    | Quant.    | Cat.                |
| **T/S**    | N         | N                    | Y (T)      | Y (T)    | N                  | N                | N                | N              | Y (S)       | Y (S)           | Y (S)     | Y (S)     | N                   |
| **Domain** | ~110k IDs | {'classic_bike',...} | Datetime   | Datetime | ~100 stations      | e.g., 'JC005'    | ~100 stations    | e.g., 'JC008'  | 40.69-40.75 | -74.1 to -74.02 | (Similar) | (Similar) | {'member','casual'} |

## <span id="team-roles--responsibilities" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #2C3E50; border-bottom: 2px solid #0e4378; padding-bottom: 8px; display: block;">F. Quality & Limitations</span>

The main data quality issues are missing values and outliers. Some trips, particularly those with electric bikes, have no end station information because they can be parked anywhere; this is a real-world scenario we need to handle in our visualization. We also expect to find outliers in trip duration. To prepare the data, we will first calculate trip duration from the start and end times. Then, we will filter out very short trips (under 60 seconds) and very long ones (over 24 hours) to remove potential errors, and we will explicitly manage trips with missing end-station data.

## <span id="current-progress-and-future-plans" style="font-family: 'Montserrat', sans-serif; font-weight: 600; color: #2C3E50; border-bottom: 2px solid #0e4378; padding-bottom: 8px; display: block;">G. Suitability</span>

This dataset comes as a single CSV file, which makes it easy to start working with without much cleanup. However, with 100k records, it is large enough to reveal interesting patterns in urban mobility and to test the performance of our D3.js visualizations. The data is also rich, combining temporal, spatial, and network information. This variety allows us to create multiple types of visualizations, such as flow maps to explore and compare trip data effectively.

</div>
