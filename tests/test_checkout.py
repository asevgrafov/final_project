import allure
import pytest

from common.constants import CheckoutSubheader, Alerts, PersonalData


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
        6. Проверить заголовок страницы
        """
        app.main_page.move_to_product_click()
        app.product_page.add_to_cart_click()
        app.product_page.cart_icon_click()
        app.cart_page.checkout_click()
        assert app.checkout_page.get_subheader_text() == CheckoutSubheader.CHECKOUT
        app.checkout_page.cancel_click()
        app.cart_page.remove_button_click()

    @allure.story("Checkout")
    @allure.severity("minor")
    @pytest.mark.usefixtures("product_in_cart")
    def test_empty_firstname_field(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к странице checkout
        6. Проверить alert об обязательном поле firstname
        """
        app.cart_page.checkout_click()
        app.checkout_page.continue_click()
        assert app.checkout_page.error_text() == Alerts.FIRSTNAME_REQUIRED
        app.checkout_page.cancel_click()
        app.cart_page.remove_button_click()

    @allure.story("Checkout")
    @allure.severity("minor")
    @pytest.mark.usefixtures("product_in_cart")
    def test_empty_lastname_field(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к странице checkout
        6. Проверить alert об обязательном поле lastname
        """
        app.cart_page.checkout_click()
        app.checkout_page.input_firstname(firstname=PersonalData.FIRSTNAME)
        app.checkout_page.continue_click()
        assert app.checkout_page.error_text() == Alerts.LASTNAME_REQUIRED
        app.checkout_page.cancel_click()
        app.cart_page.remove_button_click()

    @allure.story("Checkout")
    @allure.severity("minor")
    @pytest.mark.usefixtures("product_in_cart")
    def test_empty_postal_code_field(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к странице checkout
        6. Проверить alert об обязательном поле postal_code
        """
        app.cart_page.checkout_click()
        app.checkout_page.input_firstname(firstname=PersonalData.FIRSTNAME)
        app.checkout_page.input_lastname(lastname=PersonalData.LASTNAME)
        app.checkout_page.continue_click()
        assert app.checkout_page.error_text() == Alerts.POSTAL_CODE_REQUIRED
        app.checkout_page.cancel_click()
        app.cart_page.remove_button_click()
