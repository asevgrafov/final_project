from locators.authorization import AuthorizationLocators


class AuthorizationPage:
    def __ini__(self, app):
        self.app = self.app

    def user_name_field(self):
        self.app.driver.find_by_element(*AuthorizationLocators.LOGIN_INPUT)