from selenium.webdriver.common.by import By


class CartLocators:
    YOUR_CART = (By.XPATH, '//*[@class="subheader"]')
    CONTINUE_SHOPPING = (By.XPATH, '//*[@class="btn_secondary"]')
    CHECKOUT = (By.XPATH, '//*[@class="btn_action checkout_button"]')
