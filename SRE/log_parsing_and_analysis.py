import pandas as pd

# Sample log data
log_data = {
    "timestamp": [
        "2024-12-01T10:15:30", "2024-12-01T10:16:00", "2024-12-01T10:17:00",
        "2024-12-01T10:17:30", "2024-12-01T10:18:00"
    ],
    "status_code": [200, 500, 200, 404, 500],
    "response_time_ms": [120, 850, 95, 200, 940],
    "url": ["/home", "/api", "/home", "/search", "/api"]
}

# Create a DataFrame
df = pd.DataFrame(log_data)

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Filter requests with errors (HTTP 500)
error_logs = df[df["status_code"] == 500]
print("\nError Logs:")
print(error_logs)

# Calculate average response time per URL
avg_response_time = df.groupby("url")["response_time_ms"].mean()
print("\nAverage Response Time by URL:")
print(avg_response_time)
