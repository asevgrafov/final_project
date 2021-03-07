import allure
import pytest
from pytest_testrail.plugin import pytestrail

from common.constants import CheckoutSubheader, Alerts, Cart
from models.fake_data import PersonalInfo


class TestCheckout:
    @allure.story("Checkout")
    @allure.severity("minor")
    @pytestrail.case("C5")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart")
    def test_checkout_page(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к странице checkout
        6. Проверить заголовок страницы
        """
        app.cart_page.checkout_click()
        assert app.checkout_page.get_subheader_text() == CheckoutSubheader.CHECKOUT
        app.checkout_page.cancel_click()
        app.cart_page.remove_button_click()

    @allure.story("Checkout")
    @allure.severity("minor")
    @pytestrail.case("")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart")
    def test_back_to_cart(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к странице checkout
        6. Вернуться назад в корзину
        7. Проверить нахождение на странице корзины
        """
        app.cart_page.checkout_click()
        app.checkout_page.cancel_click()
        assert app.cart_page.subheader_text() == Cart.YOUR_CART
        app.cart_page.remove_button_click()

    @allure.story("Checkout")
    @allure.severity("minor")
    @pytestrail.case("C6")
    @pytest.mark.smoke
    @pytest.mark.regression
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
    @pytestrail.case("C7")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart")
    def test_empty_lastname_field(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к странице checkout
        6. Ввести валидные данные в поле firstname
        7. Проверить alert об обязательном поле lastname
        """
        personal_data = PersonalInfo.random()
        app.cart_page.checkout_click()
        app.checkout_page.input_firstname(firstname=personal_data.firstname)
        app.checkout_page.continue_click()
        assert app.checkout_page.error_text() == Alerts.LASTNAME_REQUIRED
        app.checkout_page.cancel_click()
        app.cart_page.remove_button_click()

    @allure.story("Checkout")
    @allure.severity("minor")
    @pytestrail.case("C8")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart")
    def test_empty_postal_code_field(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к странице checkout
        6. Ввести валидные данные в поле firstname
        7. Ввести валидные данные в поле lastname
        8. Проверить alert об обязательном поле postal_code
        """
        personal_data = PersonalInfo.random()
        app.cart_page.checkout_click()
        app.checkout_page.input_firstname(firstname=personal_data.firstname)
        app.checkout_page.input_lastname(lastname=personal_data.lastname)
        app.checkout_page.continue_click()
        assert app.checkout_page.error_text() == Alerts.POSTAL_CODE_REQUIRED
        app.checkout_page.cancel_click()
        app.cart_page.remove_button_click()
