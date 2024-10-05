from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Secondary button')
def click_secondary_btn(context):
    context.app.secondary_page.click_secondary_btn()


@then('Go to the final page using the pagination button')
def go_to_final_page(context):
    context.app.secondary_page.go_to_final_page()


@then('Go back to the first page using the pagination button')
def go_to_final_page(context):
    context.app.secondary_page.go_to_first_page()