import matplotlib.pyplot as plt
import numpy as np


sport_users = users_clean['top_sport'].value_counts().reset_index()
sport_users.columns = ['sport', 'user_count']

sport_analysis = sport_clicks.merge(sport_users, on='sport', how='left')
sport_analysis['clicks_perc'] = (sport_analysis['clicks'] /
                                      sport_analysis['user_count']).round(3)
print(sport_analysis.sort_values('clicks_perc', ascending=False))


plot_df = sport_analysis.sort_values('user_count', ascending=False)

fig, ax1 = plt.subplots(figsize=(14, 6))

x = np.arange(len(plot_df))
width = 0.6
bars = ax1.bar(x, plot_df['user_count'], width, color='steelblue', alpha=0.7, label='User Count')
ax1.set_xlabel('Sport')
ax1.set_ylabel('Number of Users (top sport)', color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue')
ax1.set_xticks(x)
ax1.set_xticklabels(plot_df['sport'], rotation=45, ha='right')

ax2 = ax1.twinx()
line = ax2.plot(x, plot_df['clicks_perc'], color='darkorange', marker='o', linewidth=2, markersize=6, label='Clicks per User')
ax2.set_ylabel('Average Clicks per User', color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')

plt.title('User Count vs. Related Clicks per User by Top Sport')
fig.tight_layout()
plt.show()
