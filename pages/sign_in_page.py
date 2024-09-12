from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SigninPage(BasePage):
    BACK_TXT = (By.XPATH, '//div[text()="Back"]')
    CONTINUE_BTN = (By.XPATH, "//a[text()='Continue']")
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[type="email"]')
    EMAIL_TEXT = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    PASSWORD_TEXT = (By.CSS_SELECTOR, 'input[type="password"]')
    SETTINGS_OPTION = (By.XPATH, "//div[text()='Settings']")
    SUBSCRIPTION_AND_PAYMENT = (By.CSS_SELECTOR, 'a.page-setting-block[href="/subscription"]')
    SUBSCRIPTION_AND_PAYMENT_TXT = (By.XPATH, "//div[text()='Subscription & payments']")
    UPGRADE_PLAN_BTN = (By.XPATH, '//div[text()=\'Upgrade plan\']')
    USER_NAME = (By.XPATH, '//div[@wized="userName" and @class="name_text_account" and @w-el-text="Name Surname" and '
                           'text()="Dany C"]')


    EMAIL = "dchiselenco@gmail.com"
    PASSWORD = "Qwaszx!234"

    def click_continue(self, context):
        self.wait_until_clickable(*self.CONTINUE_BTN)

    def click_settings_option(self, context):
        self.wait_until_clickable(*self.SETTINGS_OPTION)

    def click_subscription_and_payments(self, context):
        self.wait_until_clickable(*self.SUBSCRIPTION_AND_PAYMENT)

    def correct_username_is_visible_in_email_field(self, expected_email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.EMAIL_TEXT)
        )
        entered_email = email_field.get_attribute('value')
        assert entered_email == expected_email, f"Expected email '{expected_email}' but got '{entered_email}'"

    def correct_password_is_visible_in_password_field(self, expected_password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PASSWORD_TEXT)
        )
        entered_password = password_field.get_attribute('value')
        assert entered_password == expected_password, f"Expected password '{expected_password}' but got '{entered_password}'"



    def input_credentials(self):
        email_field = self.driver.find_element(*self.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(self.EMAIL)

        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(self.PASSWORD)


    def verify_subscription_and_payments_text(self):
        self.verify_text('Subscription & payments', *self.SUBSCRIPTION_AND_PAYMENT_TXT)

    def verify_back_button_available(self):
        self.verify_text('Back', *self.BACK_TXT)

    def verify_upgrade_plan_available(self):
        self.verify_text('Upgrade plan', *self.UPGRADE_PLAN_BTN)

    def verify_user_name_is_visible(self):
        self.verify_text('Dany C', *self.USER_NAME)
