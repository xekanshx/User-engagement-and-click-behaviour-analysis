import pandas as pd
users = pd.read_csv('data_task_users.csv')
users_clean = users.drop(columns=['age', 'gender', 'city'])
users_clean = users_clean.drop_duplicates(subset='ppid', keep='first').reset_index(drop=True)

print(f"Original rows: {len(users)}")
print(f"Rows after dropping demographics and duplicates: {len(users_clean)}")
print(f"Unique ppid: {users_clean['ppid'].nunique()}")

assert users_clean['ppid'].is_unique, "Still have duplicate ppid"
print("Verification passed: all ppid are unique.")
