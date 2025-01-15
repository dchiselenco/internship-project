from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class MarketPage(BasePage):
    ADD_COMPANY_BUTTON = (By.XPATH, '//div[text()="Add company"]')
    CURRENT_PAGE = (By.CSS_SELECTOR, '[wized="currentPageMarket"]')
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, '[wized="nextPageMarket"]')
    PREVIOUS_PAGE_BUTTON = (By.XPATH, '//div[contains(@wized, "previousPageMarket")]')
    PUBLISH_MY_COMPANY_BUTTON = (By.XPATH, '//a[contains(text(), "Publish my company")]')
    TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageMarket"]')
    MARKET_BUTTON = (By.XPATH, '//div[text()="Market"]')
    DEVELOPERS_BUTTON = (By.XPATH, '//div[text()="Developers"]')

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

    def click_developer_filter(self):
        self.wait_until_clickable(*self.DEVELOPERS_BUTTON)

    def verify_license_tag(self):

        LISTING_CARDS = (By.CSS_SELECTOR, '[wized="marketPageLinkCard"]')
        LICENSE_TEXT = (By.XPATH, "//div[@class='license-txt' and text()='License']")
        # LICENSE_TEXT = (By.CSS_SELECTOR, "div.license-txt")
        NEXT_BUTTON = (By.CSS_SELECTOR, '[wized="nextPageMarket"]')
        TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageMarket"]')
        DEVELOPERS_COUNTER = (By.CSS_SELECTOR, '[wized="totalMarketPageCounter"]')


        sleep(6)

        counter_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DEVELOPERS_COUNTER)
        ).text
        int_counter = int(counter_number)
        print(f'Total cards listed in developer page: {int_counter}')
        sum = 0
        page = 0

        # Get the total number of pagination
        total_number_of_page = self.find_element(*TOTAL_PAGES).text
        print(f'Total number of pages: {total_number_of_page}')

        while page < int(total_number_of_page):
            # Scroll to the bottom of the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            sleep(3)
            # listing_cards = self.find_elements(*LISTING_CARDS)
            # for card in listing_cards:  # ITERATE EACH card
            #     license_tag = card.find_element(*LICENSE_TEXT).text  # Find license tag in each card
            #     if license_tag == 'License':
            #         actual_listing += 1
            #     else:
            #         print(f"Unexpected tag found: {license_tag}")

            license_tags = self.find_elements(*LICENSE_TEXT)
            license_tags_count = len(license_tags)
            sum += int(license_tags_count)

            # CLICK NEXT BUTTON
            self.click(*NEXT_BUTTON)
            page += 1
            print(
                f'After page number {page} total of cards that have “License” tag is: {license_tags_count} and sum of the pages is: {sum}')
        # Final verification
        assert sum == int_counter, (
            f"Expected {int_counter} cards with the 'License' tag, but found {sum}."
        )
        print("All cards have the correct 'License' tag.")

    def click_add_company(self):
        self.wait_until_clickable(*self.ADD_COMPANY_BUTTON)

    def verify_add_company_tab_opens(self, expected_partial_url='presentation-for-the-agency'):
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f'URL does not contain {expected_partial_url}')

    sleep(10)
    def verify_publish_my_company_available(self):
        publish_my_company_elements = self.driver.find_elements(*self.PUBLISH_MY_COMPANY_BUTTON)
        visible_elements = [element for element in publish_my_company_elements if element.is_displayed()]
        print(f"Visible elements count: {len(visible_elements)}")


