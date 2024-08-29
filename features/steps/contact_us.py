from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify that URL of window contains {partial_url}')
def verify_url_contains_contact_us(context, partial_url):
    context.app.contact_us_page.verify_url_contains_contact_us(partial_url)


@then('Verify there are at least {number} social media icons')
def verify_number_of_social_media_icons(context, number):
    context.app.contact_us_page.verify_number_of_social_media_icons(number)


@then('Verify “Connect the company” button is available and clickable')
def connect_the_company_button_verification(context):
    context.app.contact_us_page.connect_the_company_button_verification()
