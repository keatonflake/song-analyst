import plotly.express as px

def analyze_energy_vs_popularity(df):
    print("\nAverage Energy and Popularity per artist:")
    avg_df = df.groupby('Artist')[['Energy', 'Popularity']].mean()
    print(avg_df)

    # Filter to exclude extreme outliers if necessary
    energy_threshold = 1.0  # Adjust as needed for your dataset
    df_filtered = df[df['Energy'] <= energy_threshold]

    # Create an interactive scatter plot
    fig = px.scatter(df_filtered,
                     x='Energy',
                     y='Popularity',
                     hover_data=['Track', 'Artist'],
                     title='Popularity vs. Energy (Outliers Removed)',
                     labels={'Energy': 'Energy', 'Popularity': 'Popularity'},
                     trendline='ols')

    # Save the plot as an HTML file
    fig.write_html('popularity_vs_energy.html')  # Save as HTML file for interactivity

    # Save as PNG file
    fig.write_image('popularity_vs_energy.png')  # Save as PNG file