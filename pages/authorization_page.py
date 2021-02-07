from locators.authorization import AuthorizationLocators


class AuthorizationPage:
    def __init__(self, app):
        self.app = app

    def user_name_field(self):
        return self.app.driver.find_element(*AuthorizationLocators.LOGIN_INPUT)

    def password_field(self):
        return self.app.driver.find_element(*AuthorizationLocators.PASSWORD_INPUT)

    def login_button(self):
        return self.app.driver.find_element(*AuthorizationLocators.LOGIN_BUTTON)

    def auth(self, username, password):
        self.user_name_field().send_keys(username)
        self.password_field().send_keys(password)
        self.login_button().click()

    def get_title(self):
        return self.app.driver.title
