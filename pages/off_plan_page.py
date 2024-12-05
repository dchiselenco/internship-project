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
        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # Get the total number of pages
        total_number_of_pages = int(self.find_element(*self.TOTAL_PAGES).text)
        print(f'Total number of pages: {total_number_of_pages}')

        # Start on page 1
        page = 1

        # Loop through all pages until reaching the last one
        while page < total_number_of_pages:
            print(f'Navigating to page {page + 1}')  # Print the next page number for tracking

            # Click the next button to go to the next page
            self.click(*self.NEXT_PAGE_BUTTON)

            # Increment the page count
            page += 1
            sleep(3)  # Optional: Add delay to wait for page load if needed

        print("Reached the last page.")

    def go_to_first_page(self):
        # Check if we're already on the first page
        current_page = int(self.find_element(*self.CURRENT_PAGE).text)

        # Navigate back to the first page if not already there
        while current_page > 1:
            print(f"Currently on page {current_page}. Go to the previous page.")

            # Click the "Previous" button
            self.click(*self.PREVIOUS_PAGE_BUTTON)

            # Wait for the page to load (adjust as needed)
            sleep(3)

            # Update the current page number
            current_page = int(self.find_element(*self.CURRENT_PAGE).text)

        print("Reached the first page.")

    def click_filter_headers(self):

        filters_btns = self.driver.find_elements(*self.FILTERS_HEADER)

        # Select the element at index 1 (second element in the list)
        filters_btn = filters_btns[1]

        # Click the element
        filters_btn.click()

    def click_apply_filter_button(self):
        apply_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.APPLY_FILTERS_BTN)  # Change the locator as necessary
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(apply_btn).perform()
        apply_btn.click()
        sleep(2)

    def price_in_range(self):

        sleep(3)

        # Get the total number of pages
        total_number_of_page = self.find_element(*self.TOTAL_PAGES).text
        print(f'Total number of pages: {total_number_of_page}')

        page = 1

        while page <= int(total_number_of_page):
            # Scroll to the bottom of the page to load all listings
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            sleep(3)

            # Locate the elements and check if they are present
            unit_price_elements = self.find_elements(*self.UNIT_PRICE)  # Locate the elements

            # Check if prices are within the specified range
            all_prices_within_range = True  # Flag to track if all prices are within range

            for unit_price_element in unit_price_elements:
                # Extract the text from the price element
                unit_price_text = unit_price_element.text  # e.g., 'AED 1,500,000'

                # Remove the currency and commas to clean up the price text
                unit_price_cleaned = unit_price_text.replace('AED', '').replace(',', '').strip()

                # Convert the cleaned string to an integer
                unit_price_value = int(unit_price_cleaned)

                # Check if the price is within the range
                if not (1200000 <= unit_price_value <= 2000000):
                    all_prices_within_range = False  # Set the flag to False if any price is out of range
                    break  # No need to check further prices on this page

            # Print a single summary message for the page
            if all_prices_within_range:
                print(f'All cards are inside the range (1200000 - 2000000) on page {page}.')
            else:
                print(f'Some prices are out of range on page {page}.')

            # Click the next button if there are more pages
            if page < int(total_number_of_page):
                self.click(*self.NEXT_PAGE_BUTTON)  # CLICK NEXT BUTTON
                page += 1  # ADD 1 TO THE NUMBER OF PAGE IN EACH ITERATION
                print(f'Page number: {page}')  # Update the page number
            else:
                break  # Exit the loop if no more pages

        print("Price verification completed.")

    # def select_sale_status_out_of_stocks(self):

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

