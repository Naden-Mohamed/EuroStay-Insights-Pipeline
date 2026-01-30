import csv
import os

def save_hotels(hotels):
    os.makedirs("scraped_data", exist_ok=True)
    file = "scraped_data/scraped_hotels.csv"

    if not hotels:
        print("No hotels to save — dataset is empty.")
        return

 
    file_exists = os.path.isfile(file) and os.path.getsize(file) > 0

    with open(file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=hotels[0].keys())
        
        if not file_exists:
            writer.writeheader()
            
        writer.writerows(hotels)
    
    print(f"Successfully appended {len(hotels)} hotels to {file}")


def save_rooms(rooms):
    if not rooms:
        return

    os.makedirs("scraped_data", exist_ok=True)
    file = "scraped_data/scraped_rooms.csv"
    
    file_exists = os.path.isfile(file) and os.path.getsize(file) > 0

    with open(file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rooms[0].keys())
        
        if not file_exists:
            writer.writeheader()
            
        writer.writerows(rooms)
