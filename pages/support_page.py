from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SupportPage(BasePage):

    def switch_to_support_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('ALL windows:', self.driver.window_handles)
        print('Switching to... ', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def back_to_settings_page(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])
