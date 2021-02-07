from selenium.webdriver.common.by import By


class AuthorizationLocators:
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    LOGIN_INPUT = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
