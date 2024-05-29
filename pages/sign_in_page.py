from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SigninPage(Page):
    BACK_TXT = (By.XPATH, '//div[text()="Back"]')
    CONTINUE_BTN = (By.XPATH, "//a[text()='Continue']")
    SETTINGS_OPTION = (By.XPATH, "//div[text()='Settings']")
    SUBSCRIPTION_AND_PAYMENT = (By.CSS_SELECTOR, 'a.page-setting-block[href="/subscription"]')
    SUBSCRIPTION_AND_PAYMENT_TXT = (By.XPATH, "//div[text()='Subscription & payments']")
    UPGRADE_PLAN_BTN =(By.XPATH, "//div[text()='Upgrade plan']")


    def input_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        email_field.send_keys("dchiselenco@gmail.com")



    def input_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        password_field.send_keys("Qwaszx!234")


    def click_continue(self, context):
        self.wait_until_clickable(*self.CONTINUE_BTN)


    def click_settings_option(self, context):
        self.wait_until_clickable(*self.SETTINGS_OPTION)

    def click_subscription_and_payments(self, context):
        self.wait_until_clickable(*self.SUBSCRIPTION_AND_PAYMENT)


    def verify_subscription_and_payments_text(self):
        self.verify_text('Subscription & payments', *self.SUBSCRIPTION_AND_PAYMENT_TXT)


    def verify_back_button_available(self):
        self.verify_text('Back', *self.BACK_TXT)



    def verify_upgrade_plan_available(self):
        self.verify_text('Upgrade plan', *self.UPGRADE_PLAN_BTN)