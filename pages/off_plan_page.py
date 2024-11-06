from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep



class OffPlanPage(BasePage):
    # Locators
    OFF_PLAN_TAB_LOCATOR = (By.XPATH, "//a[contains(@class, 'menu-text-link-leaderboard') and contains(@class, 'w--current') and text()='Off-plan']")
    OFF_PLAN_BUTTON = (By.XPATH, '//div[text()="Off-plan"]')
    NEXT_BUTTON = (By.CSS_SELECTOR, '[wized="nextPageProperties"]')
    TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')
    CURRENT_PAGE = (By.CSS_SELECTOR, '[wized="currentPageProperties"]')
    PREVIOUS_BUTTON = (By.XPATH, '//div[contains(@wized, "previousPage")]')

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
            self.click(*self.NEXT_BUTTON)

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
            self.click(*self.PREVIOUS_BUTTON)

            # Wait for the page to load (adjust as needed)
            sleep(3)

            # Update the current page number
            current_page = int(self.find_element(*self.CURRENT_PAGE).text)

        print("Reached the first page.")