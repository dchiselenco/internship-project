import time

from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import sleep

class SecondaryPage(BasePage):
    NEXT_BTN = FORWARD = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")
    BACK_BUTTON = (By.XPATH, '//div[contains(@wized, "previousPage")]')
    SECONDARY_BTN = (By.XPATH, '//div[text()="Secondary"]')
    # CURRENT_PAGE = (By.CSS_SELECTOR, "div.page-count[wized='currentPageProperties'][w-el-text='1']")
    # TOTAL_PAGE = (By.CSS_SELECTOR, "div.page-count[wized='totalPageProperties'][w-el-text='1']")

    def click_secondary_btn(self):
        self.wait_until_clickable(*self.SECONDARY_BTN)

    def go_to_final_page(self):

        while True:
            try:
                next_btn = self.wait.until(EC.element_to_be_clickable(self.NEXT_BTN))
                actions = ActionChains(self.driver)
                actions.move_to_element(next_btn)
                actions.perform()
                next_btn.click()
                self.wait.until(EC.staleness_of(next_btn))

            except:
                print("Reached the last page,  'Next' button is not anymore clickable")
                break


    def go_to_first_page(self):

        while True:
            try:
                previous_btn = self.wait.until(EC.element_to_be_clickable(self.BACK_BUTTON))
                actions = ActionChains(self.driver)
                actions.move_to_element(previous_btn)
                actions.perform()
                previous_btn.click()
                self.wait.until(EC.staleness_of(previous_btn))

            except:
                print("Reached the first page,  'Back' button is not anymore clickable")
                break



