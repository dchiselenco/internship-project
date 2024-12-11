from behave import given, when, then


@then('Verify the options of visualization are “architecture”, “interior”')
def visualization_options(context):
    context.app.first_project_page.visualization_options()


@then('Verify the visualization options are clickable')
def visualization_options_clickable(context):
    context.app.first_project_page.visualization_options_clickable()
