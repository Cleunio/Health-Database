import pandas as pd

# Carregar os datasets
health_data = pd.read_csv('cardio_base.csv', sep=',')  # Definir o separador como ',' para o novo formato do arquivo
cardio_alco_data = pd.read_csv('cardio_alco.csv', sep=';')  # Definir o separador como ';' para o novo formato do arquivo

# Mesclar os datasets com base no ID
merged_data = pd.merge(health_data, cardio_alco_data, on='id', how='inner')

# Filtrar pessoas com mais de 50 anos
over_50 = merged_data[merged_data['age'] > 50]

# Calcular a porcentagem de pessoas com mais de 50 anos que consomem álcool
alcohol_consumers_percentage = (over_50['alco'] == 1).mean() * 100

print("A porcentagem da população com mais de 50 anos que consome álcool é: {:.2f}%".format(alcohol_consumers_percentage))
