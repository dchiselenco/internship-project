from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SettingsPage(BasePage):
    ADD_PROJECT = (By.XPATH, "//div[contains(text(), 'Add a project')]")
    CLOSE_BTN = (By.CSS_SELECTOR, 'a.close-button')
    COMPANY_INPUT = (By.CSS_SELECTOR, 'input#Company-name')
    COMMUNITY_BTN = (By.XPATH, "//div[@class='setting-text' and text()='Community']")
    CONTACT_US_BTN = (By.XPATH, '//div[@class="setting-text" and text()="Contact us"]')
    EDIT_BTN = (By.XPATH, "//div[text()='Edit profile']")
    NAME_INPUT = (By.CSS_SELECTOR, 'input[name="Fullname"]')
    NUMBER_INPUT = (By.CSS_SELECTOR, 'input#number')
    SAVE_BTN = (By.CSS_SELECTOR, 'div.save-changes-button')
    USER_GUIDE_BUTTON = (By.XPATH, "//div[@class='setting-text' and text()='User guide']")


    def click_edit_profile_btn(self):
        self.click(*self.EDIT_BTN)
        sleep(3)

    def click_community_btn(self):
        self.click(*self.COMMUNITY_BTN)
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

    def click_add_project(self):
        self.click(*self.ADD_PROJECT)

    def click_contact_us(self):
        self.click(*self.CONTACT_US_BTN)

    def click_user_guide(self):
        self.click(*self.USER_GUIDE_BUTTON)

    # def click_user_guide(self, context):
    #     self.wait_until_clickable(*self.USER_GUIDE_BUTTON)

    # def click_user_guide(self):
    #     # Optional: Wait for the entire page to be fully loaded
    #     WebDriverWait(self.driver, 30).until(
    #         lambda driver: driver.execute_script('return document.readyState') == 'complete'
    #     )
    #
    #     # Wait until the user guide button is visible
    #     user_guide_button = WebDriverWait(self.driver, 30).until(
    #         EC.visibility_of_element_located(self.USER_GUIDE_BUTTON)
    #     )
    #
    #     # Scroll the element into view
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", user_guide_button)
    #
    #     # Ensure it's clickable
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.USER_GUIDE_BUTTON)
    #     )
    #
    #     # Click the element
    #     user_guide_button.click()