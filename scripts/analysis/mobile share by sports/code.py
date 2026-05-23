import matplotlib.pyplot as plt
import seaborn as sns

device_sport = related.groupby(['sport', 'device_type']).size().unstack(fill_value=0)
device_sport['mobile_pct'] = (device_sport['mobile'] /
                               device_sport.sum(axis=1) * 100).round(1)
print(device_sport.sort_values('mobile_pct', ascending=False))

plot_data = device_sport.sort_values('mobile_pct', ascending=False).reset_index()

plt.figure(figsize=(10, 8))
sns.barplot(data=plot_data, y='sport', x='mobile_pct', palette='coolwarm')
plt.title('Mobile Share of Related Clicks by Sport')
plt.xlabel('Mobile Clicks (%)')
plt.ylabel('Sport')
plt.xlim(0, 100)
plt.tight_layout()
plt.show()
