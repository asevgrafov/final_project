from selenium.common.exceptions import NoSuchElementException

from common.base import BaseClass
from locators.authorization import AuthorizationLocators
import logging

logger = logging.getLogger()


class AuthorizationPage(BaseClass):
    def __init__(self, app):
        self.app = app

    def username_field(self):
        return self.app.driver.find_element(*AuthorizationLocators.LOGIN_INPUT)

    def username_field_is_visible(self):
        """
        Проверка наличия поля ввода username на странице
        """
        logger.info("Проверяем есть ли на странице поле ввода username")
        try:
            self.username_field()
            return True
        except NoSuchElementException:
            return False

    def password_field(self):
        return self.app.driver.find_element(*AuthorizationLocators.PASSWORD_INPUT)

    def password_field_is_visible(self):
        """
        Проверка наличия поля ввода password на странице
        """
        logger.info("Проверяем есть ли на странице поле ввода password")
        try:
            self.password_field()
            return True
        except NoSuchElementException:
            return False

    def login_button(self):
        return self.app.driver.find_element(*AuthorizationLocators.LOGIN_BUTTON)

    def login_button_is_visible(self):
        """
        Проверка наличия кнопки login на странице
        """
        logger.info("Проверяем есть ли на странице кнопка login")
        try:
            self.login_button()
            return True
        except NoSuchElementException:
            return False

    def auth(self, username: str, password: str):
        logger.info(
            f"Пытаемся авторизоваться с помощью"
            f" username: {username} и password: {password}"
        )
        self.username_field().send_keys(username)
        self.password_field().send_keys(password)
        self.login_button().click()

    def get_title(self):
        return self.app.driver.title

    def alert_field(self):
        return self.app.driver.find_element(*AuthorizationLocators.ALERT)

    def alert_text(self):
        return self.alert_field().text
