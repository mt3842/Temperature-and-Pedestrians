import pandas as pd 
import numpy as np 
from datetime import datetime

df_weather_2023 = pd.read_csv('IDCJAC0010_086338_2023_Data.csv')
df_weather_2023['date'] = pd.to_datetime(df_weather_2023[['Year', 'Month', 'Day']])
df_weather_2023.drop(['Product code', 'Bureau of Meteorology station number', 'Days of accumulation of maximum temperature', 'Quality', 'Year', 'Month', 'Day'], axis=1, inplace=True)

df_weather_2024 = pd.read_csv('IDCJAC0010_086338_2024_Data.csv')
df_weather_2024['date'] = pd.to_datetime(df_weather_2024[['Year', 'Month', 'Day']])
df_weather_2024.drop(['Product code', 'Bureau of Meteorology station number', 'Days of accumulation of maximum temperature', 'Quality', 'Year', 'Month', 'Day'], axis=1, inplace=True)

df_weather = pd.concat([df_weather_2023, df_weather_2024])

df_pedestrian_2023 = pd.read_csv('pedestrian-counting-system-monthly-counts-per-hour-2023.csv').sort_values(by='Sensing_Date')
df_pedestrian_2023['date'] = pd.to_datetime(df_pedestrian_2023['Sensing_Date'])
df_pedestrian_2023.drop(['ID', 'Location_ID', 'HourDay', 'Direction_1', 'Direction_2','Sensor_Name', 'Location', 'Sensing_Date'], axis=1, inplace=True)
df_pedestrian_2023 = df_pedestrian_2023.groupby('date').sum()

df_pedestrian_2024 = pd.read_csv('pedestrian-counting-system-monthly-counts-per-hour-2024.csv').sort_values(by='Sensing_Date')
df_pedestrian_2024['date'] = pd.to_datetime(df_pedestrian_2024['Sensing_Date'])
df_pedestrian_2024.drop(['ID', 'Location_ID', 'HourDay', 'Direction_1', 'Direction_2','Sensor_Name', 'Location', 'Sensing_Date'], axis=1, inplace=True)
df_pedestrian_2024 = df_pedestrian_2024.groupby('date').sum()

df_pedestrian = pd.concat([df_pedestrian_2023, df_pedestrian_2024]).sort_values('date')

df = pd.merge(df_weather, df_pedestrian, how='inner', on='date')

df.to_csv('melbourne_pedestrian_weather.csv', index=False)

#print(df.head(10))
#print(df.tail(10))