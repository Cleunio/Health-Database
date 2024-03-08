import pandas as pd

# Assuming you have the dataset in a CSV file named 'health_data.csv'
data = pd.read_csv('cardio_base.csv')

# Calculate the Spearman correlation matrix
spearman_corr = data.corr(method='spearman')

# Find the feature pairs with the highest Spearman correlations
highest_corr_pairs = spearman_corr.abs().unstack().sort_values(ascending=False)

# Ignore the main diagonal (correlations of a feature with itself)
highest_corr_pairs = highest_corr_pairs[highest_corr_pairs.index.get_level_values(0) != highest_corr_pairs.index.get_level_values(1)]

# Print the top two pairs with the highest Spearman correlation
print("The two pairs with the highest Spearman correlation are:")
print(highest_corr_pairs.head(2))
