import allure
import pytest

from common.constants import MainFooter, Cart, MainHeader, SauceLabs, Title


class TestFooterMain:
    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytest.mark.usefixtures("auth")
    def test_footer_data(self, app):
        """
        1. Авторизоваться
        2. Проверить наличие иконок в футере
        """
        assert app.main_page.twitter_text() == MainFooter.TWITTER
        assert app.main_page.facebook_text() == MainFooter.FACEBOOK
        assert app.main_page.linkedin_text() == MainFooter.LINKEDIN
        assert app.main_page.footer_copy_text() == MainFooter.FOOTER_COPY


class TestHeaderMain:
    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytest.mark.usefixtures("auth")
    def test_move_to_cart(self, app):
        """
        1. Авторизоваться
        2. Перейти в корзину
        3. Проверить текст в subheader'e
        """
        app.main_page.cart_icon_click()
        assert app.cart_page.subheader_text() == Cart.YOUR_CART

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytest.mark.usefixtures("auth")
    def test_move_to_all_items(self, app):
        """
        1. Авторизоваться
        2. Кликнуть по бургеру
        3. Кликнуть по all items
        4. Проверить текст product label
        """
        app.main_page.burger_button_click()
        app.main_page.all_items_click()
        assert app.main_page.product_label_text() == MainHeader.PRODUCT_LABEL

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytest.mark.usefixtures("auth")
    def test_move_to_about(self, app):
        """
        1. Авторизоваться
        2. Кликнуть по бургеру
        3. Кликнуть по about
        4. Проверить Title?
        """
        app.main_page.burger_button_click()
        app.main_page.about_click()
        assert app.saucelabs.get_title() == SauceLabs.TITLE

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytest.mark.usefixtures("auth")
    def test_move_to_logout(self, app):
        """
        1. Авторизоваться
        2. Кликнуть по бургеру
        3. Кликнуть по logout
        4. Проверить Title?
        """
        app.main_page.burger_button_click()
        app.main_page.logout_click()
        assert app.authorization.get_title() == Title.TITLE

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytest.mark.usefixtures("auth")
    @pytest.mark.skip(reason="При клике на reset app state ничего не происходит")
    def test_move_to_reset_app(self, app):
        """
        1. Авторизоваться
        2. Кликнуть по бургеру
        3. Кликнуть по reset app state
        """
        app.main_page.burger_button_click()
        app.main_page.reset_app_click()
