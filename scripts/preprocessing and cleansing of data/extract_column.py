import pandas as pd
import re


# Step 1
def extract_sport(slug):
    slug_lower = slug.lower()
    # Specific long patterns first
    if 'college-football' in slug_lower:
        return 'college-football'
    elif 'college-basketball' in slug_lower:
        return 'college-basketball'
    elif 'wnba' in slug_lower:
        return 'wnba'
    elif 'wrestling' in slug_lower:
        return 'wrestling'
    elif 'gymnastics' in slug_lower:
        return 'gymnastics'
    elif 'volleyball' in slug_lower:
        return 'volleyball'
    elif 'boxing' in slug_lower:
        return 'boxing'
    elif 'nhl' in slug_lower:
        return 'nhl'
    elif 'nfl' in slug_lower:
        return 'nfl'
    elif 'nba' in slug_lower:
        return 'nba'
    elif 'mlb' in slug_lower:
        return 'mlb'
    elif 'golf' in slug_lower:
        return 'golf'
    elif 'nascar' in slug_lower:
        return 'nascar'
    elif 'olympics' in slug_lower:
        return 'olympics'
    elif 'ufc' in slug_lower:
        return 'ufc'
    elif 'tennis' in slug_lower:
        return 'tennis'
    else:
        return 'other'

related['sport'] = related['slug'].apply(extract_sport)

# Step 2
def device_type(ua):
    if pd.isna(ua):
        return 'unknown'
    ua_lower = ua.lower()
    if 'iphone' in ua_lower or 'android' in ua_lower:
        return 'mobile'
    elif 'ipad' in ua_lower or 'tablet' in ua_lower:
        return 'tablet'
    elif 'windows' in ua_lower or 'macintosh' in ua_lower or 'linux' in ua_lower:
        return 'desktop'
    else:
        return 'other'

related['device_type'] = related['ua'].apply(device_type)

# Step 3
related['timestamp'] = pd.to_datetime(related['timestamp'])
related['click_hour'] = related['timestamp'].dt.hour

# Step 4
related['source_group'] = related['source_group'].str.lower().str.strip()
related['source_group'] = related['source_group'].replace({'others': 'other', 'unknown': 'other'})

# Final
related_clean = related.drop(columns=['source', 'ua', 'date'])
print("\nCleaned and enriched related table shape:", related_clean.shape)
print("\nColumns:", related_clean.columns.tolist())
print("\nSport distribution:")
print(related_clean['sport'].value_counts())
print("\nDevice type distribution:")
print(related_clean['device_type'].value_counts())
print("\nClick hour distribution (first 5 hours):")
print(related_clean['click_hour'].value_counts().sort_index().head(10))
print("\nSource group distribution:")
print(related_clean['source_group'].value_counts())
