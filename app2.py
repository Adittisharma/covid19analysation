import pandas
import numpy
import seaborn as sns
import matplotlib.pyplot as plt


data = pandas.read_csv(r"C:\Users\DeLL\Downloads\india-covid-update.csv")
#print(data.columns)
#print(data.describe())
#print(sns.relplot(x="Total Confirmed cases",y="Cured/Discharged/Migrated",kind='line',data=data))
#print(sns.catplot(x="Total Confirmed cases",y="Cured/Discharged/Migrated",data=data))
print(sns.relplot(x="Total Confirmed cases",y="Deaths",kind='line',data=data))
#data.head()
plt.show()

#IMPACT
#1. People are recovering with respect to total cases.
#2.  Death rate was relatively constant but then rise up when "Total cases" crosses 10,000 .
