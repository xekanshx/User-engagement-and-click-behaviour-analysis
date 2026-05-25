sport_segment = users_clean.groupby(['top_sport', 'user_segment']).size().unstack(fill_value=0)
sport_segment = sport_segment.loc[sport_segment.sum(axis=1).sort_values(ascending=False).head(10).index]
print(sport_segment)

fig, ax = plt.subplots(figsize=(12, 6))

sport_segment.plot(
    kind='bar',
    stacked=True,
    ax=ax,
    color=['#AED6F1', '#2E86C1', '#1B4F72'],
    width=0.6
)

ax.set_title('User Segment Distribution by Sport', fontsize=14, pad=15)
ax.set_xlabel('Sport', fontsize=11)
ax.set_ylabel('Number of Users', fontsize=11)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.legend(['Casual', 'Power', 'Regular'], loc='upper right')

for i, sport in enumerate(sport_segment.index):
    total = sport_segment.loc[sport].sum()
    power_pct = (sport_segment.loc[sport, 'power'] / total * 100).round(1)
    ax.text(i, total + 20, f'{power_pct}% power',
            ha='center', fontsize=8, color='#1B4F72')

plt.tight_layout()
plt.show()
