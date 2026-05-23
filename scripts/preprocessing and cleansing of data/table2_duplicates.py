import pandas as pd
import re

related = related_raw.drop_duplicates().copy()
print(f"After dropping duplicates: {len(related)} rows (was {len(related_raw)})")
