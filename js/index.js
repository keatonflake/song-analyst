document.addEventListener("DOMContentLoaded", function () {
  fetch("./data_analyst/average_popularity.json")
    .then((response) => response.json())
    .then((data) => {
      // Convert the object into an array of [artist, popularity] pairs
      const artistPopularityArray = Object.entries(data);

      // Sort the array by popularity (second element in each pair)
      artistPopularityArray.sort((a, b) => a[1] - b[1]);

      // Separate the sorted arrays back into labels and popularity
      const labels = artistPopularityArray.map((item) => item[0]);
      const popularity = artistPopularityArray.map((item) => item[1]);

      const ctx = document.getElementById("popularityChart").getContext("2d");
      const popularityChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: labels,
          datasets: [
            {
              label: "Average Popularity",
              data: popularity,
              backgroundColor: "rgb(100, 166, 240)",
              borderColor: "rgba(255, 255, 255, 1)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          plugins: {
            legend: {
              labels: {
                color: "white",
              },
            },
          },
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                color: "white",
              },
              grid: {
                color: "rgba(255, 255, 255, 0.2)",
              },
            },
            x: {
              ticks: {
                color: "white",
              },
              grid: {
                color: "rgba(255, 255, 255, 0.2)",
              },
            },
          },
        },
      });
    })
    .catch((error) => console.error("Error fetching data:", error));
});
