import allure
import pytest

from common.constants import MainFooter, Cart


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
