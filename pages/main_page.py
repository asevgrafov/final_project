from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from common.constants import Filter
from locators.main import (
    MainFooterLocators,
    MainHeaderLocators,
    BurgerButtonLocators,
    MainLocators,
)
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

    def twitter_href(self):
        return self.app.driver.find_element(*MainFooterLocators.TWITTER_HREF)

    def twitter_href_text(self):
        logger.info("Пытаемся забрать текст из аттрибута href")
        return self.twitter_href().get_attribute("href")

    def twitter_href_click(self):
        logger.info("Пытаемся кликнуть на иконку twitter")
        self.twitter_href().click()

    def switch_browser_tab(self):
        logger.info("Пытаемся переключить вкладку в браузере на вторую")
        window_after = self.app.driver.window_handles[1]
        self.app.driver.switch_to.window(window_after)

    def return_old_tab(self):
        logger.info("Пытаемся вернуться на первую вкладку в браузере")
        window_before = self.app.driver.window_handles[0]
        self.app.driver.switch_to.window(window_before)

    def close_current_tab(self):
        logger.info("Пытаемся закрыть текущую вкладку в браузере")
        self.app.driver.close()

    def get_current_url(self):
        logger.info("Пытаемся забрать URL страницы, на которой находимся")
        self.app.driver.implicitly_wait(10)
        return self.app.driver.current_url

    def twitter_is_visible(self):
        """
        Проверка наличия иконки twitter на странице
        """
        logger.info("Проверяем есть ли на странице иконка twitter")
        try:
            self.twitter_icon()
            return True
        except NoSuchElementException:
            return False

    def facebook_icon(self):
        logger.info("Пытаемся найти иконку Facebook")
        return self.app.driver.find_element(*MainFooterLocators.FACEBOOK)

    def facebook_href(self):
        return self.app.driver.find_element(*MainFooterLocators.FACEBOOK_HREF)

    def facebook_href_text(self):
        logger.info("Пытаемся забрать текст из аттрибута href")
        return self.facebook_href().get_attribute("href")

    def facebook_href_click(self):
        logger.info("Пытаемся кликнуть на иконку facebook")
        self.facebook_href().click()

    def facebook_is_visible(self):
        """
        Проверка наличия иконки facebook на странице
        """
        logger.info("Проверяем есть ли на странице иконка facebook")
        try:
            self.facebook_icon()
            return True
        except NoSuchElementException:
            return False

    def linkedin_icon(self):
        logger.info("Пытаемся найти иконку LinkedIn")
        return self.app.driver.find_element(*MainFooterLocators.LINKEDIN)

    def linkedin_href(self):
        return self.app.driver.find_element(*MainFooterLocators.LINKEDIN_HREF)

    def linkedin_href_text(self):
        logger.info("Пытаемся забрать текст из аттрибута href")
        return self.linkedin_href().get_attribute("href")

    def linkedin_href_click(self):
        logger.info("Пытаемся кликнуть на иконку linkedin")
        self.linkedin_href().click()

    def linkedin_is_visible(self):
        """
        Проверка наличия иконки linkedin на странице
        """
        logger.info("Проверяем есть ли на странице иконка linkedin")
        try:
            self.linkedin_icon()
            return True
        except NoSuchElementException:
            return False

    def footer_copy(self):
        logger.info("Пытаемся найти иконку Footer_copy")
        return self.app.driver.find_element(*MainFooterLocators.FOOTER_COPY)

    def footer_copy_text(self):
        return self.footer_copy().text

    def cart_icon(self):
        return self.app.driver.find_element(*MainHeaderLocators.CART)

    def cart_icon_click(self):
        logger.info("Пытаемся кликнуть по иконке корзины")
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

    def products_in_cart(self):
        return self.app.driver.find_element(*MainHeaderLocators.COUNT_PRODUCTS_IN_CART)

    def products_in_cart_text(self):
        return self.products_in_cart().text

    def reset_app(self):
        return self.app.driver.find_element(*BurgerButtonLocators.RESET_APP_STATE)

    def reset_app_click(self):
        logger.info("Пытаемся кликнуть по reset app state")
        self.reset_app().click()

    def exit_button(self):
        return self.app.driver.find_element(*BurgerButtonLocators.EXIT)

    def exit_button_click(self):
        logger.info("Пытаемся кликнуть по крестику в модалке")
        self.exit_button().click()

    def is_element_present(self):
        """
        Проверка наличия иконки количества товаров в корзине
        на странице
        """
        logger.info(
            "Проверяем есть ли на странице иконка " "количества товаров в корзине"
        )
        try:
            self.products_in_cart()
            return True
        except NoSuchElementException:
            return False

    def add_to_cart(self):
        return self.app.driver.find_element(*MainLocators.ADD_TO_CART)

    def add_to_cart_click(self):
        logger.info("Пытаемся добавить товар в корзину")
        self.add_to_cart().click()

    def move_to_product(self):
        return self.app.driver.find_element(*MainLocators.PRODUCT)

    def move_to_product_click(self):
        logger.info("Пытаемся кликнуть по товару")
        self.move_to_product().click()

    def find_products(self):
        logger.info("Пытаемся найти товары на странице")
        return self.app.driver.find_elements(*MainLocators.PRODUCTS_NAME)

    def filter_list(self):
        return self.app.driver.find_element(*MainLocators.FILTER)

    def select_filter_za(self):
        logger.info("Пытаемся выбрать фильтр ZA в выпадающем списке")
        select = Select(self.filter_list())
        select.select_by_value(Filter.ZA)

    def check_found_products_az(self):
        """
        Проверка сортировки A-Z
        """
        logger.info("Пытаемся найти товары на странице")
        products = self.find_products()
        for i in range(1, len(products)):
            if products[i - 1].text > products[i].text:
                return False
        return True

    def check_found_products_za(self):
        """
        Проверка сортировки Z-A
        """
        logger.info("Пытаемся найти товары на странице")
        products = self.find_products()
        for i in range(1, len(products)):
            if products[i - 1].text < products[i].text:
                return False
        return True

    def check_products_price(self):
        return self.app.driver.find_elements(*MainLocators.PRODUCTS_PRICE)

    def select_filter_lh(self):
        logger.info("Пытаемся выбрать фильтр Low-High в выпадающем списке")
        select = Select(self.filter_list())
        select.select_by_value(Filter.LOHI)

    def select_filter_hl(self):
        logger.info("Пытаемся выбрать фильтр High_low в выпадающем списке")
        select = Select(self.filter_list())
        select.select_by_value(Filter.HILO)

    def check_found_product_price_lh(self):
        """
        Проверка сортировки Low-High
        """
        logger.info("Пытаемся найти товары на странице")
        products = self.check_products_price()
        names = self.find_products()
        for i in range(1, len(products)):
            if (
                products[i - 1].text > products[i].text
                and names[i - 1].text > names[i].text
            ):
                return False
        return True

    def check_found_product_price_hl(self):
        """
        Проверка сортировки High-Low
        """
        logger.info("Пытаемся найти товары на странице")
        products = self.check_products_price()
        names = self.find_products()
        for i in range(1, len(products)):
            if (
                products[i - 1].text < products[i].text
                and names[i - 1].text < names[i].text
            ):
                return False
        return True
