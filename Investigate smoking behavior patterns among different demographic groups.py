import pandas as pd

# Assuming you have the dataset in a CSV file named 'health_data.csv'
data = pd.read_csv('cardio_base.csv')

# Calculate the proportion of male smokers
male_smokers_proportion = data[data['gender'] == 'male']['smoke'].mean()

# Calculate the proportion of female smokers
female_smokers_proportion = data[data['gender'] == 'female']['smoke'].mean()

# Compare the proportions to determine the answer
if male_smokers_proportion == female_smokers_proportion:
    print("a) Similar portion of men and women are smokers")
elif male_smokers_proportion > female_smokers_proportion:
    print("b) Yes, men are {:.0f} times more likely to be smokers".format(male_smokers_proportion / female_smokers_proportion))
else:
    print("c) No, women are {:.0f} times more likely to be smokers".format(female_smokers_proportion / male_smokers_proportion))
