# An aggie does not lie, cheat, or steal or tolerate those that do.
# I have not received or given any unauthorized assistance.
# Nick Foley
# ENGR 102 538
# Assignment 11b
# 2 NOV 2022

import csv

# open and read csv
weather_file = open('WeatherDataWindows.csv', 'r')
weather_column = csv.DictReader(weather_file)

# created empty lists to store csv data
dates = []
temp_high = []
temp_low = []
avg_precip_s = []
dew_high = []

# add data to lists
for col in weather_column:




    temp_high.append(col['Temp High'])
    temp_low.append(col['Temp Low'])
    avg_precip_s.append(col['Precipitation (in.)'])
    dates.append(col['Date'])



avg_precip_f = [float(x) for x in avg_precip_s]
daily_precipitation = sum(avg_precip_f) / len(avg_precip_f)

print(f'Max Temp: {max(temp_high)}')
print(f'Min Temp: {min(temp_low)}')
print(f'Average daily precipitation: {daily_precipitation:.2f} in.')

# close csv
weather_file.close()
# # open and read csv
# weather_file = open('WeatherDataWindows.csv', 'r')
# weather_row = csv.reader(weather_file)
#
# count = 0
#
# for row in weather_row:
#     print(row)
#
#     if count > 5:
#         break
#     count += 1
#
# weather_file.close()
#
#








