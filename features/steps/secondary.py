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


@then('Filter the products by “Want to buy”')
def want_to_buy_listing_type(context):
    context.app.secondary_page.want_to_buy_listing_type()

@then('Click on "Apply Filter" button')
def hover_and_click_apply_filter(context):
    context.app.secondary_page.hover_and_click_apply_filter()

@then('Verify all cards have “for sale” tag')
def all_cards_have_for_sale_tag(context):
    context.app.secondary_page.all_cards_have_for_sale_tag()

@then('Verify all cards have “Want to buy” tag')
def all_cards_have_for_sale_tag(context):
    context.app.secondary_page.all_cards_have_want_to_buy_tag()

@then('Filter the products by price range from 1200000 to 2000000 AED')
def filter_price(context):
    context.app.secondary_page.filter_price()

@then('Verify the price in all cards is inside the range (1200000 - 2000000)')
def price_in_to_inside_range(context):
    context.app.secondary_page.price_in_to_inside_range()

