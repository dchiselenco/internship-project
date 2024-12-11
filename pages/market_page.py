from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class MarketPage(BasePage):
    CURRENT_PAGE = (By.CSS_SELECTOR, '[wized="currentPageMarket"]')
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, '[wized="nextPageMarket"]')
    PREVIOUS_PAGE_BUTTON = (By.XPATH, '//div[contains(@wized, "previousPageMarket")]')
    TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageMarket"]')
    MARKET_BUTTON = (By.XPATH, '//div[text()="Market"]')

    def click_market_btn(self):
        self.wait_until_clickable(*self.MARKET_BUTTON)
        sleep(6)

    def verify_market_tab_opens(self, expected_partial_url='market-companies'):
        self.wait.until(EC.url_contains(expected_partial_url), message=f'URL does not contain {expected_partial_url}')

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
