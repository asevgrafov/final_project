import allure
from pytest_testrail.plugin import testrail

from common.constants import Users


class TestAuth:
    @allure.story("Авторизация")
    @allure.severity("blocker")
    @testrail('C1')
    def test_auth_shop(self, app):
        """
        1. Открыть страницу
        2. Кликнуть на login button
        3. Ввести валидные данные
        4. Проверить имя
        """
        app.open_main_page()
        email = Users.EMAIL
        password = Users.PASSWORD
        app.login.auth(email=email, password=password)
        assert app.login.get_userdata() == Users.ACCOUNT_DATA
        app.login.logout_button_click()