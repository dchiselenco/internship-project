from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class VerificationPage(BasePage):

    NEXT_STEP = (By.XPATH, '//div[text()="Next step ->"]')
    UPLOAD_IMAGE = (By.CSS_SELECTOR, "label[for='input_file']")
    ELEMENT_UPLOADED = (By.CLASS_NAME, "verify-step-block")

    def verify_url_contains_verification(self, expected_partial_url='Verification'):
        self.wait.until(EC.url_contains(expected_partial_url),
                        message=f'URL does not contain {expected_partial_url}')
    sleep(6)
    def upload_image_and_next_step_button_verification(self):


        upload_image_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.UPLOAD_IMAGE)
        )
        is_upload_button_displayed = upload_image_button.is_displayed()
        print(f'The "Upload Image" button is displayed: {is_upload_button_displayed}')

        next_step_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.NEXT_STEP)  # Ensures the element is present
        )
        is_next_button_displayed = next_step_button.is_displayed()
        print(f'The "Next Step" button is displayed: {is_next_button_displayed}')