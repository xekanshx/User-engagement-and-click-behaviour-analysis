import matplotlib.pyplot as plt

def segment_user(visits):
    if visits <= 5:
        return 'casual'
    elif visits <= 20:
        return 'regular'
    else:
        return 'power'

users_clean['user_segment'] = users_clean['visit_count'].apply(segment_user)
print(users_clean['user_segment'].value_counts())
print(users_clean['user_segment'].value_counts(normalize=True).round(3) * 100)

segment_order = ['casual', 'regular', 'power']
segment_counts = users_clean['user_segment'].value_counts().reindex(segment_order)
segment_percent = (segment_counts / segment_counts.sum() * 100).round(1)

colors = ['#AED6F1', '#2E86C1', '#1B4F72']

plt.figure(figsize=(7,7))
plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.0f%%',
        startangle=90, colors=colors, textprops={'fontsize': 12})
plt.title('User Segment Share', fontsize=14)
plt.show()
