import ast
import re

# Define parsing function for the specific format
def parse_touchpoint(tp_str):
    if pd.isna(tp_str):
        return {}
    # Example: '{poll=1}' or '{quiz=51, poll=40}'
    pattern = r'(\w+)=(\d+)'
    matches = re.findall(pattern, tp_str)
    return {key: int(value) for key, value in matches}

users_clean['touchpoint_dict'] = users_clean['touchpoint_count'].apply(parse_touchpoint)
#normalize
print(users_clean[['ppid', 'touchpoint_count', 'touchpoint_dict']].head())

for key in all_keys:
    users_clean[key + '_count'] = users_clean['touchpoint_dict'].apply(lambda d: d.get(key, 0))

# Drop the old touchpoint columns
users_clean = users_clean.drop(columns=['touchpoint_count', 'touchpoint_dict'])

# Verify new columns
print("New columns added:", [c for c in users_clean.columns if '_count' in c and c not in ['visit_count', 'visit_count']])
print("\nFirst 5 rows with new engagement counts:")
print(users_clean[['ppid', 'poll_count', 'quiz_count', 'comment_count']].head(10))

#convert more columns
users_clean = users_clean.rename(columns={
    'sports_with_visit_count': 'sports_visit_count',
    'entity_with_visit_count': 'entity_visit_count',
    'source_with_visit_count': 'source_visit_count'
})

def parse_dict_str(dict_str):
    if pd.isna(dict_str):
        return {}
    # Format: {key1=value1, key2=value2, ...}
    pattern = r'(\w+)=(\d+)'
    matches = re.findall(pattern, dict_str)
    return {key: int(value) for key, value in matches}

# Apply parsing to create new dict columns
users_clean['sports_dict'] = users_clean['sports_visit_count'].apply(parse_dict_str)
users_clean['entity_dict'] = users_clean['entity_visit_count'].apply(parse_dict_str)
users_clean['source_dict'] = users_clean['source_visit_count'].apply(parse_dict_str)

print("Sample rows with new dict columns:")
print(users_clean[['ppid', 'sports_dict', 'entity_dict', 'source_dict']].head(10))
