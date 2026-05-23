import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

users = pd.read_csv('data_task_users.csv')
related = pd.read_csv('data_task_related_entries_of_users.csv')

print("=== USERS DATASET ===")
print("Shape:", users.shape)
print("\nFirst 5 rows:")
display(users.head())

print("\nColumn names:")
print(users.columns.tolist())

print("\nData types:")
print(users.dtypes)

print("\nMissing values:")
print(users.isnull().sum())

print("\nBasic stats for numeric columns:")
display(users.describe())

print("\n=== RELATED POSTS ENGAGEMENT DATASET ===")
print("Shape:", related.shape)
print("\nFirst 5 rows:")
display(related.head())

print("\nColumn names:")
print(related.columns.tolist())

print("\nMissing values:")
print(related.isnull().sum())
