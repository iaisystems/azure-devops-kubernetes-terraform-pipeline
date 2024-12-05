# Simulated traffic data
data = {
    "timestamp": pd.date_range(start="2024-12-01", periods=100, freq="T"),
    "requests": np.random.poisson(lam=10, size=100)
}

df = pd.DataFrame(data)
df.set_index("timestamp", inplace=True)

# Detect spikes (requests greater than 1.5x the mean)
threshold = df["requests"].mean() * 1.5
spikes = df[df["requests"] > threshold]
print("\nTraffic Spikes Detected:")
print(spikes)
