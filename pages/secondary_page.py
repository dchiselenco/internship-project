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
    FOR_SALE_TAG = (By.XPATH, "//div[text()='For sale']")
    FILTERS_BTN = (By.CSS_SELECTOR, '.filter-text')
    LISTINGS = (By.XPATH, "//div[@wized='listingsCounterMLS' and @class='properties-counter listing']")
    LISTING_CARDS = (By.XPATH, "//div[contains(@class, 'listing-card')]")
    NEXT_BTN = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")
    SECONDARY_BTN = (By.XPATH, '//div[text()="Secondary"]')
    WANT_TO_SELL= (By.CSS_SELECTOR, "div.switcher-button.active")
    # CURRENT_PAGE = (By.CSS_SELECTOR, "div.page-count[wized='currentPageProperties'][w-el-text='1']")
    #TOTAL_PAGE = (By.CSS_SELECTOR, "div.page-count[wized='totalPageProperties'][w-el-text='1']")


    def click_secondary_btn(self):
        self.wait_until_clickable(*self.SECONDARY_BTN)

        sleep(6)

    def go_to_final_page(self):

        while True:
            try:
                # Wait for the 'Next' button to be clickable
                next_btn = self.wait.until(EC.element_to_be_clickable(self.NEXT_BTN))

                # Check if the 'Next' button is enabled and displayed
                if next_btn.is_enabled() and next_btn.is_displayed():
                    # Use ActionChains to move to the 'Next' button and click it
                    actions = ActionChains(self.driver)
                    actions.move_to_element(next_btn).perform()  # Move to the button
                    next_btn.click()  # Click the button

                    # Wait for the page to load after clicking the "Next" button
                    self.wait.until(EC.staleness_of(next_btn))
                else:
                    print("The 'Next' button is not clickable or not visible.")
                    print("Reached the last page. No more pages available.")
                    break  # Break the loop if the button is not clickable
            except TimeoutException:
                print("Timed out waiting for the 'Next' button to become clickable.")
                break  # Break if the button doesn't appear in time
            except StaleElementReferenceException:
                print("The 'Next' button became stale. Retrying...")
                continue  # Retry if the button becomes stale
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break  # Break on other exceptions

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



    def hover_and_click_apply_filter(self):
        # Wait for the Apply Filter button to be visible
        apply_filter_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.APPLY_FILTER)  # You can also use another locator if needed
        )

        # Create an instance of ActionChains
        actions = ActionChains(self.driver)

        # Hover over the Apply Filter button
        actions.move_to_element(apply_filter_button).perform()

        # Click on the Apply Filter button after hovering
        apply_filter_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FOR_SALE_TAG)  # Change to a relevant element for confirmation
        )

    def for_sale_tags_on_all_cards(self):
        # Collect total listings count from the first page
        listings_element = self.wait.until(EC.presence_of_element_located(self.LISTINGS))
        expected_total_listings_text = listings_element.text.strip()  # Assuming the text is the number
        expected_total_listings = int(expected_total_listings_text)  # Convert to integer

        # Initialize the count of 'For Sale' tags
        total_for_sale_tags = 0

        # Start navigating through pages
        while True:
            try:
                # Collect cards on the current page
                cards = self.wait.until(EC.visibility_of_all_elements_located(self.LISTING_CARDS))

                # Collect 'For Sale' tags for each listing on the current page
                for card in cards:
                    # Check for 'For Sale' tags using the defined locator
                    tags = card.find_elements(*self.FOR_SALE_TAG)
                    for tag in tags:
                        if tag.text.strip() == "For sale":  # Check if the tag's text is exactly "For sale"
                            total_for_sale_tags += 1  # Increment count if 'For Sale' tag exists

                # Print or log the counts for debugging
                print(f"Found {total_for_sale_tags} 'For Sale' tags so far.")

                # Check if there's a next page
                next_btn = self.driver.find_element(*self.NEXT_BTN)
                if next_btn.is_enabled() and next_btn.is_displayed():
                    actions = ActionChains(self.driver)
                    actions.move_to_element(next_btn).perform()
                    next_btn.click()
                    self.wait.until(EC.staleness_of(next_btn))  # Wait for page load
                else:
                    break  # Exit if no more pages

            except TimeoutException:
                print("Timed out while waiting for elements on the page.")
                break
            except StaleElementReferenceException:
                print("A stale element reference encountered. Retrying...")
                continue
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break

        # Verification step using assertions
        assert total_for_sale_tags == expected_total_listings, (
            f"Mismatch found: {total_for_sale_tags} 'For Sale' tags vs. {expected_total_listings} expected listings."
        )
        print("All listings verified successfully.")