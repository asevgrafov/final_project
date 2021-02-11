import logging
from locators.complete import CompletePageLocators

logger = logging.getLogger()


class CompletePage:
    def __init__(self, app):
        self.app = app

    def get_subheader(self):
        logger.info("Пытаемся найти subheader")
        return self.app.driver.find_element(*CompletePageLocators.SUBHEADER)

    def get_subheader_text(self):
        return self.get_subheader().text

    def get_header(self):
        logger.info("Пытаемся найти header с благодарностью")
        return self.app.driver.find_element(*CompletePageLocators.COMPLETE_HEADER)

    def get_header_text(self):
        return self.get_header().text

    def get_complete(self):
        logger.info("Пытаемся найти текст успешного заказа")
        return self.app.driver.find_element(*CompletePageLocators.COMPLETE_TEXT)

    def get_complete_text(self):
        return self.get_complete().text
