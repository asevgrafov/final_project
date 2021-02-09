from locators.main import MainFooterLocators, MainHeaderLocators, BurgerButtonLocators
import logging

logger = logging.getLogger()


class MainPage:
    def __init__(self, app):
        self.app = app

    def get_title(self):
        return self.app.driver.title

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

    def burger_button(self):
        return self.app.driver.find_element(*MainHeaderLocators.BURGER_BUTTON)

    def burger_button_click(self):
        logger.info("Пытаемся кликнуть по burger")
        self.burger_button().click()

    def all_items(self):
        return self.app.driver.find_element(*BurgerButtonLocators.ALL_ITEMS)

    def all_items_click(self):
        logger.info("Пытаемся кликнуть по all items")
        self.all_items().click()

    def product_label(self):
        return self.app.driver.find_element(*MainHeaderLocators.PRODUCT_LABEL)

    def product_label_text(self):
        return self.product_label().text

    def about(self):
        return self.app.driver.find_element(*BurgerButtonLocators.ABOUT)

    def about_click(self):
        logger.info("Пытаемся кликнуть по about")
        self.about().click()

    def logout(self):
        return self.app.driver.find_element(*BurgerButtonLocators.LOGOUT)

    def logout_click(self):
        logger.info("Пытаемся кликнуть по logout")
        self.logout().click()

    def reset_app(self):
        return self.app.driver.find_element(*BurgerButtonLocators.RESET_APP_STATE)

    def reset_app_click(self):
        logger.info("Пытаемся кликнуть по reset app state")
        self.reset_app().click()
