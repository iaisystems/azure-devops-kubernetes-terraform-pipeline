# Sample metrics log
data = {
    "service": ["web", "db", "api", "web", "db", "api"],
    "response_time_ms": [120, 200, 300, 150, 210, 310],
    "status_code": [200, 200, 500, 404, 200, 500]
}

df = pd.DataFrame(data)

# Calculate average response time per service
avg_response_per_service = df.groupby("service")["response_time_ms"].mean()
print("\nAverage Response Time per Service:")
print(avg_response_per_service)

# Count HTTP status codes by service
status_code_counts = df.groupby(["service", "status_code"]).size().unstack(fill_value=0)
print("\nHTTP Status Code Counts by Service:")
print(status_code_counts)
