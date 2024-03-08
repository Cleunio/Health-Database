import pandas as pd

# Assuming you have the dataset in a CSV file named 'health_data.csv'
data = pd.read_csv('cardio_base.csv')

# Calculate the average cholesterol levels for people over 50 years old
cholesterol_over_50_mean = data[data['age'] > 50]['cholesterol'].mean()

# Calculate the average cholesterol levels for people under 50 years old
cholesterol_under_50_mean = data[data['age'] <= 50]['cholesterol'].mean()

# Compare the means to determine if there's a significant difference
if cholesterol_over_50_mean == cholesterol_under_50_mean:
    print("a) No, it's about the same")
elif cholesterol_over_50_mean > cholesterol_under_50_mean:
    print("b) Yes, their cholesterol level is {:.0%} higher on average".format((cholesterol_over_50_mean / cholesterol_under_50_mean) - 1))
else:
    print("d) No, people over 50 have {:.0%} lower cholesterol level".format(1 - (cholesterol_over_50_mean / cholesterol_under_50_mean)))
