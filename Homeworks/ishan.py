import pandas as pd

# Load Excel 1 and Excel 2
excel1 = pd.read_excel("Homeworks/excel1.xlsx")
excel2 = pd.read_excel("Homeworks/excel2.xlsx")

# Rename columns to ensure a common key for merge
excel1.rename(columns={"SUB ORDER ID": "Sub Order No"}, inplace=True)

# Merge on 'Sub Order No' to get Packet Id from Excel 2
merged = pd.merge(excel1, excel2[["Sub Order No", "Packet Id"]], on="Sub Order No", how="left")

# Fill the empty 'Packet Id' in Excel 1 with values from Excel 2
merged["Packet Id_x"] = merged["Packet Id_x"].fillna(merged["Packet Id_y"])

# Clean up columns
merged.drop(columns=["Packet Id_y"], inplace=True)
merged.rename(columns={"Packet Id_x": "Packet Id"}, inplace=True)

# Save updated Excel 1
merged.to_excel("updated_excel1.xlsx", index=False)
