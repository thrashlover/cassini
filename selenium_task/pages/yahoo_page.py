import hamcrest as hc

from selenium_task.pages.base_action import BaseAction
from selenium_task.pages.locators import Locators
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Yahoo(BaseAction):
    def login(self, test_data):
        if self.check_element_is_presented(Locators.ACCEPT_COOKIES):
            self.find_element(Locators.ACCEPT_COOKIES).click()
        else:
            pass
        self.check_element_is_clickable(Locators.SIGN_IN)
        self.find_element(Locators.SIGN_IN).click()
        self.input_data(Locators.USERNAME, test_data[0])
        self.find_element(Locators.LOGIN_NEXT_BUTTON).click()
        self.input_data(Locators.PASSWORD, test_data[1])
        self.find_element(Locators.LOGIN_NEXT_BUTTON).click()

    def click_finances(self):
        self.find_element(Locators.FINANCES).click()

    def hover_market_data_and_click_calendar(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, "//*[contains(@title, 'Market Data')]")
        action.pause(1)
        action.move_to_element(element).perform()
        calendar = self.driver.find_element(By.XPATH, "//*[contains(@title, 'Calendar')]")
        action.pause(1)
        action.move_to_element(calendar).perform()
        calendar.click()

    def click_next_button(self):
        self.move_to_element(Locators.NEXT)
        self.find_element(Locators.NEXT).click()

    def assert_values_for_the_day(self):
        return hc.assert_that(self.find_element(Locators.CELL_VALUE).text, hc.not_none(),
                              f"A value of element {self.find_element(Locators.CELL_VALUE)} is empty")


'''Alternative approach'''

# class Yahoo(BaseAction):
#     def login(self, user, password):
#         if self.check_element_is_presented(Locators.ACCEPT_COOKIES):
#             self.find_element(Locators.ACCEPT_COOKIES).click()
#         else:
#             pass
#         self.check_element_is_clickable(Locators.SIGN_IN)
#         self.find_element(Locators.SIGN_IN).click()
#         self.input_data(Locators.USERNAME, user)
#         self.find_element(Locators.LOGIN_NEXT_BUTTON).click()
#         self.input_data(Locators.PASSWORD, password)
#         self.find_element(Locators.LOGIN_NEXT_BUTTON).click()
#
#     def click_finances(self):
#         self.find_element(Locators.FINANCES).click()
#
#     def hover_market_data_and_click_calendar(self):
#         action = ActionChains(self.driver)
#         element = self.driver.find_element(By.XPATH, "//*[contains(@title, 'Market Data')]")
#         action.pause(1)
#         action.move_to_element(element).perform()
#         calendar = self.driver.find_element(By.XPATH, "//*[contains(@title, 'Calendar')]")
#         action.pause(1)
#         action.move_to_element(calendar).perform()
#         calendar.click()
#
#     def click_next_button(self):
#         self.move_to_element(Locators.NEXT)
#         self.find_element(Locators.NEXT).click()
#
#     def assert_values_for_the_day(self):
#         return hc.assert_that(self.find_element(Locators.CELL_VALUE).text, hc.not_none(),
#                        f"A value of element {self.find_element(Locators.CELL_VALUE)} is empty")
