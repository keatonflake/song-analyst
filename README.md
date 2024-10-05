# Spotify Top 100 Songs Dataset Analysis

## Overview

In this dataset, we observe statistics about the top 100 songs as recorded on Spotify. For more details, please refer to the original dataset on Kaggle: [Top 100 Songs Dataset](https://www.kaggle.com/datasets/thebumpkin/600-billboard-hot-100-tracks-with-spotify-data).

### [Software Demo Video](https://youtu.be/X0zyIVkeNwM)

### [Live Project](https://keatonflake.github.io/song-analyst/)

# Development Environment

Using Python Pandas, matplotlib, seaborn, numpy, plotly, and scikit-learn scatter plots and a JSON file of ranked songs and artists were created.

Using JavaScript A front-End was created to show the ranked artists on a bar chart and display the created satter plots.

### Question 1: Least to Most Popular Artist

Based on this dataset what is the ranked list of artists by popularity?
Result: At the time of this dataset "The Weeknd" was the #1 most popular artist

### Question 2: Energy vs. Popularity

If a song has high energy, does it have a higher probability of being more popular?

To explore this question, a scatter plot of energy vs. popularity was created to illustrate the relationship between these two variables.

Result: Suprisingly, based on this dataset, there is a slight correlation between lower energy and more popularity. Though it is in the margin of error, it is still noticable.

### Question 3: Duration vs. Popularity

If a song has a shorter duration, does it have a higher probability of being more popular?

Similarly, a scatter plot of duration vs. popularity was created to visualize this relationship.

Result: longer songs tend to be more popular.

# Runing the Python Code

Install Dependencies:
pandas | matplotlib | seaborn | numpy | plotly | scikit-learn

Run the main.py file

# Useful Websites

[Pandas 10 Minute Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html#min)
[Pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
[Pandas Example with Titanic Data ](https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77)

# Future Work

I want to improve this project so it consistently pulls from the latest top 100. I think it would be fun to
see what new questions can be answered based on theh other records in this dataset that I did not utilize.
