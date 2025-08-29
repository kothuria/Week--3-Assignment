def alert_low_stock(df):
    low_stock = df[df["ReorderQty"] > 0]
    if not low_stock.empty:
        print("\n⚠️ Low Stock Items:")
        print(low_stock[['SKU', 'Description', 'OnHandQty', 'ReorderQty']])
    else:
        print("\n✅ No items need restocking.")
