# source: https://realpython.com/pandas-read-write-files/

import pandas as pd
from sqlalchemy import create_engine

data = {
    'CHN': {'COUNTRY': 'China', 'POP': 1_398.72, 'AREA': 9_596.96,
            'GDP': 12_234.78, 'CONT': 'Asia'},
    'IND': {'COUNTRY': 'India', 'POP': 1_351.16, 'AREA': 3_287.26,
            'GDP': 2_575.67, 'CONT': 'Asia', 'IND_DAY': '1947-08-15'},
    'USA': {'COUNTRY': 'US', 'POP': 329.74, 'AREA': 9_833.52,
            'GDP': 19_485.39, 'CONT': 'N.America',
            'IND_DAY': '1776-07-04'},
    'IDN': {'COUNTRY': 'Indonesia', 'POP': 268.07, 'AREA': 1_910.93,
            'GDP': 1_015.54, 'CONT': 'Asia', 'IND_DAY': '1945-08-17'},
    'BRA': {'COUNTRY': 'Brazil', 'POP': 210.32, 'AREA': 8_515.77,
            'GDP': 2_055.51, 'CONT': 'S.America', 'IND_DAY': '1822-09-07'},
    'PAK': {'COUNTRY': 'Pakistan', 'POP': 205.71, 'AREA': 881.91,
            'GDP': 302.14, 'CONT': 'Asia', 'IND_DAY': '1947-08-14'},
    'NGA': {'COUNTRY': 'Nigeria', 'POP': 200.96, 'AREA': 923.77,
            'GDP': 375.77, 'CONT': 'Africa', 'IND_DAY': '1960-10-01'},
    'BGD': {'COUNTRY': 'Bangladesh', 'POP': 167.09, 'AREA': 147.57,
            'GDP': 245.63, 'CONT': 'Asia', 'IND_DAY': '1971-03-26'},
    'RUS': {'COUNTRY': 'Russia', 'POP': 146.79, 'AREA': 17_098.25,
            'GDP': 1_530.75, 'IND_DAY': '1992-06-12'},
    'MEX': {'COUNTRY': 'Mexico', 'POP': 126.58, 'AREA': 1_964.38,
            'GDP': 1_158.23, 'CONT': 'N.America', 'IND_DAY': '1810-09-16'},
    'JPN': {'COUNTRY': 'Japan', 'POP': 126.22, 'AREA': 377.97,
            'GDP': 4_872.42, 'CONT': 'Asia'},
    'DEU': {'COUNTRY': 'Germany', 'POP': 83.02, 'AREA': 357.11,
            'GDP': 3_693.20, 'CONT': 'Europe'},
    'FRA': {'COUNTRY': 'France', 'POP': 67.02, 'AREA': 640.68,
            'GDP': 2_582.49, 'CONT': 'Europe', 'IND_DAY': '1789-07-14'},
    'GBR': {'COUNTRY': 'UK', 'POP': 66.44, 'AREA': 242.50,
            'GDP': 2_631.23, 'CONT': 'Europe'},
    'ITA': {'COUNTRY': 'Italy', 'POP': 60.36, 'AREA': 301.34,
            'GDP': 1_943.84, 'CONT': 'Europe'},
    'ARG': {'COUNTRY': 'Argentina', 'POP': 44.94, 'AREA': 2_780.40,
            'GDP': 637.49, 'CONT': 'S.America', 'IND_DAY': '1816-07-09'},
    'DZA': {'COUNTRY': 'Algeria', 'POP': 43.38, 'AREA': 2_381.74,
            'GDP': 167.56, 'CONT': 'Africa', 'IND_DAY': '1962-07-05'},
    'CAN': {'COUNTRY': 'Canada', 'POP': 37.59, 'AREA': 9_984.67,
            'GDP': 1_647.12, 'CONT': 'N.America', 'IND_DAY': '1867-07-01'},
    'AUS': {'COUNTRY': 'Australia', 'POP': 25.47, 'AREA': 7_692.02,
            'GDP': 1_408.68, 'CONT': 'Oceania'},
    'KAZ': {'COUNTRY': 'Kazakhstan', 'POP': 18.53, 'AREA': 2_724.90,
            'GDP': 159.41, 'CONT': 'Asia', 'IND_DAY': '1991-12-16'}
}

columns = ('COUNTRY', 'POP', 'AREA', 'GDP', 'CONT', 'IND_DAY')

df = pd.DataFrame(data=data).T

print('Get a USA country')
print(df.loc['USA'])

print(df)

df.to_csv('countries.csv')

'''
Missing values for Pandas: 'nan', '-nan', 'NA', 'N/A', 'NAN', 'null', ''
'''
# replace empty values to string (missing)
df.to_csv('new-countries.csv', na_rep='(missing)')

pd.read_csv('countries.csv')

print(df.dtypes)

print(df['IND_DAY'])

df = pd.read_csv('countries.csv', index_col=0, parse_dates=['IND_DAY'])
df.to_csv('formatted-date.csv', date_format='%B %d %Y')

'''
optional parameters to save csv:
- sep
- decimal
- encoding
- header
'''

# example of usage header
s = df.to_csv(sep=';', header=False)

print(s)


# example of saving file as json
df.to_json('data-json.json', orient='index')


# SQL
engine = create_engine('sqlite:///data.db', echo=False)

dtypes = {'POP': 'float64', 'AREA': 'float64', 'GDP': 'float64', 'IND_DAY': 'datetime64'}

df = pd.DataFrame(data=data).T.astype(dtype=dtypes)

df.to_sql('data.sql', con=engine, index_label='ID', if_exists='replace')

df = pd.read_sql('data.sql', con=engine, index_col='ID')

print('Data read from sql', df, sep="\n")

# Compress and decompress files
'''
.gz, bz2, zip, xz
'''
df = pd.DataFrame(data=data).T
df.to_csv('data.csv.zip')

# Read only columns that you are interested in
df = pd.read_csv('data.csv.zip', usecols=['COUNTRY', 'AREA'])
print(df)
'''
Another features:
- skiprows
- skipfooter
- nrows
'''

# Big datasets:
'''
Compress and decompress
Read only data that you needed
When you read files by read_csv, read_json, read_sql you can specify chunks
Use less precise data types
'''
data_chunk = pd.read_csv('data.csv.zip', index_col=0, chunksize=8)
print(type(data_chunk))

for chunk in data_chunk:
    print(chunk)