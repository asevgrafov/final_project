from selenium.webdriver.common.by import By


class CheckoutLocators:
    SUBHEADER = (By.XPATH, '//*[@class="subheader"]')
    FIRSTNAME = (By.XPATH, '//*[@id="first-name"]')
    LASTNAME = (By.XPATH, '//*[@id="last-name"]')
    POSTAL_CODE = (By.XPATH, '//*[@id="postal-code"]')
    CANCEL = (By.XPATH, '//*[@class="cart_cancel_link btn_secondary"]')
    CONTINUE = (By.XPATH, '//*[@class="btn_primary cart_button"]')
    ERROR_ALERT = (By.XPATH, '//*[@data-test="error"]')
