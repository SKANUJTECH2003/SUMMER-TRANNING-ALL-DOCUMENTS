import pandas as pd
from pathlib import Path

# Read the dataset
csv_path = Path(__file__).with_name("netflix_dataset.csv")
df = pd.read_csv(csv_path)

print("=== Pandas Practice on Netflix Dataset ===")

# 1. View first and last rows
print("\n1. First 5 rows:")
print(df.head())

print("\n2. Last 5 rows:")
print(df.tail())

# 2. Basic information about the DataFrame
print("\n3. Shape of the DataFrame:")
print(df.shape)

print("\n4. Column names:")
print(df.columns.tolist())

print("\n5. Data types:")
print(df.dtypes)

print("\n6. Summary statistics:")
print(df.describe(include="all"))

print("\n7. Information about the DataFrame:")
print(df.info())

# 3. Missing values
print("\n8. Missing values count:")
print(df.isnull().sum())

# 4. Selecting columns
print("\n9. Selected columns:")
print(df[["title", "release_year", "views_millions"]].head())

# 5. Filtering rows
print("\n10. Movies released after 2020:")
print(df[df["release_year"] >= 2020].head())

# 6. Sorting values
print("\n11. Sorted by views (highest first):")
print(df.sort_values("views_millions", ascending=False).head())

# 7. Grouping and aggregation
print("\n12. Average views by genre:")
print(df.groupby("genre")["views_millions"].mean().sort_values(ascending=False))

# 8. Value counts
print("\n13. Top countries:")
print(df["country"].value_counts().head())

# 9. Creating a new column
print("\n14. Add a new column: views_per_minute")
df["views_per_minute"] = df["views_millions"] / df["duration_min"]
print(df[["title", "views_millions", "duration_min", "views_per_minute"]].head())

# 10. Applying a function
print("\n15. Rating category using apply():")
df["rating_category"] = df["rating"].apply(lambda x: "High" if x >= 8 else "Low")
print(df[["title", "rating", "rating_category"]].head())

# 11. Renaming columns
print("\n16. Rename a column:")
renamed_df = df.rename(columns={"views_millions": "views_in_millions"})
print(renamed_df[["title", "views_in_millions"]].head())

# 12. Using query()
print("\n17. Query example: release_year >= 2020 and views > 100")
print(df.query("release_year >= 2020 and views_millions > 100").head())

print("\nDone! You can now study each section one by one.")
