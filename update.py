def save_cleaned_inventory(df, path="data/inventory_cleaned.csv"):
    df.to_csv(path, index=False)
    print(f"✅ Cleaned inventory saved to {path}")
