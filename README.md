# Analysis of U.S. Birth Patterns (1994-2014)

This project analyzes over two decades of U.S. birth data to visualize daily and monthly patterns. The final output is an interactive radial heatmap created in Tableau that reveals key trends in when babies are born.

## About the Data

The dataset used contains information on all births in the United States from 1994 to 2014. It was sourced from the Centers for Disease Control and Prevention (CDC) and made available by FiveThirtyEight. The raw data includes the year, month, day of the week, and the total number of births for that day.

## Project Methodology

1.  **Data Cleaning & Preparation**: The initial dataset was cleaned and aggregated using **Python**. A script was used to calculate the average number of births for each day of the week (e.g., all Mondays in January) across the 20-year period. This new, summarized dataset (`cleaned_birthdays.csv`) was then used for visualization.

2.  **Visualization**: The data was visualized in **Tableau** using a radial heatmap. This chart type was chosen for its ability to effectively display cyclical data (the months of the year).
    * **X/Y Coordinates** were calculated from the month and day of the week to position marks in a circle.
    * **Color and Size** are used to represent the average number of births, with pink indicating a high number and blue indicating a low number.
    * An **interactive tooltip** and **month filter** were added to the final dashboard for user-driven exploration.

## Key Insights & Findings

The visualization clearly highlights several profound trends:

1.  **The Weekday vs. Weekend Divide**: There is a significant drop in births on Saturdays and Sundays. This strongly suggests the influence of scheduled medical procedures (C-sections, induced labor) which are typically planned for standard business days.

2.  **Seasonal Birth Patterns**: A "baby season" is clearly visible in the summer months, with **July, August, and September** showing the highest average number of births.

3.  **Tuesday as the Peak Day**: Across many months, Tuesday stands out as the most popular day of the week for births.

## Technologies Used

* **Python**: For data cleaning and aggregation.
* **Tableau**: For data visualization and dashboard creation.<img width="1917" height="1001" alt="Screenshot 2025-08-20 141255" src="https://github.com/user-attachments/assets/200c25d9-84a2-4b4a-9c56-98760e76ba93" />
