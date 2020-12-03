# source: https://realpython.com/analyzing-obesity-in-england-with-python/
import pandas as pd
import matplotlib.pyplot as plt

data = pd.ExcelFile('obes-phys-acti-diet-eng-2017-tab.xlsx')

# clean other data - skip one column
data_age = data.parse(u'Table 2', index_col=0, skiprows=7, skipfooter=14, usecols=[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

data_age.rename(columns={'Year4,5': 'Year', 'All persons6': 'All persons'}, inplace=True)

data_age.dropna(inplace=True)

print(data_age)

data_age_minus_total = data_age.drop('All persons', axis=1)

data_age_minus_total.plot()

plt.show()