users_clean['total_engagement'] = users_clean['total_engagement'].fillna(0).astype(int)
print("Missing values in total_engagement after fill:", users_clean['total_engagement'].isnull().sum())
print("Sample values:")
print(users_clean[['ppid', 'total_engagement']].head())

users_clean['top_entity'] = users_clean['top_entity'].fillna('None')
users_clean['top_entity_visits'] = users_clean['top_entity_visits'].fillna(0)
