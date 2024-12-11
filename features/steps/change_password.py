from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Add some test password to the input fields')
def input_change_password_info(context):
    context.app.change_password_page.input_change_password_info()


@then('Verify the “Change password” button is available')
def verify_change_password_button_available(context):
    context.app.change_password_page.verify_change_password_button_available()
