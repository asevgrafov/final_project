import allure
import pytest

from common.constants import CheckoutSubheader, Alerts
from models.fake_data import PersonalInfo


class TestCheckout:
    @allure.story("Checkout")
    @allure.severity("minor")
    @pytest.mark.pgu
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth_pg")
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
    @pytest.mark.pgu
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart_pg")
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
    @pytest.mark.pgu
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart_pg")
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
    @pytest.mark.pgu
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart_pg")
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
