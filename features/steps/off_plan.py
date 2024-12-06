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

@then('Click on Filters from header')
def click_filter_headers(context):
    context.app.off_plan_page.click_filter_headers()

@then('Click on "Apply Filter" button from header')
def click_apply_filter_button(context):
    context.app.off_plan_page.click_apply_filter_button()

@then('Verify the price in all cards from off-plan pages are inside the range (1200000 - 2000000)')
def price_in_range(context):
    context.app.off_plan_page.price_in_range()

@then('Verify each product on this page contains a title and picture visible')
def contains_title_and_picture_visible(context):
    context.app.off_plan_page.contains_title_and_picture_visible()

@then('Click on the first product')
def click_first_product(context):
    context.app.off_plan_page.click_first_product()

@then('Filter by sale status of “Out of Stocks”')
def select_sale_status_out_of_stock(context):
    context.app.off_plan_page.select_sale_status_out_of_stock()

@then('Verify each product contains the Out of Stocks tag')
def all_cards_have_out_of_stocks_tag(context):
    context.app.off_plan_page.all_cards_have_out_of_stocks_tag()



