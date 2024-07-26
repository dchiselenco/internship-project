from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SettingsPage(BasePage):
    EDIT_BTN = (By.XPATH, "//div[text()='Edit profile']")
    NAME_INPUT = (By.CSS_SELECTOR, 'input[name="Fullname"]')
    NUMBER_INPUT = (By.CSS_SELECTOR, 'input#number')
    COMPANY_INPUT = (By.CSS_SELECTOR, 'input#Company-name')
    CLOSE_BTN = (By.CSS_SELECTOR, 'a.close-button')
    SAVE_BTN = (By.CSS_SELECTOR, 'div.save-changes-button')

    def click_edit_profile_btn(self):
        self.click(*self.EDIT_BTN)
        sleep(3)

    def click_save_btn(self):
        self.click(*self.SAVE_BTN)
        sleep(3)

    def click_close_btn(self):
        self.click(*self.CLOSE_BTN)
        sleep(3)

    def input_name(self, name):
        input_fname = self.find_element(*self.NAME_INPUT)
        input_fname.clear()
        # self.clear()
        self.input_text(name, *self.NAME_INPUT)
        sleep(2)

    def input_number(self, number):
        input_number = self.find_element(*self.NUMBER_INPUT)
        input_number.clear()
        # self.clear()
        self.input_text(number, *self.NUMBER_INPUT)
        sleep(2)

    def input_company(self, test):
        input_company = self.find_element(*self.COMPANY_INPUT)
        input_company.clear()
        # self.clear()
        self.input_text(test, *self.COMPANY_INPUT)
        sleep(2)

    def verify_new_name(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Fullname"]').get_attribute('value')
        expected_result = 'Dany C'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_new_number(self):
        actual_text = self.driver.find_element(*self.NUMBER_INPUT).get_attribute('value')
        expected_result = '832 829 0101'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'

    def verify_new_company(self):
        actual_text = self.driver.find_element(*self.COMPANY_INPUT).get_attribute('value')
        expected_result = 'test1'
        assert expected_result in actual_text, f'Error: Text not in {actual_text}'
