from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify “upload image” and “Next step” buttons are available')
def upload_image_and_next_step_button_verification(context):
    context.app.verification_page.upload_image_and_next_step_button_verification()
