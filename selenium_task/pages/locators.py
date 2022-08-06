
from selenium.webdriver.common.by import By


class Locators:
    FINANCES = (By.ID, "root_8")
    ACCEPT_COOKIES = (By.CLASS_NAME, "primary")
    MARKET_DATA = (By.XPATH, "//*[contains(@title, 'Market Data')]")
    CALENDAR = (By.XPATH, "//*[contains(@title, 'Calendar')]")
    NEXT = (By.XPATH, "//*[contains(@title, 'Next')]")
    SIGN_IN = (By.CSS_SELECTOR, "[data-redirect-params$='signin']")
    USERNAME = (By.ID, "login-username")
    PASSWORD = (By.ID, "login-passwd")
    LOGIN_NEXT_BUTTON = (By.ID, "login-signin")
    CELL_VALUE = (By.XPATH, "//*[@id='fin-cal-events']/div[2]/ul/li[4]/a[5]")


