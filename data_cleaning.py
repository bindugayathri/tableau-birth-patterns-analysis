import pandas as pd
import numpy as np

# Step 1: Load the data from the CSV file
df = pd.read_csv('birthdays.csv')

# Step 2: Map the numerical 'day_of_week' and 'month' to their corresponding names
day_of_week_map = {
    1: 'Mon',
    2: 'Tue',
    3: 'Wed',
    4: 'Thu',
    5: 'Fri',
    6: 'Sat',
    7: 'Sun'
}
df['day_of_week_name'] = df['day_of_week'].map(day_of_week_map)

month_map = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}
df['month_name'] = df['month'].map(month_map)

# Step 3: Aggregate the data and reshape it for the heatmap
df_pivot = df.pivot_table(values='births', index='month_name', columns='day_of_week_name', aggfunc='mean')

# Step 4: Reorder the months and days to be in chronological order
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

df_pivot = df_pivot.reindex(index=month_order, columns=day_order)

# Step 5: Save the cleaned DataFrame to a new CSV file
# This will save the file in the same folder as your Python script.
df_pivot.to_csv('cleaned_birthdays.csv')

print("The cleaned data has been saved to 'cleaned_birthdays.csv'")