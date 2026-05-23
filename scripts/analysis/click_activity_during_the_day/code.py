import matplotlib.pyplot as plt

hourly = related.groupby('click_hour').size().reset_index()
hourly.columns = ['hour', 'clicks']

plt.figure(figsize=(12, 5))

plt.plot(hourly['hour'], hourly['clicks'], marker='o', color='steelblue', linewidth=2)

plt.fill_between(hourly['hour'], hourly['clicks'], where=(hourly['hour'] >= 15) & (hourly['hour'] <= 19),
                 color='gold', alpha=0.3, label='Peak period (15-19)')

plt.title('Click Activity by Hour of Day')
plt.xlabel('Hour (0-23)')
plt.ylabel('Number of Clicks')
plt.xticks(range(0, 24))
plt.grid(axis='y', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(hourly)
