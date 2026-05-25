import matplotlib.pyplot as plt

# Do users click within their top sport or explore outside it?
related_with_segment['same_sport'] = (
    related_with_segment['sport'] == related_with_segment['top_sport']
)

loyalty = related_with_segment.groupby('user_segment')['same_sport'].mean().round(3) * 100
print(loyalty)

segment_order = ['casual', 'regular', 'power']
loyalty_values = [loyalty[seg] for seg in segment_order]
colors = ['#AED6F1', '#2E86C1', '#1B4F72']

plt.figure(figsize=(6, 5))
bars = plt.bar(segment_order, loyalty_values, color=colors, edgecolor='black')
plt.title('Sport Loyalty by User Segment\n(% of related clicks matching top sport)', fontsize=12)
plt.ylabel('Same-Sport Click Rate (%)')
plt.ylim(0, 100)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()
