import logging
from locators.overview import OverviewPageLocators

logger = logging.getLogger()


class OverviewPage:
    def __init__(self, app):
        self.app = app

    def finish(self):
        logger.info("Пытаемся кликнуть на кнопку  finish")
        return self.app.driver.find_element(*OverviewPageLocators.FINISH)

    def finish_click(self):
        self.finish().click()

    def cancel(self):
        logger.info("Пытаемся кликнуть на кнопку finish")
        return self.app.driver.find_element(*OverviewPageLocators.CANCEL)

    def cancel_click(self):
        self.cancel().click()

    def get_subheader(self):
        logger.info("Пытаемся найти subheader на странице Overview")
        return self.app.driver.find_element(*OverviewPageLocators.SUBHEADER)

    def get_subheader_text(self):
        return self.get_subheader().text

    def get_info(self):
        return self.app.driver.find_elements(*OverviewPageLocators.PAYMENT_INFO)

    def get_payment_info(self):
        logger.info("Пытаемся получить текст Payment Information")
        return self.get_info()[0].text

    def get_shipping_info(self):
        logger.info("Пытаемся получить текст Shipping Information")
        return self.get_info()[1].text

    def get_name(self):
        logger.info("Пытаемся найти item name")
        return self.app.driver.find_element(*OverviewPageLocators.ITEM_NAME)

    def get_name_text(self):
        return self.get_name().text

    def get_description(self):
        logger.info("Пытаемся найти item description")
        return self.app.driver.find_element(*OverviewPageLocators.ITEM_DESCRIPTION)

    def get_description_text(self):
        return self.get_description().text

    def get_price(self):
        logger.info("Пытаемся найти item price")
        return self.app.driver.find_element(*OverviewPageLocators.ITEM_PRICE)

    def get_price_text(self):
        return self.get_price().text

    def get_item_total_price(self):
        return self.app.driver.find_element(*OverviewPageLocators.ITEM_TOTAL)

    def get_item_total_text(self):
        logger.info("Пытаемся получить текст Item total")
        return self.get_item_total_price().text

    def split_item_total(self):
        """
        Функция для обрезания строки по символам ": "
        """
        item_total = self.get_item_total_text()
        parts = item_total.rsplit(": ", 1)
        split_total = parts[1]
        return split_total

    def tax(self):
        return self.app.driver.find_element(*OverviewPageLocators.TAX)

    def tax_text(self):
        logger.info("Пытаемся получить текст Tax")
        return self.tax().text

    def split_tax(self):
        """
        Функция для обрезания строки по символу "$"
        """
        tax = self.tax_text()
        parts = tax.rsplit("$", 1)
        split_tax = parts[1]
        return split_tax

    def total(self):
        return self.app.driver.find_element(*OverviewPageLocators.TOTAL)

    def total_text(self):
        logger.info("Пытаемся получить текст Total")
        return self.total().text

    def split_total(self):
        """
        Функция для обрезания строки по символу "$"
        """
        total = self.total_text()
        parts = total.rsplit("$", 1)
        split_total = parts[1]
        return split_total
