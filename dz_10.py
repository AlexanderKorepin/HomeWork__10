import pandas as pd
import seaborn as sns
import google.colab as files
# Задача 1. Найдите, какая область центрального федерального округа имела наибольшую численность студентов вечерней формы обучения в 2015 году.
from numpy import maximum
df_2019 = pd.read_csv('data20152019.csv', sep = ';',encoding='cp1251')
df_2019
df_2019 = df_2019.iloc[0:20,7:8] 
max_value = df_2019['Численность студентов очно-заочная (вечерняя) форма, человек, 2017'].max()
df_2019[df_2019['Численность студентов очно-заочная (вечерняя) форма, человек, 2017']==max_value]
#====================================================================================================
# Задача 2. Постройте диаграмму с данными о численности студентов дневной формы обучения южного федерального округа за 2017 год.
df_2019 = df_2019.iloc[33:41,:] 
df_2019
df_2019[['Субъект РФ','Численность студентов, очная форма, человек, 2017']]
plot = sns.barplot(df_2019, x = 'Субъект РФ', y = 'Численность студентов, очная форма, человек, 2017')
plot.set_xticklabels(labels = df_2019['Субъект РФ'],rotation = 90)
#diagram_2.png
#=====================================================================================================
#Задача 3. Постройте диаграмму количества студентов заочной формы обучения за 2019 год по всем регионам, в которых общее количество студентов не превышает 10000 за данный год.
df_2019 = pd.read_csv('data20152019.csv', sep = ';',encoding='cp1251')
df_2019
df_2019 = df_2019[df_2019 ['Численность студентов, очная форма, человек, 2019']< 10000]
df_2019[['Субъект РФ','Численность студентов, очная форма, человек, 2019']]
plot = sns.barplot(df_2019, x = 'Субъект РФ', y = 'Численность студентов, очная форма, человек, 2019')
plot.set_xticklabels(labels = df_2019['Субъект РФ'],rotation = 90)
