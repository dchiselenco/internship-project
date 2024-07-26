from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Click on the Edit profile option')
def click_edit_profile_btn(context):
    context.app.settings_page.click_edit_profile_btn()


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


@then('Verify the right information is present in the company input field')
def verify_new_company(context):
    context.app.settings_page.verify_new_company()


@when('Check “Save Changes” button is available and clickable')
def click_save_btn(context):
    context.app.settings_page.click_save_btn()


@when('Check “Close” button is available and clickable')
def click_close_btn(context):
    context.app.settings_page.click_close_btn()
