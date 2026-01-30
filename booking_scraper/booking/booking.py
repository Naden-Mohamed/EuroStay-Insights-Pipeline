
from booking import constant as const
from booking.filters import BookingFiltration
from booking import helpers
import os
import datetime
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class Booking(webdriver.Chrome):

    # private variables are not accessible outside the class.
    _date_checkin = ""
    _date_checkout = ""
    _adults = 0
    _rooms = 0
    _place = ""

    def __init__(
        self,
        driver_path=r"C:\Users\gilbe\Desktop\workstation\projects\scrape\SeleniumDrivers",
        teardown=True,
    ):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        super(Booking, self).__init__(options=chrome_options)


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def __enter__(self):
        return self


    def set_proxy(self):

        ip_address = "199.195.254.168:8118"

        self.desired_capabilities["proxy"] = {
            "httpProxy": ip_address,
            "ftpProxy": ip_address,
            "sslProxy": ip_address,
            "proxyType": "MANUAL",
        }

    def land_first_page(self):
        self.get(const.BASE_URL)

    def get_current_window_handle(self):

        return self.window_handles
     
    def close_popup(self):
        try:
            popup_element = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]'
            )
            popup_element.click()
        except NoSuchElementException:
            pass


    def change_currency(self, currency="USD"):
        wait = WebDriverWait(self, 30)

        try:
            currency_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
                )
            )

            self.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                currency_button
            )
            time.sleep(1)

            self.execute_script("arguments[0].click();", currency_button)

        except TimeoutException:
            raise RuntimeError("Currency button not clickable")

        currency_option = wait.until(
            EC.element_to_be_clickable(
                ( By.XPATH,
                f'//div[contains(@class,"CurrencyPicker_currency") and normalize-space()="{currency}"]')
            )
        )

        self.execute_script("arguments[0].click();", currency_option)
        time.sleep(2)



    def select_place_to_go(self, place_to_go):
        wait = WebDriverWait(self, 30)

        search_field = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="ss"]'))
        )

        search_field.clear()
        search_field.send_keys(place_to_go)

        search_field.click()
        self.place = place_to_go


    def click_date_box(self):

        """
        clicks the previous month button after the first iteration.
        """

        elem = self.find_element(By.CSS_SELECTOR, 'div[class="xp__dates-inner"]')
        elem.click()
        prev_month_status = True
        while prev_month_status:
            try:
                self.calendar_prev_month_button()

            except ElementNotInteractableException or ElementNotSelectableException or NoSuchElementException:
                prev_month_status = False

        print("click date !!!")


    def vocation_month(self, month: str):
        """_summary_

        :param month: the month you want to go to vacation.
        """
        voc_month = helpers.when_is_vocation(month)
        today_date = datetime.datetime.now()
        year = today_date.year
        start_date = voc_month + " " + str(year)

        if today_date.strftime("%B") != month.capitalize():
            status = True
            while status:
                calendar = self.find_element(
                    By.CSS_SELECTOR, 'div[data-bui-ref="calendar-content"]'
                )
                m = calendar.find_elements(
                    By.CSS_SELECTOR, 'div[data-bui-ref="calendar-month"]'
                )
                ele = m[0].find_element(
                    By.CSS_SELECTOR, 'div[class="bui-calendar__month"]'
                )

                if ele.get_attribute("innerHTML") == start_date:
                    print("this element was found")
                    print("the date", start_date, "was found")
                    status = False
                    break
                else:
                    try:
                        self.calendar_next_month_button()

                    except NoSuchElementException or ElementNotInteractableException:
                        pass
        else:
            pass

    def calendar_next_month_button(self):
        """
        clicks next month icon
        """
        try:
            next_month = self.find_element(
                By.CSS_SELECTOR, 'div[data-bui-ref="calendar-next"]'
            )
            next_month.click()

        except ElementNotInteractableException or NoSuchElementException:
            pass

    def calendar_prev_month_button(self):
        """
        clicks previous month icon
        can be used to go back to previous month,
        """
        prev_month = self.find_element(
            By.CSS_SELECTOR, 'div[data-bui-ref="calendar-prev"]'
        )
        prev_month.click()

    def select_dates(self, checkin: str, checkout: str):
        """_summary_
        Booking.com only allows a maximum of 45 nights; approximately 1.5 months.
        For easy scraping we recommend you keep the date range between one month that is 2022-05-01 - 2022-06-01
        e.i a maximum of 30 days. By default, if the start_month is current_month, the checkin date will start from current_date i.e current month and day.
        This is because, booking.com doesn't allow checkin of past dates.
        Otherwise, if you are planning checkin one month from now, then the checkin start date will always be the first day of
        desired month and checkout will be first day of next month.
        check helpers.py file on `construct_date()` also check `constants.py`

        Args:
            checkin (str): Booking.com checkin date.

            checkout (str): Booking.com checkout date.

        """
        check_in = self.find_element(By.CSS_SELECTOR, f'td[data-date="{checkin}"]')
        check_in.click()

        check_out = self.find_element_by_css_selector(f'td[data-date="{checkout}"]')
        check_out.click()

        Booking.date_checkin = checkin
        Booking.date_checkout = checkout

    def ignore_date(self):
        """_summary_
        This method will ignore date selection on booking.com
        """
        calender_container = self.find_element(By.CSS_SELECTOR, 'button[data-testid="searchbox-dates-container"]')
        calender_container.click()
    def select_adult(self, adult: int, rooms: int):
        #
        """
        Selects the number of adults per room.
        Args:
        Adult (int): Number of adults per room.

        """
        selection_element = self.find_element_by_id("xp__guests__toggle")
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()

            # if the value of adults reaches 1, then we should get out of the loop
            adults_value_element = self.find_element_by_id("group_adults")
            adults_value = adults_value_element.get_attribute("value")

            if int(adults_value) == 1:
                break

        add_adult = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(adult - 1):
            add_adult.click()

        add_rooms = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Rooms"]'
        )
        for _ in range(rooms - 1):
            add_rooms.click()

        Booking.adults = adult
        Booking.rooms = rooms

    def click_search(self):
        search_element = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_element.click()

    def clear_search_field(self):
        try:
                search_field = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="ss"]'))
                )
                
                search_field.clear()
                

                search_field.send_keys(Keys.CONTROL + "a")
                search_field.send_keys(Keys.BACKSPACE)
                
                time.sleep(1)
                
        except Exception as e:
                print(f"Error clearing search field: {e}")

    def apply_filtration(self):
        filter = BookingFiltration(driver=self)
        filter.apply_star_rating(3, 4, 5)
        filter.sort_price()

    def get_all_hotel_links(self, max_hotels=30,max_pages=5):
        all_links = set()

        for _ in range(max_pages):
            time.sleep(3)

            hotels = self.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

            for hotel in hotels:
                try:
                    link = hotel.find_element(
                        By.CSS_SELECTOR, 'a[data-testid="title-link"]'
                    ).get_attribute("href")
                    all_links.add(link)
                except:
                    continue

            if len(all_links) >= max_hotels:
                break

            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            try:
                self.load_more_results()
            except:
                pass

        return list(all_links)[:max_hotels]


    def get_hotels_list(self):
        hotels_list = self.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]'
        )
        links = []
        for hotel in hotels_list:
            try:
                link = hotel.find_element(By.CSS_SELECTOR, 'a[data-testid="title-link"]')
                links.append(link.get_attribute("href"))
            except NoSuchElementException:
                continue
        return list(set(links))  
    
    def load_more_results(self):
        """
        This method will load more results on the search results page.
        """
        try:
            load_more_button = self.find_element(
                By.CSS_SELECTOR, 'button[class="de576f5064 b46cd7aad7 d0a01e3d83 dda427e6b5 eed37d6a9d bbf83acb81 a0ddd706cc"]'
            )
            load_more_button.click()
        except NoSuchElementException:
            print("No more results to load.")

    def report_results(self):
        """_summary_
        This method will report the results of the search found on the page.
        """
        report = BookingReport(report_driver=self)
        collection_list = report.pull_deal_box_attributes(
            checkin=Booking._date_checkin,
            checkout=Booking._date_checkout,
            adult=Booking._adults,
            rooms=Booking._rooms,
            place=Booking._place,
        )
       
        with open(
            f"scraped_data\\{Booking._place}-booking.csv",
            "a",
            newline="",
            encoding="utf-8",
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=collection_list[0].keys())
        
            for _, row in enumerate(collection_list):
                writer.writerow(row)

    def reset_to_home(self):
        self.get(const.BASE_URL)
        self.close_popup()
