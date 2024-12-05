import numpy as np

# Simulated large dataset
np.random.seed(42)
large_data = {
    "timestamp": pd.date_range(start="2024-12-01", periods=100000, freq="S"),
    "status_code": np.random.choice([200, 404, 500], size=100000, p=[0.8, 0.15, 0.05]),
    "response_time_ms": np.random.normal(200, 50, size=100000)
}

df = pd.DataFrame(large_data)

# Filter logs with HTTP 500 errors
error_logs = df[df["status_code"] == 500]

# Sample 1000 rows from the filtered logs
sampled_logs = error_logs.sample(1000)
print("\nSampled Logs (HTTP 500):")
print(sampled_logs.head())
