from pages.add_project_page import AddProject
from pages.base_page import BasePage
from pages.community_page import CommunityPage
from pages.connect_company_page import ConnectCompanyPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.sign_in_page import SigninPage


class Application:
    def __init__(self, driver):
        self.add_project_page = AddProject(driver)
        self.base_page = BasePage(driver)
        self.connect_company_page = ConnectCompanyPage(driver)
        self.community_page = CommunityPage(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_in_page = SigninPage(driver)
