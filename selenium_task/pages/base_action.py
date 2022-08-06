
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://uk.yahoo.com/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_url(self):
        self.driver.get(self.base_url)

    def hover(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()

    def check_element_is_presented(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                               message=f"Element {locator} is not presented")
        if EC.presence_of_element_located(locator):
            return True
        else:
            return "Element is not located"

    def check_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        if EC.presence_of_element_located(locator):
            return True
        else:
            return "Element is not clickable"

    def move_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(2)

    def input_data(self, locator, text):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(text).perform()
        assert element is not None, "Data was not inputted"
