from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ChangePassword(BasePage):
    CHANGE_PASSWORD_BTN = (By.XPATH, "//a[@class='submit-button-2 w-button' and text()='Change password']")
    ENTER_NEW_PASSWORD_INPUT = (By.ID, "Enter-new-password")
    REPEAT_PASSWORD_INPUT = (By.ID, "Repeat-password")


    def input_change_password_info(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.ENTER_NEW_PASSWORD_INPUT)
        )
        self.input_text('Opklnm!098', *self.ENTER_NEW_PASSWORD_INPUT)
        self.input_text('Opklnm!098', *self.REPEAT_PASSWORD_INPUT)

    def verify_change_password_button_available(self):
        self.verify_text('Change password', *self.CHANGE_PASSWORD_BTN)