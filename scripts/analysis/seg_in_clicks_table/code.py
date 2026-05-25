import matplotlib.pyplot as plt

# How many users in related table are casual vs regular vs power?
related_with_segment = related.merge(
    users_clean[['ppid', 'user_segment', 'no_of_sports_interested']],
    on='ppid',
    how='left'
)
print(related_with_segment['user_segment'].value_counts())

related_with_segment = related.merge(
    users_clean[['ppid', 'user_segment', 'no_of_sports_interested', 'top_sport']],
    on='ppid',
    how='left'
)

print(related_with_segment['user_segment'].value_counts())
print("---")

# Click share vs user share comparison
segment_counts = users_clean['user_segment'].value_counts()
click_counts = related_with_segment['user_segment'].value_counts()

comparison = pd.DataFrame({
    'user_share': (segment_counts / segment_counts.sum() * 100).round(1),
    'click_share': (click_counts / click_counts.sum() * 100).round(1)
})

comparison['click_to_user_ratio'] = (comparison['click_share'] / comparison['user_share']).round(2)
print(comparison)

segments_order = ['casual', 'regular', 'power']
click_shares = [comparison.loc[seg, 'click_share'] for seg in segments_order]

colors = ['#AED6F1', '#2E86C1', '#1B4F72']

plt.figure(figsize=(7,7))
plt.pie(click_shares, labels=segments_order, autopct='%1.0f%%',
        startangle=90, colors=colors, textprops={'fontsize': 12})
plt.title('Share of Related Clicks by Segment', fontsize=14)
plt.show()
