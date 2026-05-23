# Table 1 verification
print("TABLE 1 — users_clean")
print(f"Shape: {users_clean.shape}")
print(f"Nulls:\n{users_clean.isnull().sum()}")
print(f"Duplicate PPIDs: {users_clean.duplicated(subset='ppid').sum()}")
print(f"\nSample:\n{users_clean.head(3)}")

print("\n---\n")

# Table 2 verification
print("TABLE 2 — related")
print(f"Shape: {related.shape}")
print(f"Nulls:\n{related.isnull().sum()}")
print(f"Duplicate rows: {related.duplicated().sum()}")
print(f"\nSample:\n{related.head(3)}")
