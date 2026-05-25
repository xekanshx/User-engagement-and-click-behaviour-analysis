import matplotlib.pyplot as plt
import numpy as np

def clean_referrer(ref):
    ref = str(ref).lower()
    if 'android-app' in ref or 'google' in ref:
        return 'google'
    elif 'facebook' in ref:
        return 'facebook'
    elif 'msn' in ref:
        return 'msn'
    elif 'reddit' in ref:
        return 'reddit'
    elif 'essentiallysports' in ref:
        return 'direct/internal'
    elif 'flipboard' in ref:
        return 'flipboard'
    elif 'unknown' in ref:
        return 'unknown'
    else:
        return 'other'

users_clean['referrer_group'] = users_clean['latest_referrer'].apply(clean_referrer)

referrer_analysis = users_clean.groupby('referrer_group').agg({
    'visit_count': 'mean',
    'timeonpage': 'mean',
    'articles_read_last_30_days': 'mean',
    'total_engagement': 'mean'
}).round(2).sort_values('visit_count', ascending=False)

print(referrer_analysis)
print("---")
print(users_clean['referrer_group'].value_counts())

referrer_stats = referrer_analysis.copy()
referrer_counts = users_clean['referrer_group'].value_counts()

# Align indices
common_idx = referrer_stats.index.intersection(referrer_counts.index)
referrer_stats = referrer_stats.loc[common_idx]
referrer_counts = referrer_counts[common_idx]

# Sort by visit_count descending
sorted_idx = referrer_stats['visit_count'].sort_values(ascending=False).index
referrer_stats = referrer_stats.loc[sorted_idx]
referrer_counts = referrer_counts[sorted_idx]

fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar plot: visit_count
x = np.arange(len(referrer_stats))
width = 0.6
bars = ax1.bar(x, referrer_stats['visit_count'], width, color='teal', alpha=0.7)
ax1.set_xticks(x)
ax1.set_xticklabels(referrer_stats.index, rotation=45, ha='right')
ax1.set_ylabel('Average Visit Count', color='teal')
ax1.tick_params(axis='y', labelcolor='teal')

# Secondary y-axis: user count
ax2 = ax1.twinx()
ax2.plot(x, referrer_counts, color='darkorange', marker='o', linestyle='-', linewidth=2, label='User Count')
ax2.set_ylabel('Number of Users', color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')

# Title and layout
plt.title('Referrer Group: Average Visit Count vs. User Count')
fig.tight_layout()
plt.show()

# Also show a bar chart of user counts
plt.figure(figsize=(10, 5))
referrer_counts.plot(kind='bar', color='lightseagreen')
plt.title('User Distribution by Referrer Group')
plt.xlabel('Referrer')
plt.ylabel('Number of Users')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
