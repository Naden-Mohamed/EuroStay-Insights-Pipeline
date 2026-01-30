import csv
import os
import re

def repair_csv(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"Repairing {file_path}...")
    temp_output = file_path.replace(".csv", "_fixed.csv")
    rows_cleaned = 0

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.reader(f, skipinitialspace=True)
            
            header = next(reader)
            cleaned_header = [" ".join(h.replace('\n', ' ').split()).strip() for h in header]
            
            cleaned_rows = []
            for row in reader:
                cleaned_row = [" ".join(cell.replace('\n', ' ').replace('\r', ' ').split()).strip() for cell in row]
                
                if any(cleaned_row):
                    cleaned_rows.append(cleaned_row)
                    rows_cleaned += 1

        with open(temp_output, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(cleaned_header)
            writer.writerows(cleaned_rows)

        print(f"Successfully repaired {rows_cleaned} rows!")
        print(f"Fixed file saved as: {temp_output}")

    except Exception as e:
        print(f"Error during repair: {e}")

repair_csv("scraped_data/scraped_hotels.csv")
