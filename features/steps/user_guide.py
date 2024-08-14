from behave import given, when, then


@then('Verify that URL  contains {partial_url}')
def verify_url_contains_user_guide(context, partial_url):
    context.app.user_guide_page.verify_url_contains_user_guide(partial_url)


@then('Verify all lesson videos contain titles')
def verify_all_videos_contains_title(context):
    context.app.user_guide_page.verify_all_videos_contains_title()
