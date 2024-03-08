import pandas as pd
import numpy as np
from scipy import stats  # Importing stats module from scipy

# Load the dataset
data = pd.read_csv('cardio_base.csv')

# Split the data into smokers and non-smokers
smokers = data[data['smoke'] == 1]
non_smokers = data[data['smoke'] == 0]

# Hypothesis test for the first assertion: Smokers weigh less than non-smokers
_, p_value1 = stats.ttest_ind(smokers['weight'], non_smokers['weight'], equal_var=False)
if p_value1 < 0.05:
    print("With 95% confidence, it's true that smokers weigh less than non-smokers.")
else:
    print("With 95% confidence, it's not true that smokers weigh less than non-smokers.")

# Hypothesis test for the second assertion: Smokers have higher blood pressure than non-smokers
_, p_value2 = stats.ttest_ind(smokers['ap_hi'], non_smokers['ap_hi'], equal_var=False)
if p_value2 < 0.05:
    print("With 95% confidence, it's true that smokers have higher blood pressure than non-smokers.")
else:
    print("With 95% confidence, it's not true that smokers have higher blood pressure than non-smokers.")

# Hypothesis test for the third assertion: Smokers have higher cholesterol levels than non-smokers
_, p_value3 = stats.ttest_ind(smokers['cholesterol'], non_smokers['cholesterol'], equal_var=False)
if p_value3 < 0.05:
    print("With 95% confidence, it's true that smokers have higher cholesterol levels than non-smokers.")
else:
    print("With 95% confidence, it's not true that smokers have higher cholesterol levels than non-smokers.")

# Split the data into men and women
men = data[data['gender'] == 1]
women = data[data['gender'] == 2]

# Hypothesis test for the fourth assertion: Men have higher blood pressure than women
_, p_value4 = stats.ttest_ind(men['ap_hi'], women['ap_hi'], equal_var=False)
if p_value4 < 0.05:
    print("With 95% confidence, it's true that men have higher blood pressure than women.")
else:
    print("With 95% confidence, it's not true that men have higher blood pressure than women.")
