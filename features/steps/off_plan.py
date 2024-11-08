from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Off-plan button')
def click_off_plan_btn(context):
    context.app.off_plan_page.click_off_plan_btn()


@then('Verify Off-plan page opens')
def verify_off_plan_tab_opens(context):
    context.app.off_plan_page.verify_off_plan_tab_opens()


@then('Go to the  final Off-plan page using the pagination button')
def go_to_final_page(context):
    context.app.off_plan_page.go_to_final_page()


@then('Go back to the first Off-plan page using the pagination button')
def go_to_first_page(context):
    context.app.off_plan_page.go_to_first_page()

