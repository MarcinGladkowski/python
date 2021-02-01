import csv
from datetime import datetime

import matplotlib.pyplot as plt

'''
Data comes from: https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:PLM00012375/detail

Data types:
TMAX - Maximum temperature
TAVG - Average Temperature.
TMIN - Minimum temperature
PRCP - Precipitation
SNWD - Snow depth
'''

filename = 'Warsaw_data_2021.csv'

def from_fahrenheit_to_celsius(temp):
    return round((temp - 32) * 5/9)


print(round(from_fahrenheit_to_celsius(69)))

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    print(header_row)

    dates, average_temp, min_temp, max_temp = [], [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            max_temp_day = from_fahrenheit_to_celsius(int(row[6]))
            min_temp_day = from_fahrenheit_to_celsius(int(row[7]))
        except:
            print(f'Error when parsing data for {current_date}')
        else:
            dates.append(current_date)
            max_temp.append(max_temp_day)
            min_temp.append(min_temp_day)

    print(len(min_temp))
    print(len(max_temp))

    plt.style.use('seaborn')
    fix, ax = plt.subplots()
    ax.plot(dates, max_temp, c='red')
    ax.plot(dates, min_temp, c='blue')
    plt.ylabel('Temperatures')

    plt.show()
