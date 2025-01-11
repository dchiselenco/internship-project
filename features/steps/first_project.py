from behave import given, when, then


@then('Verify the one of the three options of visualization are {tab_1}, {tab_2}, {tab_3}')
def verify_tabs(context, tab_1, tab_2, tab_3):
    context.app.first_project_page.verify_tabs(tab_1, tab_2, tab_3)
    context.tab_1 = tab_1
    context.tab_2 = tab_2
    context.tab_3 = tab_3


@then('Verify the visualization options are clickable')
def visualization_tabs_clickable(context):
    context.app.first_project_page.visualization_tabs_clickable(context.tab_1, context.tab_2, context.tab_3)
