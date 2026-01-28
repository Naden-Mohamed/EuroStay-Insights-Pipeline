from selenium.webdriver.common.by import By
from utils.safe_find import safe_find_text, safe_find_elements
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_basic_info(driver,city_name):
    return {
        "hotel_name": safe_find_text(driver, By.CSS_SELECTOR, 'h2[class="a4ac75716e f546354b44 cc045b173b"]'),
        "city": city_name,
        "address": safe_find_text(driver, By.CSS_SELECTOR, 'div[class="b99b6ef58f cb4b7a25d9 b06461926f"]'),
        "rating": safe_find_text(driver, By.CSS_SELECTOR, 'div[class="f63b14ab7a dff2e52086"]')
    }


def scrape_facilities(driver):

    most_popular_facilities = []

    groups = safe_find_elements(
        driver,
        By.CSS_SELECTOR,
        'ul[class="e9f7361569 eb3a456445 b049f18dec"]'
    )

    for group in groups:
        try:
            items = group.find_elements(By.TAG_NAME, "li")
            for item in items:
                text = item.text.strip()
                if text:
                    most_popular_facilities.append(text)
        except:
            continue

    return list(set(most_popular_facilities))
def scrape_house_rules(driver):
    rules = {"check_in": "N/A", "check_out": "N/A"}

    rule_containers = driver.find_elements(By.CSS_SELECTOR, 'div.c92998be48')

    try:
        if len(rule_containers) > 0:
            check_in_elem = rule_containers[0].find_element(By.CSS_SELECTOR, 'div.b99b6ef58f')
            rules["check_in"] = check_in_elem.text.strip()

        if len(rule_containers) > 1:
            check_out_elem = rule_containers[1].find_element(By.CSS_SELECTOR, 'div.b99b6ef58f')
            rules["check_out"] = check_out_elem.text.strip()

    except Exception as e:
        print(f"Error scraping house rules: {e}")

    return rules["check_in"], rules["check_out"]

def scrape_area_info(driver):
    top_attractions = []
    try:
        section = driver.find_element(
            By.XPATH,
            '//div[@data-testid="poi-block"][.//h3[contains(.,"Top attractions")]]'
        )

        items = section.find_elements(
            By.CSS_SELECTOR,
            'ul[data-testid="poi-block-list"] li'
        )

        for item in items:
            text = item.text.strip()
            if text:
                top_attractions.append(text)
    except:
            pass

    return list(set(top_attractions))

def scrape_Restaurants_and_cafes(driver):
    restaurants = []

    try:
        section = driver.find_element(
            By.XPATH,
            '//div[@data-testid="poi-block"][.//h3[contains(.,"Restaurants & cafes")]]'
        )

        items = section.find_elements(
            By.CSS_SELECTOR,
            'ul[data-testid="poi-block-list"] li'
        )

        for item in items:
            text = item.text.strip()
            if text:
                restaurants.append(text)
    except:
            pass

    return list(set(restaurants))

def scrape_Public_transit(driver):
    public_transit = []
    try:
 
        xpath_selector = "//div[contains(text(), 'Public transit')]/following::ul[@data-testid='poi-block-list'][1]/li"
        
        wait = WebDriverWait(driver, 10)
        items = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath_selector)))

        for item in items:
            text = item.text.strip()
            if text:
                clean_text = " ".join(text.split())
                public_transit.append(clean_text)
    except Exception:
        pass
        
    return list(set(public_transit))
    
def scrape_closest_airports(driver):
    airports = []
    try:
        section = driver.find_element(
            By.XPATH,
            f'//div[@data-testid="poi-block"][.//h3[contains(.,"Closest Airports")]]'
        )
        items = section.find_elements(
            By.CSS_SELECTOR,
            'ul[data-testid="poi-block-list"] li'
        )
        for item in items:
            text = item.text.strip()
            if text:
                airports.append(text)
    except:
        pass
    return list(set(airports))
def is_parking_allowed(driver):
        parking_info = safe_find_text(
            driver, By.CSS_SELECTOR, 'div[class="b99b6ef58f fb14de7f14 fdf31a9fa1"]'
        )
        if parking_info and not "No" in parking_info.lower():
            return True
        return False

def scrape_languages_spoken(driver):
    languages = []
    

    xpath_options = [
        "//*[contains(text(), 'Languages Spoken')]/following::ul[1]/li",
        "//div[contains(., 'Languages Spoken')]/following::ul[1]/li",
        "//ul[contains(@class, 'e9f7361569')]/li" # Using the class from your screenshot
    ]

    try:
        # 2. Scroll to the bottom or middle of the page first
        # Many sites don't load the "Facilities" or "Languages" section until you scroll to it
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        time.sleep(1) # Give it a second to "lazy load"

        found_elements = []
        for xpath in xpath_options:
            try:
                # Wait a shorter time (3s) for each attempt
                found_elements = WebDriverWait(driver, 3).until(
                    EC.presence_of_all_elements_located((By.XPATH, xpath))
                )
                if found_elements:
                    break # Stop if we found something
            except e:
                continue

        # 3. Extract text
        for item in found_elements:
            val = item.get_attribute("textContent").strip()
            if val:
                languages.append(val)

    except Exception as e:
        print(f"Error during language scraping: {e}")
        
    return list(set(languages))
def is_pets_allowed(driver):
        pets_info = safe_find_text(
            driver, By.CSS_SELECTOR, 'div[class="b99b6ef58f"]'
        )
        if pets_info and not "No" in pets_info.lower():
            return True
        return False

