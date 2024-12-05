# Simulated response times
data = {
    "response_time_ms": [100, 105, 110, 3000, 115, 120, 4000, 130, 125, 140]
}

df = pd.DataFrame(data)

# Calculate statistical bounds for anomaly detection
mean = df["response_time_ms"].mean()
std = df["response_time_ms"].std()
lower_bound = mean - (3 * std)
upper_bound = mean + (3 * std)

# Identify anomalies
anomalies = df[(df["response_time_ms"] < lower_bound) | (df["response_time_ms"] > upper_bound)]
print("\nDetected Anomalies:")
print(anomalies)
