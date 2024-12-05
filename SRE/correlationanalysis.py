# Simulated data
data = {
    "cpu_usage_percent": [50, 60, 70, 80, 90, 95, 100],
    "latency_ms": [100, 110, 130, 140, 170, 200, 250]
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df["cpu_usage_percent"].corr(df["latency_ms"])
print("\nCorrelation between CPU Usage and Latency:")
print(correlation)
