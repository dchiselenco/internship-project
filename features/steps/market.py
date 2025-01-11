from behave import given, when, then


@when('Click on Market button')
def click_market_btn(context):
    context.app.market_page.click_market_btn()


@then('Verify Market page opens')
def verify_market_tab_opens(context):
    context.app.market_page.verify_market_tab_opens()


@then('Go to the final Market page using the pagination button')
def go_to_final_page(context):
    context.app.market_page.go_to_final_page()


@then('Go back to the first Market page using the pagination button')
def go_to_first_page(context):
    context.app.market_page.go_to_first_page()


@then('Click on Developers filter at the top of the page')
def click_developer_filter(context):
    context.app.market_page.click_developer_filter()


@then('Verify all cards has the license tag')
def verify_license_tag(context):
    context.app.market_page.verify_license_tag()
