import logging
from locators.product import ProductPageLocators

logger = logging.getLogger()


class ProductPage:
    def __init__(self, app):
        self.app = app

    def back(self):
        return self.app.driver.find_element(*ProductPageLocators.BACK)

    def back_click(self):
        logger.info("Пытаемся кликнуть на кнопку back")
        self.back().click()

    def get_name(self):
        return self.app.driver.find_element(*ProductPageLocators.PRODUCT_NAME)

    def get_name_text(self):
        return self.get_name().text

    def get_description(self):
        return self.app.driver.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION)

    def get_description_text(self):
        return self.get_description().text

    def get_price(self):
        return self.app.driver.find_element(*ProductPageLocators.PRODUCT_PRICE)

    def get_price_text(self):
        return self.get_price().text

    def add_to_cart(self):
        return self.app.driver.find_element(*ProductPageLocators.ADD_TO_CART)

    def add_to_cart_click(self):
        logger.info("Пытаемся кликнуть на кнопку add to cart")
        self.add_to_cart().click()

    def remove(self):
        return self.app.driver.find_element(*ProductPageLocators.REMOVE)

    def remove_click(self):
        logger.info("Пытаемся кликнуть на кнопку remove")
        self.remove().click()

    def cart_icon(self):
        return self.app.driver.find_element(*ProductPageLocators.CART)

    def cart_icon_click(self):
        logger.info("Пытаемся кликнуть на иконку корзины")
        self.cart_icon().click()
