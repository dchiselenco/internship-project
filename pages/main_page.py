from selenium.webdriver.common.by import By
from pages.base_page import Page


from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class MainPage(Page):
    SIGN_IN = (By.CSS_SELECTOR, 'div[wized="signinButtonSignup"].sing-in-text')



    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-up')


    def click_sign_in(self,context):
        self.wait_until_clickable(*self.SIGN_IN)
