import pandas as pd

abs_weather_path = '/Users/arougellis/Desktop/PythonCourse/100Days/CourseWork/day-25-pandas-and-csv/data/weather_data.csv'
rel_weather_path = 'data/weather_data.csv'

# NOTE:
#   - the csv gets converted to type = dataframe
weather_df = pd.read_csv(abs_weather_path)
#   - but a SERIES is equivalent to a column of a df, like below...
temp_series = weather_df.temp
# We can do many things with thee series....
#   - find average temp of a list
average_temp = temp_series.mean()
#   - find max temp
max_temp = temp_series.max()

# Get a hold of a row
monday_row = weather_df[weather_df['day'] == 'Monday']

# Which row has the highest temp
hottest_day = weather_df[weather_df.temp == weather_df.temp.max()]

# Get Monday's temperature in Fahrenheit
monday_temp = weather_df[weather_df['day'] == 'Monday'].temp * (9 / 5) + 32

# ----

# From the dictionary below...
data_dict = {
    "students": ["Nate", "Joel", "Ellie"],
    "score": [76, 56, 65]
}
# ...create a DataFrame
data_df = pd.DataFrame(data=data_dict)

# Create a csv from a dataframe...
# data_df.to_csv(<path_to_destination>)


