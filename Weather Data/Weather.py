import csv

# open and read csv
weather_file = open('WeatherDataWindows.csv', 'r')
weather_column = csv.DictReader(weather_file)

count = 0
# created empty lists to store csv data
dates = []
temp_high = []
temp_low = []
avg_precip_s = []
dew_avg = []
press_high = []
press_avg = []
press_low = []
temp_avg = []
humid_low = []
june29 = []

# add data to lists
for col in weather_column:
    dates.append(col['Date'])
    temp_high.append(col['Temp High'])
    temp_avg.append(col['Temp Avg'])
    temp_low.append(col['Temp Low'])
    dew_avg.append(col['Dew Point Avg'])
    press_high.append(col['Pressure High'])
    press_avg.append(col['Pressure Avg'])
    press_low.append(col['Pressure Low'])
    avg_precip_s.append(col['Precipitation (in.)'])
    humid_low.append(col['Humidity Low'])

total_temp = temp_high + temp_avg + temp_low

# The lines below change the lists of strings to lists of ints or floats
# suffix f means float, i for int

avg_precip_f = [float(x) for x in avg_precip_s]
temp_high_i = [int(x) for x in temp_high]
temp_low_i = [int(x) for x in temp_low]
dew_avg_i = [int(x) for x in dew_avg]
total_temp_i = [int(x) for x in total_temp]
humid_low_i = [int(x) for x in humid_low]

daily_precipitation = sum(avg_precip_f) / len(avg_precip_f)

# calculating how many days
for x in humid_low_i:
    if x < 25:
        count += 1
percent_occurred = ((count / len(humid_low_i)) * 100)

# a
print(f'Max Temp: {max(temp_high_i)}')
print(f'Min Temp: {min(temp_low_i)}')

# b
print(f'Average daily precipitation: {daily_precipitation:.2f} in.')

# c
print(f'The average temperature is {(sum(total_temp_i) / len(total_temp_i)):.0f}°F.')
print(f'The frequency of when the humidity was below 25 is {percent_occurred:.2f}%.')

print(f'The temperature is', end=' ')
for y, dates in enumerate(dates):
    if '6/29/20' in dates:
        print(temp_high_i[y], end=' on ')
        june29.append(temp_high_i[y])
        print(dates, end=', ')
print()

print(f'The average temperature on June 29th is {(sum(june29) / len(june29)):.2f}°F.')


# close csv
weather_file.close()