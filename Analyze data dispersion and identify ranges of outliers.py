import pandas as pd
import numpy as np

# Assuming you have the dataset in a CSV file named 'health_data.csv'
data = pd.read_csv('cardio_base.csv')

# Calculate the mean and standard deviation of height
mean_height = data['height'].mean()
std_dev_height = data['height'].std()

# Find the upper and lower limits for 2 standard deviations from the mean
upper_limit = mean_height + 2 * std_dev_height
lower_limit = mean_height - 2 * std_dev_height

# Calculate the percentage of people who are beyond these limits
percentage_beyond_2_std_dev = ((data['height'] > upper_limit) | (data['height'] < lower_limit)).mean() * 100

print("The percentage of people who are beyond 2 standard deviations from the mean height is: {:.2f}%".format(percentage_beyond_2_std_dev))
