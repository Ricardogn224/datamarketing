#Import libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
pd.set_option('display.max_columns', None)

import plotly.express as px #for visualization
import matplotlib.pyplot as plt #for visualization 

#Read the dataset
data_df = pd.read_excel("./Telecom-Data-1.xlsx")
data_df = pd.read_excel("./train.xlsx")
data_df.dropna(inplace=True)

#Get overview of the data
def dataoveriew(df, message):
    print(f'{message}:n')
    print('Number of rows: ', df.shape[0])
    print("nNumber of features:", df.shape[1])
    print("nData Features:")
    print(df.columns.tolist())
    print("nMissing values:", df.isnull().sum().values.sum())
    print("nUnique values:")
    print(df.nunique())

dataoveriew(data_df, 'Overview of the dataset')

# plot % of Desabonnement 
target_instance = data_df["Desabonnement"].value_counts().to_frame()
target_instance = target_instance.reset_index()
target_instance = target_instance.rename(columns={'index': 'Category'})
fig = px.pie(target_instance, values='Desabonnement', names='Category', color_discrete_sequence=["green", "red"],
             title='Distribution of Desabonnement')
#fig.show()

# let explore catégorical features

#Defining bar chart function
def bar(feature, df=data_df ):
    #Groupby the categorical feature
    temp_df = df.groupby([feature, 'Desabonnement']).size().reset_index()
    temp_df = temp_df.rename(columns={0:'Count'})
    #Calculate the value counts of each distribution and it's corresponding Percentages
    value_counts_df = df[feature].value_counts().to_frame().reset_index()
    categories = [cat[1][0] for cat in value_counts_df.iterrows()]
    #Calculate the value counts of each distribution and it's corresponding Percentages
    num_list = [num[1][1] for num in value_counts_df.iterrows()]
    div_list = [element / sum(num_list) for element in num_list]
    percentage = [round(element * 100,1) for element in div_list]
    #Defining string formatting for graph annotation
    #Numeric section
    def num_format(list_instance):
        formatted_str = ''
        for index,num in enumerate(list_instance):
            if index < len(list_instance)-2:
                formatted_str=formatted_str+f'{num}%, ' #append to empty string(formatted_str)
            elif index == len(list_instance)-2:
                formatted_str=formatted_str+f'{num}% & '
            else:
                formatted_str=formatted_str+f'{num}%'
        return formatted_str
    #Categorical section
    def str_format(list_instance):
        formatted_str = ''
        for index, cat in enumerate(list_instance):
            if index < len(list_instance)-2:
                formatted_str=formatted_str+f'{cat}, '
            elif index == len(list_instance)-2:
                formatted_str=formatted_str+f'{cat} & '
            else:
                formatted_str=formatted_str+f'{cat}'
        return formatted_str
    #Running the formatting functions
    num_str = num_format(percentage)
    cat_str = str_format(categories)

    #Setting graph framework
    fig = px.bar(temp_df, x=feature, y='Count', color='Desabonnement', title=f'Desabonnement rate by {feature}', barmode="group", color_discrete_sequence=["green", "red"])
    fig.add_annotation(
                text=f'Value count of distribution of {cat_str} are<br>{num_str} percentage respectively.',
                align='left',
                showarrow=False,
                xref='paper',
                yref='paper',
                x=1.4,
                y=1.3,
                bordercolor='black',
                borderwidth=1)
    fig.update_layout(
        # margin space for the annotations on the right
        margin=dict(r=400),
    )

    return fig.show()

#Genre feature plot

#Genre feature plot 
data_df.loc[data_df.Genre==0,'Genre'] = "No"   #convert 0 to No in all data instances
data_df.loc[data_df.Genre==1,'Genre'] = "Yes"  #convert 1 to Yes in all data instances
#bar('Genre')


#Partner feature plot
#bar('Partner')
#Dependents feature plot
#bar('Dependents')



#Create an empty dataframe
bin_df = pd.DataFrame()

#Update the binning dataframe
bin_df['Anciennete'] =  pd.qcut(data_df['Anciennete'], q=3, labels= ['low', 'medium', 'high'])
bin_df['charges mensuelles'] =  pd.qcut(data_df['charges mensuelles'], q=3, labels= ['low', 'medium', 'high'])
bin_df['Charges totales'] =  pd.qcut(data_df['Charges totales'], q=3, labels= ['low', 'medium', 'high'])
bin_df['Desabonnement'] = data_df['Desabonnement']

#Plot the bar chart of the binned variables
#bar('Anciennete', bin_df)
#bar('charges mensuelles', bin_df)
#bar('Charges totales', bin_df)


# The customerID column isnt useful as the feature is used for identification of customers. 
data_df.drop(["ID"],axis=1,inplace = True)

# Encode categorical features

#Defining the map function
def binary_map(feature):
    return feature.map({'Yes':1, 'No':0})

## Encoding target feature
data_df['Desabonnement'] = data_df[['Desabonnement']].apply(binary_map)

# Encoding Genre category
data_df['Genre'] = data_df['Genre'].map({'Male':1, 'Female':0})

#Encoding other binary category
binary_list = ['Senior', 'Enfants', 'Multi-lignes', 'Service Internet', 'Autres Services','Partenaire','Contrat']
data_df[binary_list] = data_df[binary_list].apply(binary_map)

#Encoding the other categoric features with more than two categories
data_df = pd.get_dummies(data_df, drop_first=True)

# Checking the correlation between features
corr = data_df.corr()

fig = px.imshow(corr,width=1000, height=1000)
#fig.show()


#feature scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
data_df['Anciennete'] = sc.fit_transform(data_df[['Anciennete']])
data_df['charges mensuelles'] = sc.fit_transform(data_df[['charges mensuelles']])
data_df['Charges totales'] = sc.fit_transform(data_df[['Charges totales']])


