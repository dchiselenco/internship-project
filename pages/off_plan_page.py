from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class OffPlanPage(BasePage):
    # Locators
    LOBBY_LOCATOR = (By.XPATH, '//div[text()="Lobby"]')
    OFF_PLAN_TAB_LOCATOR = (By.XPATH,
                            "//a[contains(@class, 'menu-text-link-leaderboard') and contains(@class, 'w--current') and text()='Off-plan']")
    OFF_PLAN_BUTTON = (By.XPATH, '//div[text()="Off-plan"]')
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, '[wized="nextPageProperties"]')
    IMAGE_LOCATOR = (By.CSS_SELECTOR, '[wized="projectImage"]')
    NAME_OBJECT_LOCATOR = (By.CSS_SELECTOR, '[class="name_object_block"]')
    TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')
    CURRENT_PAGE = (By.CSS_SELECTOR, '[wized="currentPageProperties"]')
    PREVIOUS_PAGE_BUTTON = (By.XPATH, '//div[contains(@wized, "previousPage")]')
    FILTERS_HEADER = (By.CSS_SELECTOR, '.filter-text')
    APPLY_FILTERS_BTN = (By.CSS_SELECTOR, "a.button-filter.w-button")
    UNIT_PRICE = (By.CSS_SELECTOR, '[wized="unitPriceMLS"]')
    SALE_STATUS_SELECTION = (By.CSS_SELECTOR, 'select[id="Location-2"]')

    def click_off_plan_btn(self):
        self.wait_until_clickable(*self.OFF_PLAN_BUTTON)
        sleep(6)

    def verify_off_plan_tab_opens(self):
        off_plan_element = self.find_element(*self.OFF_PLAN_TAB_LOCATOR)
        is_active = "w--current" in off_plan_element.get_attribute("class")
        if is_active:
            print("The Off-plan page is active.")
        else:
            print("The Off-plan page is not active.")

    def go_to_final_page(self):

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        total_number_of_pages = int(self.find_element(*self.TOTAL_PAGES).text)
        print(f'Total number of pages: {total_number_of_pages}')

        page = 1
        while page < total_number_of_pages:
            print(f'Navigating to page {page + 1}')
            self.click(*self.NEXT_PAGE_BUTTON)
            page += 1
            sleep(3)

        print("Reached the last page.")

    def go_to_first_page(self):

        current_page = int(self.find_element(*self.CURRENT_PAGE).text)
        while current_page > 1:
            print(f"Currently on page {current_page}. Go to the previous page.")
            self.click(*self.PREVIOUS_PAGE_BUTTON)
            sleep(3)
            current_page = int(self.find_element(*self.CURRENT_PAGE).text)

        print("Reached the first page.")

    def click_filter_headers(self):

        filters_button = self.driver.find_elements(*self.FILTERS_HEADER)
        filters_button = filters_button[1]
        filters_button.click()

    def click_apply_filter_button(self):
        apply_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.APPLY_FILTERS_BTN)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(apply_btn).perform()
        apply_btn.click()
        sleep(2)

    def price_in_range(self):

        sleep(3)
        total_number_of_page = self.find_element(*self.TOTAL_PAGES).text
        print(f'Total number of pages: {total_number_of_page}')

        page = 1

        while page <= int(total_number_of_page):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            sleep(3)
            unit_price_elements = self.find_elements(*self.UNIT_PRICE)
            all_prices_within_range = True

            for unit_price_element in unit_price_elements:
                unit_price_text = unit_price_element.text
                unit_price_cleaned = unit_price_text.replace('AED', '').replace(',', '').strip()
                unit_price_value = int(unit_price_cleaned)

                if not (1200000 <= unit_price_value <= 2000000):
                    all_prices_within_range = False
                    break

            if all_prices_within_range:
                print(f'All cards are inside the range (1200000 - 2000000) on page {page}.')
            else:
                print(f'Some prices are out of range on page {page}.')

            if page < int(total_number_of_page):
                self.click(*self.NEXT_PAGE_BUTTON)
                page += 1
                print(f'Page number: {page}')
            else:
                break

        print("Price verification completed.")

    def contains_title_and_picture_visible(self):

        name_objects = self.find_elements(*self.NAME_OBJECT_LOCATOR)
        displayed_names = []

        for name in name_objects:
            if name.is_displayed():
                displayed_names.append(name)
        name_count = len(displayed_names)

        image_elements = self.driver.find_elements(*self.IMAGE_LOCATOR)
        displayed_images = []

        for image in image_elements:
            if image.is_displayed():
                displayed_images.append(image)
        image_count = len(displayed_images)

        if name_count == image_count:
            print(f"The number of displayed names {name_count} matches the number of displayed images {image_count}.")
        else:
            print(
                f"Mismatch: The number of displayed names {name_count} does not match the number of displayed images {image_count}.")

    def click_first_product(self):
        first_product = self.find_element(*self.IMAGE_LOCATOR)
        first_product.click()

    def select_sale_status_out_of_stock(self):
        sale_status_dd = self.find_element(*self.SALE_STATUS_SELECTION)
        select = Select(sale_status_dd)
        select.select_by_value('Out of stock')
        sleep(10)

    def all_cards_have_out_of_stock_tag(self):
        LISTING_PROJECTS = (By.CSS_SELECTOR, '[wized="projectImage"]')
        TAG_PROJECT = (By.CSS_SELECTOR, '[wized="projectStatus"]')
        NEXT_BUTTON = (By.CSS_SELECTOR, '[wized="nextPageProperties"]')
        TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')
        TOTAL_PROJECTS = (By.CSS_SELECTOR, '[wized="totalPropertyCounter"]')

        actual_listing = 0
        page = 0

        wait = WebDriverWait(self.driver, 10)
        total_number_of_page_element = wait.until(
            EC.visibility_of_element_located(TOTAL_PAGES)
        )

        total_number_of_page = total_number_of_page_element.text
        print(f"Total number of pages: {total_number_of_page}")

        counter_projects = int(self.find_element(*TOTAL_PROJECTS).text)
        print(f"Total Projects after applying Out of stock filter: {counter_projects}")

        while page < int(total_number_of_page):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            sleep(3)
            listing_projects = self.find_elements(*LISTING_PROJECTS)

            for listing in listing_projects:
                listing_value = listing.find_element(*TAG_PROJECT).text
                if listing_value == 'Out of stock':
                    actual_listing += 1
                else:
                    print(f"Unexpected tag found: {listing_value}")

            self.click(*NEXT_BUTTON)
            page += 1
            print(f'Page number: {page}')
            print(
                f'Total number of listings with status "Out of Stock" in the end of page {page} is : {actual_listing}')  # Print the current count of "Out of Stock" listings
        assert actual_listing == counter_projects, (
            f"Mismatch found: Expected {counter_projects}, but found {actual_listing}"
        )
        print(f"Assertion passed: Found {actual_listing} projects with the 'Out of Stock' tag, "
              f"matching the expected total of {counter_projects}.")
