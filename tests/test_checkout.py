import allure
import pytest

from common.constants import CheckoutSubheader


class TestCheckout:
    @allure.story("Checkout")
    @allure.severity("minor")
    @pytest.mark.usefixtures("auth")
    def test_checkout_page(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к странице checkout
        """
        app.main_page.move_to_product_click()
        app.product_page.add_to_cart_click()
        app.product_page.cart_icon_click()
        app.cart_page.checkout_click()
        assert app.checkout_page.get_subheader_text() == CheckoutSubheader.CHECKOUT
