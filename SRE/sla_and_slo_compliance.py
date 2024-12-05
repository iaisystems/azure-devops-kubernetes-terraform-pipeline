# Simulated API latency data
data = {
    "timestamp": pd.date_range(start="2024-12-01", periods=50, freq="T"),
    "latency_ms": np.random.randint(50, 500, size=50)
}

df = pd.DataFrame(data)
sla_threshold = 300  # Maximum allowed latency in milliseconds

# Calculate percentage of requests meeting SLA
sla_compliance = (df["latency_ms"] <= sla_threshold).mean() * 100
print(f"\nSLA Compliance Rate: {sla_compliance:.2f}%")
