import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('population_by_country_2020.csv')
country_data = df["Country"]
population_data = df["Population"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b","#eff542","#f5425d","#42eff5","#42f545"]
 
plt.pie(population_data, labels=country_data, colors=colors,
autopct='%1.1f%%', startangle=140)
plt.title("Population By Country")
plt.show()