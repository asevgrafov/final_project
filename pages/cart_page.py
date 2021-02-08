from locators.cart import CartLocators
import logging

logger = logging.getLogger()


class CartPage:
    def __init__(self, app):
        self.app = app

    def get_subheader(self):
        logger.info("Пытаемся найти текст Your Cart в subheader'e")
        return self.app.driver.find_element(*CartLocators.YOUR_CART)

    def subheader_text(self):
        return self.get_subheader().text
