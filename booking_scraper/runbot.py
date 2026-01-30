from random import random
from booking.booking import Booking
from scrapers.scrape_hotel import scrape_hotel_page,scrape_room_details
from utils.storage import save_hotels, save_rooms
import time

cities = ["Barcelona"]

with Booking() as bot:
    bot.maximize_window()
    bot.land_first_page()
    bot.close_popup()
    bot.change_currency("USD")


    # Scarping hotels
    for city in cities:
        print(f"\n Scraping city: {city}")
        bot.reset_to_home()
        bot.clear_search_field()
        bot.select_place_to_go(city)
        bot.ignore_date()
        bot.click_search()
        time.sleep(5)

        hotel_links = bot.get_all_hotel_links(max_hotels=5)
        print(f"Found {len(hotel_links)} hotels in {city}")

        hotels_dataset = []
        for idx, link in enumerate(hotel_links):
                print(f"[{idx+1}/{len(hotel_links)}] {city} hotel")

                try:
                    hotel = scrape_hotel_page(bot, link, city)
                    hotels_dataset.append(hotel)
                    # ؟save_rooms(rooms, link)

                except Exception as e:
                    print(" Failed hotel:", e)
                    continue

                time.sleep(2) 
        save_hotels(hotels_dataset)
        print(f"Finished {city}")


    # Scraping rooms only

    # for city in cities:
    #         print(f"\nScraping city: {city}")
    #         bot.reset_to_home()
    #         bot.clear_search_field()
    #         bot.select_place_to_go(city)
    #         bot.ignore_date() 
    #         bot.click_search()
    #         time.sleep(5)

    #         hotel_links = bot.get_all_hotel_links(max_hotels=5)
    #         print(f"Found {len(hotel_links)} hotels in {city}")

    # for idx, link in enumerate(hotel_links):
    #     print(f"[{idx+1}/{len(hotel_links)}] Scraping rooms for hotel in {city}...")

    #     try:
    #         rooms_data = scrape_room_details(bot, link, city)
                
    #         if rooms_data:
    #             save_rooms(rooms_data)
    #             print(f" Saved {len(rooms_data)} rooms.")
    #         else:
    #             print(" No rooms found for this hotel.")

    #     except Exception as e:
    #         print(f" Failed to scrape hotel at {link}: {e}")
    #         continue

    #     time.sleep(random.uniform(2, 4))

    #     print(f"🏁 Finished the rooms on all hotels in {city}")