import allure
from pytest_testrail.plugin import testrail

from common.constants import Users, Title


class TestAuth:
    @allure.story("Авторизация")
    @allure.severity("blocker")
    @testrail("C1")
    def test_auth_shop(self, app):
        """
        1. Открыть страницу
        2. Ввести username и password
        3. Кликнуть на кнопку Login
        4. Проверить title
        """
        app.open_main_page()
        username = Users.USERNAME
        password = Users.PASSWORD
        app.authorization.auth(username=username, password=password)
        assert app.authorization.get_title() == Title.TITLE
