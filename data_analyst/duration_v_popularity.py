import plotly.express as px
import pandas as pd

def analyze_duration_vs_popularity(df):
    print("\nAverage Duration and Popularity per artist:")
    avg_df = df.groupby('Artist')[['Duration', 'Popularity']].mean()
    print(avg_df)

    # Filter to exclude extreme outliers
    duration_threshold = 400000  # in milliseconds
    df_filtered = df[df['Duration'] <= duration_threshold]

    fig = px.scatter(df_filtered,
                     x='Duration',
                     y='Popularity',
                     hover_data=['Track', 'Artist'],
                     title='Popularity vs. Duration (Outliers Removed)',
                     labels={'Duration': 'Duration (ms)', 'Popularity': 'Popularity'},
                     trendline='ols')

    # Save the plot as an HTML file
    fig.write_html('popularity_vs_duration.html')  # Save as HTML file

    fig.write_image('popularity_vs_duration.png')  # Save as PNG file