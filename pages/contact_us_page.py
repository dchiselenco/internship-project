from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ContactUsPage(BasePage):
    CONNECT_COMPANY = (By.XPATH, '//div[text()="Connect the company"]')
    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, "div.text-social")

    def verify_url_contains_contact_us(self, expected_partial_url='contact-us'):
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f'URL does not contain {expected_partial_url}')

    def connect_the_company_button_verification(self):
        connect_the_company_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.CONNECT_COMPANY)
        )
        is_button_clickable = connect_the_company_button.is_enabled() and connect_the_company_button.is_displayed()
        print(f'The "Send an application" button is available and clickable: {is_button_clickable}')

    def verify_number_of_social_media_icons(self, number):
        all_social = self.find_elements(*self.SOCIAL_MEDIA_ICONS)
        print(f'How many SOCIAL on the page?: {len(all_social)}')
        assert len(all_social) >= int(number), f'Error! Expected {number}, but got {len(all_social)}'
