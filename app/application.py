from pages.add_project_page import AddProject
from pages.base_page import BasePage
from pages.change_password_page import ChangePassword
from pages.community_page import CommunityPage
from pages.contact_us_page import ContactUsPage
from pages.connect_company_page import ConnectCompanyPage
from pages.first_project_page import FirstProject
from pages.main_page import MainPage
from pages.market_page import MarketPage
from pages.off_plan_page import OffPlanPage
from pages.secondary_page import SecondaryPage
from pages.settings_page import SettingsPage
from pages.sign_in_page import SigninPage
from pages.support_page import SupportPage
from pages.user_guide_page import UserGuidePage


class Application:
    def __init__(self, driver):
        self.add_project_page = AddProject(driver)
        self.base_page = BasePage(driver)
        self.change_password_page = ChangePassword(driver)
        self.community_page = CommunityPage(driver)
        self.connect_company_page = ConnectCompanyPage(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.first_project_page = FirstProject(driver)
        self.main_page = MainPage(driver)
        self.market_page = MarketPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_in_page = SigninPage(driver)
        self.support_page = SupportPage(driver)
        self.user_guide_page = UserGuidePage(driver)
