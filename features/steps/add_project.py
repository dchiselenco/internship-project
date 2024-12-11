from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Add a project')
def click_search_icon(context):
    context.app.settings_page.click_add_project()


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.add_project_page.verify_right_page_opens()


@then('Add test information to the input fields')
def input_project_info(context):
    context.app.add_project_page.input_project_info()


@then('Verify the right information is present in the input field')
def input_field_verification(context):
    # expected_email = "dchiselenco@gmail.com"
    # expected_name = "Daniela C"
    # expected_company = "test2"
    context.app.add_project_page.input_field_verification()


@then('Verify Send an Application button is available and clickable')
def send_application_button_verification(context):
    context.app.add_project_page.send_an_application_button_verification()
