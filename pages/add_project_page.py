from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class AddProject(BasePage):

    INPUT_PROJECT_EMAIL = (By.ID, 'Email-add-project')
    INPUT_PROJECT_PHONE = (By.ID, 'Phone')
    INPUT_PROJECT_NAME = (By.ID, 'Name-project')
    INPUT_PROJECT_COUNTRY = (By.ID, 'Country')
    INPUT_PROJECT_FIELD_NAME = (By.ID, 'Your-name')
    INPUT_PROJECT_FIELD_COMPANY = (By.ID, 'Your-company-name')
    INPUT_PROJECT_FIELD_ROLE = (By.ID, 'Role')
    INPUT_PROJECT_AGE = (By.ID, 'Age-of-the-company')
    SEND_AN_APPLICATION_BUTTON = (By.XPATH, "//input[@type='submit' and @value='Send an application']")




    def verify_right_page_opens(self, expected_partial_url='add-a-project'):
        self.wait.until(EC.url_contains(expected_partial_url), message=f'URL does not contain {expected_partial_url}')

    def input_project_info(self):
        WebDriverWait(self.driver, 3).until(
        EC.presence_of_element_located(self.INPUT_PROJECT_FIELD_NAME)
        )
        self.input_text('Daniela C', *self.INPUT_PROJECT_FIELD_NAME)
        self.input_text('test2', *self.INPUT_PROJECT_FIELD_COMPANY)
        self.input_text('Broker', *self.INPUT_PROJECT_FIELD_ROLE)
        self.input_text('2010', *self.INPUT_PROJECT_AGE)
        self.input_text('USA', *self.INPUT_PROJECT_COUNTRY)
        self.input_text('New Project', *self.INPUT_PROJECT_NAME)
        self.input_text('88888', *self.INPUT_PROJECT_PHONE)
        self.input_text('dchiselenco@gmail.com', *self.INPUT_PROJECT_EMAIL)


    def input_field_verification(self):
        element_email = WebDriverWait(self.driver, 3).until(
        EC.presence_of_element_located(self.INPUT_PROJECT_EMAIL)
        )
        text_message_email = element_email.get_attribute('value')
        print(f'The chosen email is - "{text_message_email}"')

        element_name = WebDriverWait(self.driver, 3).until(
        EC.presence_of_element_located(self.INPUT_PROJECT_FIELD_NAME)
        )
        text_message_name = element_name.get_attribute('value')
        print(f'The chosen name is - "{text_message_name}"')

        element_company = WebDriverWait(self.driver, 3).until(
        EC.presence_of_element_located(self.INPUT_PROJECT_FIELD_COMPANY)
        )
        text_message_company = element_company.get_attribute('value')
        print(f'The chosen company name is - "{text_message_company}"')

    def send_an_application_button_verification(self):
        send_application_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.SEND_AN_APPLICATION_BUTTON)
        )
        is_button_clickable = send_application_button.is_enabled() and send_application_button.is_displayed()
        print(f'The "Send an application" button is available and clickable: {is_button_clickable}')