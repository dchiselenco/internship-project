from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on menu')
def click_on_main_menu(context):
    context.app.main_page.click_on_main_menu()


@when('Change the language')
def change_language(context):
    context.app.main_page.change_language()


@then('Verify the language has changed')
def verify_language(context):
    context.app.main_page.verify_language()
