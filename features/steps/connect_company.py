from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Connect the company button')
def click_connect_company(context):
    context.app.connect_company_page.click_connect_company()



@when('Switch to the new tab')
def switch_to_new_tab(context):
    context.app.connect_company_page.switch_to_new_window()



@when('Verify the right tab opens')
def verify_right_tab_opens(context):
    context.app.connect_company_page.verify_right_tab_opens()
