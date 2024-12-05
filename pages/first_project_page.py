from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class FirstProject(BasePage):
    ARCHITECTURE_LOCATOR = (By.XPATH, '//div[text()="Architecture"]')
    INTERIOR_LOCATOR = (By.XPATH, "//div[text()='Interior']")

    def visualization_options(self):
        architecture_option = self.driver.find_element(*self.ARCHITECTURE_LOCATOR).text.strip()
        interior_option = self.wait.until(
        EC.visibility_of_element_located(self.INTERIOR_LOCATOR)).text.strip()

        actual_options = [architecture_option, interior_option]
    # Expected visualization options
        expected_options = ["Architecture", "Interior"]

    # Verify the options are as expected
        assert actual_options == expected_options, (
            f"Expected options {expected_options}, but found {actual_options}"
        )

    def visualization_options_clickable(self):
        architecture_option = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.ARCHITECTURE_LOCATOR)
        )
        is_button_clickable = architecture_option.is_enabled()
        print(f'The "Architecture" option is clickable: {is_button_clickable}')
    # lobby_option = WebDriverWait(self.driver, 3).until(
    #     EC.presence_of_element_located(self.LOBBY_LOCATOR)
    # )
    # is_button_clickable = lobby_option.is_enabled()
    # print(f'The "Lobby" option is clickable: {is_button_clickable}')
        interior_option = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INTERIOR_LOCATOR)
        )
        is_button_clickable = interior_option.is_enabled()
        print(f'The "Interior" option is clickable: {is_button_clickable}')
