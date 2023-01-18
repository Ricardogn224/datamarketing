import pandas as pd

# Ouvrir le fichier excel
df = pd.read_excel("train.xlsx")

# Parcours des lignes de la colonne desabonnement
for i, row in df.iterrows():
    if row['Contrat'] == "Mensuel":
        df.at[i, 'Genre'] = 1
    elif row['Contrat'] == "Annuel":
        df.at[i, 'Genre'] = 0

# Enregistrement des modifications dans le fichier excel
df.to_excel("train.xlsx", index=False)
