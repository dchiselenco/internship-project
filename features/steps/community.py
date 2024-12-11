from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Verify the right Community page open')
def verify_community_page_opens(context):
    context.app.community_page.verify_community_page_opens()


@when('Verify “Contact support” button is available and clickable')
def contact_support_button_verification(context):
    context.app.community_page.contact_support_button_verification()
