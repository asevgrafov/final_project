from locators.authorization import AuthorizationLocators
import logging

logger = logging.getLogger()


class AuthorizationPage:
    def __init__(self, app):
        self.app = app

    def username_field(self):
        return self.app.driver.find_element(*AuthorizationLocators.LOGIN_INPUT)

    def password_field(self):
        return self.app.driver.find_element(*AuthorizationLocators.PASSWORD_INPUT)

    def login_button(self):
        return self.app.driver.find_element(*AuthorizationLocators.LOGIN_BUTTON)

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
