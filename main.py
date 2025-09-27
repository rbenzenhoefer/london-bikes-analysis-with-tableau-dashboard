''' importing libraries'''
import pandas as pd
import zipfile

'''Loading the data and getting an overview'''
bikes = pd.read_csv("london_merged.csv")
#print(bikes.info())
#print(bikes.shape)
#print(bikes)
#print(bikes.weather_code.value_counts())
#print(bikes.season.value_counts())

'''renaming columns + humidty values -> percentages'''
new_cols_dict ={
    'timestamp':'time',
    'cnt':'count',
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}
bikes.rename(new_cols_dict, axis=1, inplace=True)
bikes.humidity_percent = bikes.humidity_percent / 100

'''Creating weather and season dictonaries to map integers to written values + changing data types'''
season_dict ={
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
}
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered Clouds',
    '3.0':'Broken Clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall'
}

bikes.season = bikes.season.astype('str')
bikes.season = bikes.season.map(season_dict)
bikes.weather = bikes.weather.astype('str')
bikes.weather = bikes.weather.map(weather_dict)
print(bikes.head())

bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')