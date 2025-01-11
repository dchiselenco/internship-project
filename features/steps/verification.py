from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @then('Verify that URL of window contains verification')
# def verify_url_contains_verification(context):
#     context.app.verification_page.verify_url_contains_verification()


@then('Verify “upload image” and “Next step” buttons are available')
def upload_image_and_next_step_button_verification(context):
    context.app.verification_page.upload_image_and_next_step_button_verification()
