import allure
import pytest

from common.constants import Cart, Product


class TestCart:
    @allure.story("Cart")
    @allure.severity("minor")
    @pytest.mark.pu
    @pytest.mark.usefixtures("auth_pu")
    def test_move_to_cart(self, app):
        """
        1. Авторизоваться
        2. Перейти в корзину
        3. Проверить текст в subheader'e
        """
        app.main_page.cart_icon_click()
        assert app.cart_page.subheader_text() == Cart.YOUR_CART

    @allure.story("Cart")
    @allure.severity("minor")
    @pytest.mark.pu
    @pytest.mark.usefixtures("auth_pu")
    def test_add_to_cart(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Проверить наличие кнопки Remove и иконки количества товаров в корзине
        5. Перейти в корзину
        6. Проверить name, description, price и наличие кнопки remove
        """
        app.main_page.move_to_product_click()
        app.product_page.add_to_cart_click()
        name = app.product_page.get_name_text()
        description = app.product_page.get_description_text()
        price = app.product_page.get_price_text()
        assert app.main_page.is_element_present() is True
        assert app.product_page.is_remove_present() is True
        app.product_page.cart_icon_click()
        assert name == app.cart_page.get_name_text()
        assert description == app.cart_page.get_description_text()
        assert price == Product.PRICE
        assert app.cart_page.remove_button_text() == Cart.REMOVE
        app.cart_page.remove_button_click()
