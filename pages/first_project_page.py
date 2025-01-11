from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FirstProject(BasePage):

    OPTION = (By.CSS_SELECTOR, '.tab div')

    def verify_tabs(self, tab_1, tab_2, tab_3):
        elements = self.find_elements(*self.OPTION)
        options = [element.text.strip().lower() for element in elements]
        # print(options)

        expected_options = {tab_1, tab_2, tab_3}
        assert expected_options.intersection(options), "None of the expected options are present!"

    def visualization_tabs_clickable(self,tab_1, tab_2, tab_3):
        elements = self.find_elements(*self.OPTION)
        expected_options = {tab_1, tab_2, tab_3}

        for element in elements:
            text = element.text.strip().lower()
            if text in expected_options:
                element.click()
                # print(element.text)