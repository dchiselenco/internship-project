from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Secondary button')
def click_secondary_btn(context):
    context.app.secondary_page.click_secondary_btn()


@then('Go to the final page using the pagination button')
def go_to_final_page(context):
    context.app.secondary_page.go_to_final_page()


@then('Go back to the first page using the pagination button')
def go_to_first_page(context):
    context.app.secondary_page.go_to_first_page()


@then('Click on Filters')
def click_filters_btn(context):
    context.app.secondary_page.click_filters_btn()

@then('Filter the products by "Want to sell"')
def want_to_sell_listing_type(context):
    context.app.secondary_page.want_to_sell_listing_type()

@then('Click on "Apply Filter" button')
def hover_and_click_apply_filter(context):
    context.app.secondary_page.hover_and_click_apply_filter()

@then('Verify all cards have “for sale” tag')
def for_sale_tags_on_all_cards(context):
    context.app.secondary_page.for_sale_tags_on_all_cards()
