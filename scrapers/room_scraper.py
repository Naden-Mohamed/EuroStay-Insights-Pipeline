from selenium.webdriver.common.by import By
from utils.safe_find import safe_find_elements
import re


def get_room_type(row):
    """Extracts the name/type of the room."""
    try:
        return row.safe_find_elements(By.CSS_SELECTOR, 'span[class="hprt-roomtype-icon-link "]').text.strip()
    except:
        return None

def get_beds(row):
    """Extracts and parses bed counts and types."""
    beds = []
    try:
        bed_items = row.safe_find_elements(By.CSS_SELECTOR, 'ul[class="rt-bed-types"]')
        for bed in bed_items:
            text = bed.text.lower()
            match = re.search(r'(\d+)\s+(.*)', text)
            if match:
                beds.append({
                    "count": int(match.group(1)),
                    "type": match.group(2)
                })
    except:
        pass
    return beds

def get_top_facilities(row):
    """Extracts the short list of facility icons."""
    facilities = []
    try:
        badges = row.find_elements(By.CSS_SELECTOR, 'div[data-testid="facility-icons"] span')
        for badge in badges:
            text = badge.text.strip()
            if text:
                facilities.append(text)
    except:
        pass
    return facilities

def get_number_of_guests(row):
    """Extracts the maximum occupancy for the room."""
    try:
        occupancy_elem = row.find_element(By.CSS_SELECTOR, 'span[data-testid="occupancy-config"]')
        # Uses regex to find the digit in 'x 2' or '2 guests'
        match = re.search(r'\d+', occupancy_elem.text)
        return int(match.group()) if match else None
    except:
        return None

def get_price(row):
    """Extracts the displayed price."""
    try:
        return row.find_element(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]').text.strip()
    except:
        return None


