import pandas as pd

# Assuming you have the dataset in a CSV file named 'health_data.csv'
data = pd.read_csv('cardio_base.csv')

# Find the height of the tallest 1% of people
tallest_1_percent_height = data['height'].quantile(0.99)

print("They are taller than {:.0f}cm".format(tallest_1_percent_height))
