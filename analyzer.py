import pandas as pd

# Sample Econet site data - Harare region
data = {
    'site': ['Harare CBD', 'Kuwadzana', 'Chitungwiza'],
    'latency_ms': [120, 45, 300],
    'packet_loss': [0.5, 0.1, 2.3]
}

df = pd.DataFrame(data)
df['status'] = df['latency_ms'].apply(lambda x: 'ALERT' if x > 100 else 'OK')

print("Network Report for Econet:")
print(df)
df.to_csv('network_report.csv', index=False)
print("\nReport saved - ready for NOC team")
