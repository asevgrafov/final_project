from locators.main import MainFooterLocators, MainHeaderLocators
import logging

logger = logging.getLogger()


class MainPage:
    def __init__(self, app):
        self.app = app

    def twitter_icon(self):
        logger.info("Пытаемся найти иконку Twitter")
        return self.app.driver.find_element(*MainFooterLocators.TWITTER)

    def twitter_text(self):
        return self.twitter_icon().text

    def facebook_icon(self):
        logger.info("Пытаемся найти иконку Facebook")
        return self.app.driver.find_element(*MainFooterLocators.FACEBOOK)

    def facebook_text(self):
        return self.facebook_icon().text

    def linkedin_icon(self):
        logger.info("Пытаемся найти иконку LinkedIn")
        return self.app.driver.find_element(*MainFooterLocators.LINKEDIN)

    def linkedin_text(self):
        return self.linkedin_icon().text

    def footer_copy(self):
        logger.info("Пытаемся найти иконку Footer_copy")
        return self.app.driver.find_element(*MainFooterLocators.FOOTER_COPY)

    def footer_copy_text(self):
        return self.footer_copy().text

    def cart_icon(self):
        return self.app.driver.find_element(*MainHeaderLocators.CART)

    def cart_icon_click(self):
        self.cart_icon().click()
