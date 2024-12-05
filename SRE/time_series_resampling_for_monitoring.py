# Simulated metrics data
metrics_data = {
    "timestamp": pd.date_range(start="2024-12-01", periods=10, freq="T"),
    "cpu_usage": [50, 60, 65, 55, 70, 80, 75, 65, 60, 55],
    "memory_usage": [70, 72, 75, 71, 74, 76, 78, 73, 72, 70]
}

# Create a DataFrame
df = pd.DataFrame(metrics_data)
df.set_index("timestamp", inplace=True)

# Resample to calculate average CPU and memory usage per 5 minutes
resampled_metrics = df.resample("5T").mean()
print("\nResampled Metrics (5-minute intervals):")
print(resampled_metrics)
