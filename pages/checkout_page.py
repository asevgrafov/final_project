from locators.checkout import CheckoutLocators
import logging

logger = logging.getLogger()


class CheckoutPage:
    def __init__(self, app):
        self.app = app

    def get_subheader(self):
        logger.info("Пытаемся найти subheader")
        return self.app.driver.find_element(*CheckoutLocators.SUBHEADER)

    def get_subheader_text(self):
        return self.get_subheader().text

    def firstname(self):
        return self.app.driver.find_element(*CheckoutLocators.FIRSTNAME)

    def input_firstname(self, firstname):
        logger.info(f"Пытаемся заполнить поле firstname значением {firstname}")
        self.firstname().send_keys(firstname)

    def lastname(self):
        return self.app.driver.find_element(*CheckoutLocators.LASTNAME)

    def input_lastname(self, lastname):
        logger.info(f"Пытаемся заполнить поле lastname значением {lastname}")
        self.lastname().send_keys(lastname)

    def postal_code(self):
        return self.app.driver.find_element(*CheckoutLocators.POSTAL_CODE)

    def input_postal_code(self, postal_code):
        logger.info(f"Пытаемся заполнить поле postal code значением {postal_code}")
        self.postal_code().send_keys(postal_code)

    def cancel(self):
        return self.app.driver.find_element(*CheckoutLocators.CANCEL)

    def cancel_click(self):
        logger.info("Пытаемся кликнуть по кнопке cancel")
        self.cancel().click()

    def continue_button(self):
        return self.app.driver.find_element(*CheckoutLocators.CONTINUE)

    def continue_click(self):
        logger.info("Пытаемся кликнуть по кнопке continue")
        self.continue_button().click()

    def error(self):
        logger.info("Пытаемся найти alert о пустом поле")
        return self.app.driver.find_element(*CheckoutLocators.ERROR_ALERT)

    def error_text(self):
        return self.error().text
