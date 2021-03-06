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

    def remove_button(self):
        return self.app.driver.find_element(*CartLocators.REMOVE)

    def remove_button_click(self):
        self.remove_button().click()

    def remove_button_text(self):
        return self.remove_button().text

    def get_name(self):
        return self.app.driver.find_element(*CartLocators.ITEM_NAME)

    def get_name_text(self):
        return self.get_name().text

    def get_description(self):
        return self.app.driver.find_element(*CartLocators.ITEM_DESCRIPTION)

    def get_description_text(self):
        return self.get_description().text

    def get_price(self):
        return self.app.driver.find_element(*CartLocators.ITEM_PRICE)

    def get_price_text(self):
        return self.get_price().text

    def checkout(self):
        return self.app.driver.find_element(*CartLocators.CHECKOUT)

    def checkout_click(self):
        logger.info("Пытаемся кликнуть на кнопку checkout")
        self.checkout().click()

    def continue_shopping(self):
        return self.app.driver.find_element(*CartLocators.CONTINUE_SHOPPING)

    def continue_shopping_click(self):
        logger.info("Пытаемся кликнуть на кнопку continue shopping")
        self.continue_shopping().click()
