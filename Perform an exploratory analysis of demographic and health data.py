import pandas as pd

# Assuming you have the dataset in a CSV file named 'health_data.csv'
data = pd.read_csv('cardio_base.csv')

# Round age down
data['age'] = data['age'].apply(lambda x: int(x))

# Calculate the average weight per age group
average_weight_by_age = data.groupby('age')['weight'].mean()

# Find the age with the highest average weight and the age with the lowest average weight
age_with_highest_weight = average_weight_by_age.idxmax()
age_with_lowest_weight = average_weight_by_age.idxmin()

# Calculate the difference in weight between age groups
difference_in_weight = average_weight_by_age[age_with_highest_weight] - average_weight_by_age[age_with_lowest_weight]

print(f"The difference in weight between the age group with the highest average weight ({age_with_highest_weight} years) and the age group with the lowest average weight ({age_with_lowest_weight} years) is {difference_in_weight:.2f} kg.")
