import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Charger les données à partir d'un fichier CSV
data = pd.read_excel("Telecom-Data-1.xlsx")

# Sélectionner les colonnes à utiliser pour la prédiction
X = data[['Anciennete','Autres Services','Mode de paiement','charges mensuelles','Partenaire','Charges totales']]

# Sélectionner la colonne cible (désabonnement ou non)
y = data['Desabonnement']

# Diviser les données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Créer et entraîner un classificateur de forêt aléatoire
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Effectuer des prédictions sur l'ensemble de test
y_pred = clf.predict(X_test)

# Calculer la précision de la prédiction
accuracy = accuracy_score(y_test, y_pred)

print("La précision de la prédiction est de {:.2f}%".format(accuracy*100))