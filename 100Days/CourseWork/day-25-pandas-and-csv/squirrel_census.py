import pandas as pd

abs_squirrel_path = '/Users/arougellis/Desktop/PythonCourse/100Days/CourseWork/day-25-pandas-and-csv/data/squirrel_data.csv'
rel_squirrel_path = 'data/squirrel_data.csv'

squirrel_df = pd.read_csv(abs_squirrel_path)

# TASK 1:
#       - create a csv of number of squirrels that have a specific fur color
#
fur_color_series = squirrel_df['Primary Fur Color']

# Want to see how many unique color there are first...
fur_color_series.unique()
#           Output : [nan, 'Gray', 'Cinnamon', 'Black']

grey_count = len(squirrel_df[fur_color_series == 'Gray'])
cinnamon_count = len(squirrel_df[fur_color_series == 'Cinnamon'])
black_count = len(squirrel_df[fur_color_series == 'Black'])

fur_color_dict = {
    "furColor": ['Gray', 'Cinnamon', 'Black'],
    "count": [grey_count, cinnamon_count, black_count]
}

fur_color_df = pd.DataFrame(data=fur_color_dict)

abs_squirrel_color_dest = '/Users/arougellis/Desktop/PythonCourse/100Days/CourseWork/day-25-pandas-and-csv/data/squirrel_color_count.csv'
rel_squirrel_color_dest = 'data/squirrel_color_count.csv'
fur_color_df.to_csv(abs_squirrel_color_dest)
