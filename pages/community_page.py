from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CommunityPage(BasePage):
    CONTACT_SUPPORT_BUTTON = CONNECT_BUTTON = (By.XPATH, "//*[text()='Contact support']")

    def verify_community_page_opens(self, expected_partial_url='community'):
        self.wait.until(EC.url_contains(expected_partial_url), message=f'URL does not contain {expected_partial_url}')

    def contact_support_button_verification(self):
        contact_support_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.CONTACT_SUPPORT_BUTTON)
        )
        is_button_clickable = contact_support_button.is_enabled() and contact_support_button.is_displayed()
        print(f'The "Send an application" button is available and clickable: {is_button_clickable}')
