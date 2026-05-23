import pandas as pd
#check unique and dup ppid
print("Number of unique ppid:", users['ppid'].nunique())
print("Duplicated ppid count:", users['ppid'].duplicated().sum())
dup_ppid = users[users['ppid'].duplicated(keep=False)]
print("Sample of duplicated ppid rows:")
display(dup_ppid.head(10))

print("\n--- total_engagement non-null sample ---")
display(users[users['total_engagement'].notna()][['ppid', 'total_engagement', 'touchpoint_count']].head(10))

#check if other columns are varying other than the demographic ones
users = pd.read_csv('data_task_users.csv')

users_no_demo = users.drop(columns=['age', 'gender', 'city'])

dup_mask = users_no_demo.duplicated(subset='ppid', keep=False)
dup_users = users_no_demo[dup_mask]
dup_ppids = dup_users['ppid'].unique()

print(f"Total unique ppid: {users_no_demo['ppid'].nunique()}")
print(f"Number of ppid with duplicates: {len(dup_ppids)}")
print(f"Total duplicate rows: {len(dup_users)}")

cols_to_check = [c for c in users_no_demo.columns if c != 'ppid']
varying_cols = {}

for col in cols_to_check:
    varying_count = 0
    for pid in dup_ppids:
        subset = users_no_demo[users_no_demo['ppid'] == pid][col]
        if subset.nunique() > 1:
            varying_count += 1
    varying_cols[col] = varying_count

print("\nColumns that vary within at least one duplicate group:")
for col, count in varying_cols.items():
    if count > 0:
        print(f"  {col}: varies in {count} out of {len(dup_ppids)} duplicate groups")
    else:
        print(f"  {col}: always identical (no variation)")

# Show a few examples where a column varies
print("\n--- Example of varying column ---")
for col, count in varying_cols.items():
    if count > 0:
        # Find first duplicate group where this column varies
        for pid in dup_ppids:
            subset = users_no_demo[users_no_demo['ppid'] == pid]
            if subset[col].nunique() > 1:
                print(f"\nColumn '{col}' varies for ppid: {pid}")
                print(f"Values: {subset[col].tolist()}")
                break
        break
