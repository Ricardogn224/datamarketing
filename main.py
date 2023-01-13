# Import required libraries
import numpy as np
import pandas as pd
  
# Import the dataset
dataset = pd.read_excel('Telecom-Data-1.xlsx')
  
# Glance at the first five records
dataset.head()
#print(dataset.head())
  
# Print all the features of the data
dataset.columns

# Churners vs Non-Churners
#print(dataset['Desabonnement'].value_counts())

# Count the number of churners and non-churners by A
# nciennete
print(dataset.groupby('Anciennete')['Desabonnement','Enfants'].value_counts())


# Import matplotlib and seaborn
import matplotlib.pyplot as plt
import seaborn as sns
  
# Visualize the distribution of 'Total day minutes'
plt.hist(dataset['charges mensuelles'], bins = 100)
  
# Display the plot
#plt.show()


# Create the box plot
sns.boxplot(x = 'Desabonnement',
            y = 'Anciennete',
            data = dataset,
            sym = "",                  
            hue = "Facturation electronique") 
# Display the plot
plt.show()