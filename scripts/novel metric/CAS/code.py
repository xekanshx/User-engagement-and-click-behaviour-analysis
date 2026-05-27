from sklearn.preprocessing import MinMaxScaler
import numpy as np

scaler = MinMaxScaler()

# User segment
def segment_user(visits):
    if visits <= 5:
        return 'casual'
    elif visits <= 20:
        return 'regular'
    else:
        return 'power'

users_clean['user_segment'] = users_clean['visit_count'].apply(segment_user)

# Loyalty
users_clean['log_visits'] = np.log1p(users_clean['visit_count'])
users_clean['loyalty_score'] = scaler.fit_transform(users_clean[['log_visits']])

# Recency
users_clean['recency_days'] = 1 - scaler.fit_transform(users_clean[['days_since_last_read_es']])
users_clean['recency_articles'] = scaler.fit_transform(
    users_clean[['articles_read_last_30_days']])
users_clean['recency_score'] = (users_clean['recency_days'] * 0.6 +
                                 users_clean['recency_articles'] * 0.4)

# Breadth
users_clean['breadth_sports'] = scaler.fit_transform(users_clean[['no_of_sports_interested']])
users_clean['breadth_entities'] = scaler.fit_transform(users_clean[['no_of_entity_interested']])
users_clean['breadth_score'] = (users_clean['breadth_sports'] * 0.6 +
                                 users_clean['breadth_entities'] * 0.4)

# Interactivity
users_clean['interactivity_score'] = scaler.fit_transform(users_clean[['total_engagement']])

# CAS
users_clean['CAS'] = (
    users_clean['loyalty_score'] * 0.40 +
    users_clean['recency_score'] * 0.25 +
    users_clean['breadth_score'] * 0.20 +
    users_clean['interactivity_score'] * 0.15
)

users_clean['cas_tier'] = pd.cut(users_clean['CAS'],
    bins=[0, 0.2, 0.35, 1.0],
    labels=['Low', 'Medium', 'High'])

print(users_clean['CAS'].describe())
print("\nCAS by user segment:")
print(users_clean.groupby('user_segment')['CAS'].mean().round(3))

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# CAS distribution
axes[0].hist(users_clean['CAS'], bins=50, color='steelblue', edgecolor='white')
axes[0].set_title('Content Affinity Score Distribution')
axes[0].set_xlabel('CAS')
axes[0].set_ylabel('Number of Users')

# CAS by user segment
users_clean.groupby('user_segment')['CAS'].mean().plot(
    kind='bar', ax=axes[1],
    color=['#AED6F1', '#2E86C1', '#1B4F72'],
    width=0.5
)
axes[1].set_title('Average CAS by User Segment')
axes[1].set_xlabel('User Segment')
axes[1].set_ylabel('Average CAS')
axes[1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()

print(users_clean.groupby('user_segment')['CAS'].mean().round(3))
