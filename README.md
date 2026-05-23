# User-engagement analyis for a sports news platform

User Engagement Analysis for a sports news platform

## Overview
An end-to-end exploratory data analysis of user behavior and engagement patterns on a top 10 US sports media platform. The analysis covers 10,000 users and their interactions with related post content, uncovering actionable insights around sport preferences, device behavior, traffic quality, and user segmentation.

---

## Dataset
Two tables provided:
- **data_task_users** — user profiles including visit count, time on page, sport interests, referrer, engagement metrics, and touchpoint data
- **data_task_related_entries_of_users** — related post click events including article slug, timestamp, user agent, and source group

---

## Workflow

### 1. Data Cleaning & Preprocessing
- Identified and resolved duplicate PPIDs with inconsistent demographic columns — dropped age, gender and city due to 50-60% null rates and cross-record inconsistency
- Parsed semi-structured string columns using regex — extracted poll, quiz and comment counts from touchpoint_count into separate features
- Retained sports_dict and entity_dict as dictionaries due to high cardinality
- Extracted sport category from article slugs using keyword matching
- Extracted device type from user agent strings and click hour from timestamps
- Removed 51% duplicate rows from the related posts table
- Filled null engagement values with 0 and resolved remaining nulls in top_entity and top_entity_visits


### 2. Exploratory Analysis
- **Sport popularity** — college football and NFL together account for 39% of all related post clicks
- **Click rate per user** — NFL has the largest audience but lowest related post engagement per user, representing the highest opportunity for recommendation improvement
- **Device behavior** — volleyball, combat sports and NFL/NBA audiences are mobile-heavy; MLB, NASCAR and Olympics audiences are desktop-heavy
- **Peak activity** — click activity peaks between 3-7pm, with late night traffic likely representing US-based users
- **Referrer quality** — Google drives 75% of traffic; Flipboard users are smallest in volume but highest in average visit count and loyalty
- **User segmentation** — users segmented into casual (61%), regular (27%) and power (12%) based on visit count thresholds informed by data distribution
- **Sport loyalty** — casual users click within their top sport 86% of the time; power users are more exploratory at 67.4%
- **Segment click share** — power users represent 12% of audience but drive disproportionate related post engagement

<img width="592" height="582" alt="image" src="https://github.com/user-attachments/assets/aa41d78c-186c-4763-892e-55498465e63b" />

<img width="1389" height="590" alt="image" src="https://github.com/user-attachments/assets/8bb0e76c-e505-4888-9447-3f86abc74afc" />

<img width="764" height="590" alt="image" src="https://github.com/user-attachments/assets/59f66a4e-97b0-43df-a5c6-f8930173ec0c" />


### 3. Novel Metric — Content Affinity Score (CAS)
A composite weighted engagement score built to quantify user quality beyond simple segmentation:

| Component | Weight | Description |
|---|---|---|
| Loyalty | 40% | Log-transformed visit count |
| Recency | 25% | Days since last read + articles read in last 30 days |
| Breadth | 20% | Number of sports and entities followed |
| Interactivity | 15% | Total poll and quiz engagement |

All components normalized using MinMaxScaler before combining. CAS tiered into Low (53%), Medium (35%) and High (11%) — distribution aligns with visit-based segmentation confirming metric validity.

**Key findings:**
- Golf, college football and WNBA users have highest average CAS despite smaller audiences
- High CAS users are the most valuable targets for recommendation personalization

### 4. Additional Metrics Proposed
Three metrics identified that cannot be calculated from current data but would significantly improve engagement understanding:
- **Scroll Depth Score** — tracks how far users scroll in articles, more accurate than time on page
- **Related Post CTR** — requires impression data to calculate click through rate per user per sport
- **Session Depth** — number of articles read per session, stronger signal than total visit count

---

## Tools & Technologies
- **Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, SQLite3, Regex
- **Environment:** Google Colab
- **SQL:** SQLite3 in-memory database for analytical queries

---

## Key Insights Summary
- NFL is the biggest audience but most underutilized for related post engagement — highest ROI for recommendation improvement
- Mobile-first widget design should be prioritized for volleyball, combat sports, NFL and NBA audiences
- Flipboard referrals are small in volume but highest in user quality — worth investing in content distribution there
- 61% of users are casual with limited history — any recommendation system must handle cold start users effectively
- Power users follow 6 sports on average vs 1.6 for casual — recommendation diversity should scale with user segment

