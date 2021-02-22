import allure
import pytest
from pytest_testrail.plugin import pytestrail

from common.constants import Users, Title, Alerts
from models.fake_data import UserData


class TestAuth:
    data = UserData.random()

    @allure.story("Авторизация")
    @allure.severity("critical")
    @pytestrail.case("C1")
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "username, password",
        (
            (Users.STANDARD_USERNAME, Users.PASSWORD),
            (Users.PROBLEM_USERNAME, Users.PASSWORD),
            (Users.PERFORMANCE_GLITCH_USERNAME, Users.PASSWORD),
        ),
    )
    def test_valid_auth(self, app, username, password):
        """
        1. Открыть страницу
        2. Ввести username и password
        3. Кликнуть на кнопку Login
        4. Проверить title
        """
        app.open_main_page()
        app.authorization.auth(username=username, password=password)
        assert app.main_page.get_title() == Title.TITLE

    @allure.story("Авторизация")
    @allure.severity("critical")
    @pytestrail.case("C2")
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "username, password, alert",
        (
            (data.username, data.password, Alerts.INVALID_DATA_ALERT),
            (Users.EMPTY_USERNAME, Users.EMPTY_PASSWORD, Alerts.EMPTY_ALERT),
            (Users.LOCKED_USERNAME, Users.LOCKED_PASSWORD, Alerts.LOCKED_USER_ALERT),
        ),
    )
    def test_invalid_auth(self, app, username, password, alert):
        """
        1. Открыть страницу
        2. Ввести username и password
        3. Кликнуть на кнопку Login
        4. Проверить alert
        """
        app.open_main_page()
        app.authorization.auth(username=username, password=password)
        assert app.authorization.alert_text() == alert
