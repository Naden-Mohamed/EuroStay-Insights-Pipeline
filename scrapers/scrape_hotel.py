from scrapers.hotel_page import (
    scrape_basic_info,
    scrape_facilities,
    scrape_house_rules,
    scrape_area_info,
    scrape_Restaurants_and_cafes,
    scrape_Public_transit,
    is_parking_allowed,
    scrape_languages_spoken,
    is_pets_allowed,
    scrape_closest_airports,

)

from scrapers.room_scraper import (
    get_room_type,
    get_beds,
    get_top_facilities,
    get_number_of_guests,
    get_price)

import time
import random

def scrape_hotel_page(driver, hotel_url, city):
    driver.get(hotel_url)
    time.sleep(random.uniform(4, 7))

    hotel_data = scrape_basic_info(driver,city)
    hotel_data["top_attractions"] = scrape_area_info(driver)
    hotel_data["Restaurants & cafes"] = scrape_Restaurants_and_cafes(driver)
    hotel_data["Public transit"] = scrape_Public_transit(driver)
    hotel_data["Closest Airports"] = scrape_closest_airports(driver)
    hotel_data["Parking"] = is_parking_allowed(driver)
    hotel_data["Languages Spoken"] = scrape_languages_spoken(driver)
    hotel_data["Check_in"] , hotel_data["Check_out"] = scrape_house_rules(driver)
    hotel_data["Pets_allowance"] = is_pets_allowed(driver)
    hotel_data["facilities"] = scrape_facilities(driver)

    # rooms = scrape_room_details(driver)

    # hotel_name = hotel_data["hotel_name"]
    # # attach hotel reference
    # for room in rooms:
    #     room["hotel_name"] = hotel_name
    #     room["city"] = city

    return hotel_data

def scrape_room_details(driver, hotel_url, city):
    driver.get(hotel_url)
    time.sleep(random.uniform(3, 5))
    
    # 1. Scrape Hotel Name for reference
    try:
        hotel_name = driver.find_element(By.CSS_SELECTOR, 'h2.pp-header__title, h2.d2f04c8189').text.strip()
    except:
        hotel_name = "Unknown Hotel"

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.4);")
    time.sleep(2)

    rooms_list = []
    room_rows = driver.find_elements(By.CSS_SELECTOR, 'tr[data-testid="room-row"]')

    for row in room_rows:
        try:
            room_data = {
                "city": city,
                "hotel_name": hotel_name,
                "room_type": get_room_type(row),
                "beds": get_beds(row),
                "top_facilities": get_top_facilities(row),
                "number_of_guests": get_number_of_guests(row),
                "price": get_price(row),
                "hotel_url": hotel_url
            }

            if room_data["room_type"] or room_data["price"]:
                rooms_list.append(room_data)
        except Exception as e:
            print(f"Skipping a row due to error: {e}")

    return rooms_list