from selenium.webdriver.common.by import By


class CompletePageLocators:
    SUBHEADER = (By.XPATH, '//*[@class="subheader"]')
    COMPLETE_HEADER = (By.XPATH, '//*[@class="complete-header"]')
    COMPLETE_TEXT = (By.XPATH, '//*[@class="complete-text"]')
