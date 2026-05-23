import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect(':memory:')
related.to_sql('related_posts', conn, index=False)

query = """
SELECT sport, COUNT(*) AS clicks
FROM related_posts
GROUP BY sport
ORDER BY clicks DESC
"""

sport_clicks = pd.read_sql(query, conn)

plt.figure(figsize=(12, 6))
plt.bar(sport_clicks['sport'], sport_clicks['clicks'], color='steelblue')
plt.xticks(rotation=45, ha='right')
plt.title('Related Post Clicks by Sport')
plt.xlabel('Sport')
plt.ylabel('Number of Clicks')
plt.tight_layout()
plt.show()

print(sport_clicks)
