import allure
import pytest
from pytest_testrail.plugin import pytestrail

from common.constants import Cart, Product


class TestCart:
    @allure.story("Cart")
    @allure.severity("minor")
    @pytestrail.case("C10")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
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
    @pytestrail.case("C4")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
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

    @allure.story("Cart")
    @allure.severity("minor")
    @pytestrail.case("C25")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart")
    def test_remove_from_cart(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Проверить наличие кнопки remove
        6. Кликнуть по кнопке Remove
        7. Проверить отсутствие кнопки remove
        """
        assert app.cart_page.remove_is_visible() is True
        app.cart_page.remove_button_click()
        assert app.cart_page.remove_is_visible() is False

    @allure.story("Cart")
    @allure.severity("minor")
    @pytestrail.case("C26")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart")
    def test_continue_shopping(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Кликнуть на кнопку Continue shopping
        6. Проверить нахождение на главной странице
        """
        app.cart_page.continue_shopping_click()
        assert app.main_page.is_products_present() is True
        app.main_page.cart_icon_click()
        app.cart_page.remove_button_click()

    @allure.story("Cart")
    @allure.severity("minor")
    @pytestrail.case("C27")
    @pytest.mark.skip(
        reason="Alert о невозможности перейти к оформлению заказа "
        "с пустой корзиной не появляется"
    )
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_empty_cart_continue(self, app):
        """
        1. Авторизоваться
        2. Перейти в корзину
        3. Проверить что корзина пуста
        4. Кликнуть на кнопку Checkout
        5. Сравнить текст Alert'a
        """
        app.main_page.cart_icon_click()
        assert app.main_page.is_element_present() is False
        app.cart_page.checkout_click()
