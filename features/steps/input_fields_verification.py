from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify correct username is visible in email field')
def correct_username_is_visible_in_email_field(context):
    expected_email = context.email
    context.app.sign_in_page.correct_username_is_visible_in_email_field(expected_email)


@then('Verify correct password is present in password field')
def correct_password_is_visible_in_password_field(context):
    expected_password = context.password
    context.app.sign_in_page.correct_password_is_visible_in_password_field(expected_password)


