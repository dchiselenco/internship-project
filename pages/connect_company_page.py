from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ConnectCompanyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_connect_company(self):
        connect_button = self.find_element(By.XPATH, "//*[text()='Connect the company']")
        connect_button.click()

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('ALL windows:', self.driver.window_handles)
        print('Switching to... ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def verify_right_tab_opens(self):
        actual_text = self.find_element(By.XPATH, "//div[text()='Get details about Reelly corporate offer']").text
        assert "Get details about Reelly corporate offer" in actual_text, f'Error! Text "Get details about Reelly corporate offer" not in {actual_text}'
