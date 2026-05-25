import seaborn as sns

segment_analysis = users_clean.groupby('user_segment').agg({
    'timeonpage': 'mean',
    'no_of_sports_interested': 'mean',
    'articles_read_last_30_days': 'mean',
    'total_engagement': 'mean',
    'days_since_last_read_es': 'mean'
}).round(2)

print(segment_analysis)

segment_data = users_clean.groupby('user_segment').agg({
    'timeonpage': 'mean',
    'no_of_sports_interested': 'mean',
    'articles_read_last_30_days': 'mean',
    'total_engagement': 'mean',
    'days_since_last_read_es': 'mean'
}).round(2)

# Normalise for heatmap
segment_norm = (segment_data - segment_data.min()) / (segment_data.max() - segment_data.min())
segment_norm.columns = ['Time on Page', 'Sports Followed',
                        'Articles (30d)', 'Total Engagement', 'Days Since Last Read']

plt.figure(figsize=(10, 4))
sns.heatmap(segment_norm, annot=segment_data.values, fmt='.2f',
            cmap='Blues', linewidths=0.5)
plt.title('User Segment Behaviour Comparison', fontsize=14)
plt.tight_layout()
plt.show()
