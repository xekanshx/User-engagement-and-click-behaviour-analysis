engagement_segment = users_clean.groupby('user_segment').agg({
    'poll_count': 'mean',
    'quiz_count': 'mean',
    'comment_count': 'mean'
}).round(3)

print(engagement_segment)

fig, ax = plt.subplots(figsize=(9, 5))

x = range(len(engagement_segment.index))
width = 0.25

bars1 = ax.bar([i - width for i in x], engagement_segment['poll_count'],
               width=width, label='Polls', color='#2E86C1')
bars2 = ax.bar(x, engagement_segment['quiz_count'],
               width=width, label='Quizzes', color='#28B463')
bars3 = ax.bar([i + width for i in x], engagement_segment['comment_count'],
               width=width, label='Comments', color='#E74C3C')

ax.set_xticks(x)
ax.set_xticklabels(['Casual', 'Power', 'Regular'], fontsize=11)
ax.set_title('Average Poll, Quiz & Comment Engagement by User Segment', fontsize=13)
ax.set_xlabel('User Segment')
ax.set_ylabel('Average Count per User')
ax.legend()
plt.tight_layout()
plt.show()
