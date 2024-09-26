from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application

#  Run Behave tests with Allure results; it will run all the test from feature folder and stored in test_results file
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/


def browser_init(context, scenario_name):
    """
    Initialize the browser driver.
    :param context: Behave context
    :param scenario_name: The name of the current scenario
    """

    # # BrowserStack credentials ##
    # bs_user = 'danielachiselenc_VWo7fR'
    # bs_key = 'LQ9LBkxj9w7egjACmDQa'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # # Define BrowserStack options  ##
    # bstack_options = {
    #     'osVersion': 'Sonoma',
    #     'browserName': 'Chrome',
    #     'os': 'OS X',
    #     'browserVersion': 'latest',
    #     'consoleLogs': 'info',
    #     'sessionName': scenario_name,
    # }
    #
    # # Set up WebDriver with BrowserStack
    # options = Options()
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(6)
    context.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    if hasattr(context, 'driver'):
        context.driver.delete_all_cookies()
        context.driver.quit()
