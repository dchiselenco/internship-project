from selenium.webdriver.common.by import By
from pages.base_page import BasePage

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  # Import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    LANGUAGE = (By.CSS_SELECTOR, '[id="w-dropdown-toggle-0"]')
    MENU_LANG = (By.CSS_SELECTOR, "div[id='w-dropdown-toggle-0']")
    MAIN_MENU = (By.XPATH, "//div[contains(@class, 'menu-button-text') and contains(., 'Main menu')]")
    SIGN_IN = (By.CSS_SELECTOR, 'div[wized="signinButtonSignup"].sing-in-text')
    TEXT = (By.CSS_SELECTOR, '.h1-menu')



    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-up')

    def click_sign_in(self, context):
        self.wait_until_clickable(*self.SIGN_IN)

    def clear(self, *locator):
        self.driver.find_element(*locator).clear()


    def click_on_main_menu(self):
        self.click(*self.MAIN_MENU)

    def change_language(self):
        self.wait_until_visible(*self.MENU_LANG)
        ln = self.find_element(*self.MENU_LANG)
        actions = ActionChains(self.driver)
        actions.move_to_element(ln)
        actions.move_by_offset(0, 25)
        actions.click()
        actions.perform()


    def verify_language(self):
        self.verify_text('Главное меню', *self.TEXT)