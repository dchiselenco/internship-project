from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class UserGuidePage(BasePage):
    TITLES_LOCATOR = (By.XPATH, "//div[text()='Full overview of Reelly platform']")

    def verify_url_contains_user_guide(self, expected_partial_url='user-guide'):
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f'URL does not contain {expected_partial_url}')

    def verify_all_videos_contains_title(self):
        titles = self.driver.find_elements(*self.TITLES_LOCATOR)
        assert all(title.text.strip() != "" for title in titles), "Not all lesson videos have titles"
