import pandas as pd
import json
from energy_v_popularity import analyze_energy_vs_popularity
from duration_v_popularity import analyze_duration_vs_popularity
# In this data set, we observe statistics about the top 100 songs as recorded in spodify
# For more detials: https://www.kaggle.com/datasets/thebumpkin/600-billboard-hot-100-tracks-with-spotify-data
# A general overview of the dataset is given, then we will analyze the data in different ways:

# Question 1) "If a song has a high energy, does it have a higher probability of being more popular?"
# Using this dataset, scatter plot of energy vs. popularity is created showing this relationship
# Conclusion: high energy songs have a higher probability of being more popular.

# Question 2) "If a song has a shorter duration, does it have a higher probability of being more popular?"
# Using this dataset, scatter plot of duration vs. popularity is created showing this relationship

# Load the dataset
df = pd.read_csv('Hot100.csv')

# General overview of the dataset
print("Dataset Info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nStatistics for numeric features:")
print(df.describe())
print("\nAverage popularity per artist:")
avg_popularity = df.groupby('Artist')['Popularity'].mean()
print(avg_popularity)

# Save the average popularity to a JSON file
avg_popularity_dict = avg_popularity.to_dict()
with open('average_popularity.json', 'w') as json_file:
    json.dump(avg_popularity_dict, json_file)

# Energy vs. Popularity Analysis
analyze_energy_vs_popularity(df)

# Duration vs. Popularity Analysis
analyze_duration_vs_popularity(df)