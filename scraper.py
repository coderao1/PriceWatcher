import pandas as pd

def get_prices(item_name, ean, country, region):
    # Only use Excel file, pick lowest price per country
    import os
    excel_path = "c:\\Users\\jayasimhab\\OneDrive - Microsoft\\Development\\PriceWatcher\\pricewatcher\\Grocery_Price_Comp_new.xlsx"
    results = []
    try:
        ext = os.path.splitext(excel_path)[1].lower()
        if ext == ".xls":
            df = pd.read_excel(excel_path, engine="xlrd")
        elif ext == ".xlsx":
            df = pd.read_excel(excel_path, engine="openpyxl")
        else:
            raise ValueError("Unsupported file extension: {}".format(ext))
        # Normalize columns
        df.columns = [col.strip() for col in df.columns]
        # Filter by item name and country
        filtered = df[df['Item Name'].str.lower().str.contains(item_name.lower()) & df['Country'].str.lower().str.contains(country.lower())]
        if not filtered.empty:
            # Find row with lowest price
            filtered['Price_numeric'] = pd.to_numeric(filtered['Price'], errors='coerce')
            min_row = filtered.loc[filtered['Price_numeric'].idxmin()]
            results.append({
                'Store': min_row['store'] if 'store' in min_row else '',
                'Product': min_row['Item Name'],
                'Price': min_row['Price'],
                'Country': min_row['Country'],
                'Region': '',
                'EAN': ''
            })
        else:
            results.append({'Store': 'N/A', 'Product': item_name, 'Price': 'Not found', 'Country': country, 'Region': region, 'EAN': ean})
    except Exception as e:
        results.append({'Store': 'N/A', 'Product': item_name, 'Price': f'Error: {e}', 'Country': country, 'Region': region, 'EAN': ean})
    return results
