import seaborn as sns

corr_cols = ['visit_count', 'timeonpage', 'total_engagement',
             'no_of_sports_interested', 'articles_read_last_30_days',
             'days_since_last_read_es']

corr_matrix = users_clean[corr_cols].corr().round(2)

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm',
            center=0, linewidths=0.5)
plt.title('Feature Correlation Matrix')
plt.tight_layout()
plt.show()
