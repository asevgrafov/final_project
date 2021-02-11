from common.base import BaseClass
from common.constants import PersonalData
from locators.checkout import CheckoutLocators
import logging

logger = logging.getLogger()


class CheckoutPage(BaseClass):
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
        self.input_value(self.firstname(), PersonalData.FIRSTNAME)

    def lastname(self):
        return self.app.driver.find_element(*CheckoutLocators.LASTNAME)

    def input_lastname(self, lastname):
        logger.info(f"Пытаемся заполнить поле lastname значением {lastname}")
        self.input_value(self.lastname(), PersonalData.LASTNAME)

    def postal_code(self):
        return self.app.driver.find_element(*CheckoutLocators.POSTAL_CODE)

    def input_postal_code(self, postal_code):
        logger.info(f"Пытаемся заполнить поле postal code значением {postal_code}")
        self.input_value(self.postal_code(), PersonalData.POSTAL_CODE)

    def input_all_value(self, firstname, lastname, postal_code):
        logger.info(
            f"Пытаемся заполнить поля значениями: "
            f"{firstname}, {lastname}, {postal_code}"
        )
        self.input_value(self.firstname(), PersonalData.FIRSTNAME)
        self.input_value(self.lastname(), PersonalData.LASTNAME)
        self.input_value(self.postal_code(), PersonalData.POSTAL_CODE)

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
