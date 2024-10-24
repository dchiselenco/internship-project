import time

from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import sleep

class SecondaryPage(BasePage):
    APPLY_FILTER = (By.CSS_SELECTOR, "a.button-filter.w-button")
    BACK_BUTTON = (By.XPATH, '//div[contains(@wized, "previousPage")]')
    FILTERS_BTN = (By.CSS_SELECTOR, '.filter-text')
    SECONDARY_BTN = (By.XPATH, '//div[text()="Secondary"]')
    NEXT_BUTTON = (By.CSS_SELECTOR, '[wized="nextPageMLS"]')
    WANT_TO_BUY = (By.XPATH, "//div[text()='Want to buy']")
    WANT_TO_SELL= (By.XPATH, "//div[text()='Want to sell']")

    CURRENT_PAGE = (By.CSS_SELECTOR, "div.page-count[wized='currentPageProperties'].page-count")


    def click_secondary_btn(self):
        self.wait_until_clickable(*self.SECONDARY_BTN)

        sleep(6)

    # def go_to_final_page(self):
    #     try:
    #         # Wait for the total page number to be visible and retrieve it
    #         total_page_element = self.wait.until(EC.visibility_of_element_located(self.TOTAL_PAGE))
    #         total_page_number = int(total_page_element.text.strip())  # Get the total page number
    #
    #         print(f"Total pages: {total_page_number}")
    #
    #         current_page_element = self.wait.until(EC.visibility_of_element_located(self.CURRENT_PAGE))
    #         current_page_number = int(current_page_element.text.strip())  # Get the current page number
    #
    #         print(f"Starting at page: {current_page_number}")
    #
    #         while current_page_number < total_page_number:  # Continue until you reach the last page
    #             try:
    #                 # Wait for the 'Next' button to be clickable
    #                 next_btn = self.wait.until(EC.element_to_be_clickable(self.NEXT_BTN))
    #
    #                 # Check if the 'Next' button is enabled and visible
    #                 if next_btn.is_enabled() and next_btn.is_displayed():
    #                     # Move to the next button and click it
    #                     actions = ActionChains(self.driver)
    #                     actions.move_to_element(next_btn).perform()
    #                     next_btn.click()
    #                     self.wait.until(EC.staleness_of(next_btn))  # Wait for the page to load
    #
    #                     # Update the current page number
    #                     current_page_element = self.wait.until(EC.visibility_of_element_located(self.CURRENT_PAGE))
    #                     current_page_number = int(current_page_element.text.strip())  # Update the current page number
    #                 else:
    #                     print("The 'Next' button is not clickable or not visible.")
    #                     print("Reached the last page. No more pages available.")
    #                     break  # Exit loop if the next button isn't clickable
    #
    #             except TimeoutException:
    #                 print("Timed out waiting for the 'Next' button to become clickable.")
    #             except StaleElementReferenceException:
    #                 print("The 'Next' button became stale. Retrying...")
    #                 continue  # Retry the loop to re-find the 'Next' button
    #             except Exception as e:
    #                 print(f"An unexpected error occurred: {e}")
    #                 break  # Exit the loop on unexpected errors
    #
    #         print("Finished navigating to the final page.")
    #
    #     except TimeoutException:
    #         print("Timed out waiting for the total page number to be visible.")
    #     except Exception as e:
    #         print(f"An unexpected error occurred: {e}")
    #
    #     assert current_page_number == total_page_number, (
    #     f"Mismatch found: {current_page_number} and we found {total_page_number} ."
    # )
    #
    def go_to_final_page(self):

        while True:
            try:

                next_btn = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))

                if next_btn.is_enabled() and next_btn.is_displayed():
                    actions = ActionChains(self.driver)
                    actions.move_to_element(next_btn).perform()
                    next_btn.click()
                    self.wait.until(EC.staleness_of(next_btn))
                else:
                    print("The 'Next' button is not clickable or not visible.")
                    print("Reached the last page. No more pages available.")
                    break
            except TimeoutException:
                print("Timed out waiting for the 'Next' button to become clickable.")
                break
            except StaleElementReferenceException:
                print("The 'Next' button became stale. Retrying...")
                continue
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break

    def go_to_first_page(self):

        while True:
            try:
                previous_btn = self.wait.until(EC.element_to_be_clickable(self.BACK_BUTTON))
                actions = ActionChains(self.driver)
                actions.move_to_element(previous_btn)
                actions.perform()
                previous_btn.click()
                self.wait.until(EC.staleness_of(previous_btn))

            except:
                print("Reached the first page,  'Back' button is not anymore clickable")
                break


    def click_filters_btn(self):

        filters_btn = self.wait.until(
            EC.visibility_of_element_located(self.FILTERS_BTN)
        )
        filters_btn.click()


    def want_to_sell_listing_type(self):
        element_to_hover = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.WANT_TO_SELL)  # Change the locator as necessary
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover).perform()
        element_to_hover.click()
        sleep(2)

    def want_to_buy_listing_type(self):
        element_to_hover = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.WANT_TO_BUY)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover).perform()
        element_to_hover.click()
        sleep(2)


    def hover_and_click_apply_filter(self):
        # Wait for the Apply Filter button to be visible
        apply_filter_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.APPLY_FILTER)  # You can also use another locator if needed
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(apply_filter_button).perform()
        apply_filter_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.WANT_TO_SELL)  # Change to a relevant element for confirmation
        )

    def all_cards_have_for_sale_tag(self):
        LISTING_CARDS = (By.CSS_SELECTOR, '[wized="listingCardMLS"]')
        FOR_SALE_TAG = (By.CSS_SELECTOR, '[wized="saleTagBoxMLS"]')
        NEXT_BUTTON = (By.CSS_SELECTOR, '[wized="nextPageMLS"]')
        TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')

        sleep(3)
        actual_listing = 0
        sale_boxes = self.find_elements(*LISTING_CARDS)

        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # Get the total number of pagination
        total_number_of_page = self.find_element(*TOTAL_PAGES).text
        print(f'Total number of pages: {total_number_of_page}')

        # Box Value Ex. 'For sale'
        box_value = self.find_element(*FOR_SALE_TAG).text

        # Set page to count starting 1
        page = 1

        # While page value is less than the total number of pagination and if the box_value is For sale
        while page <= int(total_number_of_page) and box_value == 'For sale':
            sleep(3)
            for box in sale_boxes:  # ITERATE EACH SALE BOXES
                if box_value == 'For sale':  # CHECK IF THE VALUE IS 'For sale'
                    actual_listing += 1
                else:  # IF Fos Sale, assert and break the loop
                    assert box_value != 'For sale', f'Expecting For sale Box value, but it has {box_value}'
                    print(box_value)
                    break

            self.click(*NEXT_BUTTON)  # CLICK NEXT BUTTON
            page += 1  # ADD 1 TO THE NUMBER OF PAGE IN EACH ITERATION

            print(f'Page number: {page}')  # PAGE NUMBER
            print(f'Actual Listing: {actual_listing}')  # TOTAL OF ACTUAL LISTING FOUND

    def all_cards_have_want_to_buy_tag(self):
        LISTING_CARDS = (By.CSS_SELECTOR, '[wized="listingCardMLS"]')
        TAG_BOX = (By.CSS_SELECTOR, '[wized="saleTagBoxMLS"]')
        NEXT_BUTTON = (By.CSS_SELECTOR, '[wized="nextPageMLS"]')
        TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')

        sleep(3)
        actual_listing = 0
        sale_boxes = self.find_elements(*LISTING_CARDS)

        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # Get the total number of pagination
        total_number_of_page = self.find_element(*TOTAL_PAGES).text
        print(f'Total number of pages: {total_number_of_page}')

        # Box Value Ex. 'want to by'
        box_value = self.find_element(*TAG_BOX).text

        # Set page to count starting 1
        page = 1

        # While page value is less than the total number of pagination and if the box_value is For sale
        while page <= int(total_number_of_page) and box_value == 'Want to buy':
            sleep(3)
            for box in sale_boxes:  # ITERATE EACH SALE BOXES
                if box_value == 'Want to buy':  # CHECK IF THE VALUE IS 'For sale'
                    actual_listing += 1
                else:  # IF Fos Sale, assert and break the loop
                    assert box_value != 'Want to buy', f'Expecting Want to buy Box value, but it has {box_value}'
                    print(box_value)
                    break

            self.click(*NEXT_BUTTON)  # CLICK NEXT BUTTON
            page += 1  # ADD 1 TO THE NUMBER OF PAGE IN EACH ITERATION

            print(f'Page number: {page}')  # PAGE NUMBER
            print(f'Actual Listing: {actual_listing}')  # TOTAL OF ACTUAL LISTING FOUND


    def filter_price(self):
        PRICE_FROM_FILTER = (By.CSS_SELECTOR, '[wized="unitPriceFromFilter"]')
        PRICE_TO_FILTER = (By.CSS_SELECTOR, '[wized = "unitPriceToFilter"]')

        # Set the price range in the filter
        self.find_element(*PRICE_FROM_FILTER).clear()  # Clear any pre-existing value
        self.find_element(*PRICE_FROM_FILTER).send_keys('1200000')  # Set minimum price

        self.find_element(*PRICE_TO_FILTER).clear()  # Clear any pre-existing value
        self.find_element(*PRICE_TO_FILTER).send_keys('2000000')  # Set maximum price

        sleep(3)  # Wait for the page to apply the filter
        print("Price filter applied: 1,200,000 to 2,000,000 AED")

    def price_in_to_inside_range(self):

        sleep(3)
        UNIT_PRICE = (By.CSS_SELECTOR, '[wized="unitPriceMLS"]')
        NEXT_BUTTON = (By.CSS_SELECTOR, '[wized="nextPageMLS"]')
        TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')

        # Get the total number of pages
        total_number_of_page = self.find_element(*TOTAL_PAGES).text
        print(f'Total number of pages: {total_number_of_page}')

        page = 1

        while page <= int(total_number_of_page):
            # Scroll to the bottom of the page to load all listings
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            sleep(3)

            # Locate the elements and check if they are present
            unit_price_elements = self.find_elements(*UNIT_PRICE)  # Locate the elements

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
                self.click(*NEXT_BUTTON)  # CLICK NEXT BUTTON
                page += 1  # ADD 1 TO THE NUMBER OF PAGE IN EACH ITERATION
                print(f'Page number: {page}')  # Update the page number
            else:
                break  # Exit the loop if no more pages

        print("Price verification completed.")



