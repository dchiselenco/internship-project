from behave import given, when, then


@then('Go back to Settings page')
def back_to_settings_page(context):
    context.app.support_page.back_to_settings_page()


@then('Switch to Support windows')
def switch_to_support_window(context):
    context.app.support_page.switch_to_support_window()
