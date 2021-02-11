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
