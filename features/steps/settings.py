from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Click on the Edit profile option')
def click_edit_profile_btn(context):
    context.app.settings_page.click_edit_profile_btn()


@when('Click on Community option')
def click_community_btn(context):
    context.app.settings_page.click_community_btn()


@when('Enter test data into the name field: {name}')
def input_name(context, name):
    context.app.settings_page.input_name(name)


@then('Enter test data into the phone number field: {number}')
def input_number(context, number):
    context.app.settings_page.input_number(number)


@when('Enter test data into the company field: {test}')
def input_company(context, test):
    context.app.settings_page.input_company(test)


@then('Verify the right information is present in the name input field')
def verify_new_name(context):
    context.app.settings_page.verify_new_name()


@then('Verify the right information is present in the phone number input field')
def verify_new_num(context):
    context.app.settings_page.verify_new_number()


@then('Click on "Contact us" button')
def click_contact_us(context):
    context.app.settings_page.click_contact_us()


@then('Verify the right information is present in the company input field')
def verify_new_company(context):
    context.app.settings_page.verify_new_company()


@when('Check “Save Changes” button is available and clickable')
def click_save_btn(context):
    context.app.settings_page.click_save_btn()


@when('Check “Close” button is available and clickable')
def click_close_btn(context):
    context.app.settings_page.click_close_btn()


@then('Click on User Guide button')
def click_user_guide(context):
    context.app.settings_page.click_user_guide()


@then('Click on Change password option')
def click_change_password(context):
    context.app.settings_page.click_change_password()


@then('Click on Support option')
def click_on_support(context):
    context.app.settings_page.click_on_support()


@then('Click on News option')
def click_news(context):
    context.app.settings_page.click_news()
