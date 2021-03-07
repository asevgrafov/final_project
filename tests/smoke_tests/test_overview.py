import allure
import pytest
from pytest_testrail.plugin import pytestrail

from common.constants import Overview, Finish
from models.fake_data import PersonalInfo


class TestOverview:
    @allure.story("Overview")
    @allure.severity("minor")
    @pytestrail.case("C32")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart")
    def test_move_to_overview(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к оформлению заказа
        6. Ввести валидные данные в поля персональной информации
        7. Кликнуть Finish
        8. Проверить нахождение на странице Overview
        """
        personal_data = PersonalInfo.random()
        app.cart_page.checkout_click()
        app.checkout_page.input_all_value(
            firstname=personal_data.firstname,
            lastname=personal_data.lastname,
            postal_code=personal_data.postal_code,
        )
        app.checkout_page.continue_click()
        assert app.overview_page.get_subheader_text() == Overview.OVERVIEW
        app.overview_page.cancel_click()
        app.main_page.cart_icon_click()
        app.cart_page.remove_button_click()

    @allure.story("Overview")
    @allure.severity("minor")
    @pytestrail.case("C33")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart")
    def test_cancel_button_click(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к оформлению заказа
        6. Ввести валидные данные в поля персональной информации
        7. Кликнуть Finish
        8. Кликнуть на Cancel
        9. Проверить нахождение на главной странице
        """
        personal_data = PersonalInfo.random()
        app.cart_page.checkout_click()
        app.checkout_page.input_all_value(
            firstname=personal_data.firstname,
            lastname=personal_data.lastname,
            postal_code=personal_data.postal_code,
        )
        app.checkout_page.continue_click()
        app.overview_page.cancel_click()
        assert app.main_page.is_products_present() is True
        app.main_page.cart_icon_click()
        app.cart_page.remove_button_click()

    @allure.story("Overview")
    @allure.severity("minor")
    @pytestrail.case("C34")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_check_info(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к оформлению заказа
        6. Ввести валидные данные в поля персональной информации
        7. Кликнуть Finish
        8. Проверяем всю информацию на странице
        """
        personal_data = PersonalInfo.random()
        app.main_page.move_to_product_click()
        name = app.product_page.get_name_text()
        description = app.product_page.get_description_text()
        price = app.product_page.get_price_text()
        app.product_page.add_to_cart_click()
        app.product_page.cart_icon_click()
        app.cart_page.checkout_click()
        app.checkout_page.input_all_value(
            firstname=personal_data.firstname,
            lastname=personal_data.lastname,
            postal_code=personal_data.postal_code,
        )
        app.checkout_page.continue_click()
        assert app.overview_page.get_name_text() == name
        assert app.overview_page.get_description_text() == description
        assert app.overview_page.get_price_text() == price
        assert app.overview_page.get_payment_info() == "SauceCard #31337"
        assert app.overview_page.get_shipping_info() == "FREE PONY EXPRESS DELIVERY!"
        assert app.overview_page.split_item_total() == price
        assert app.overview_page.split_tax() == Overview.TAX
        assert app.overview_page.split_total() == Overview.TOTAL
        app.overview_page.cancel_click()
        app.main_page.cart_icon_click()
        app.cart_page.remove_button_click()

    @allure.story("Overview")
    @allure.severity("minor")
    @pytestrail.case("C35")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("product_in_cart")
    def test_finish_button_click(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к оформлению заказа
        6. Ввести валидные данные в поля персональной информации
        7. Кликнуть на Finish
        8. Кликнуть на Finish
        9. Проверить нахождение на финальной странице
        """
        personal_data = PersonalInfo.random()
        app.cart_page.checkout_click()
        app.checkout_page.input_all_value(
            firstname=personal_data.firstname,
            lastname=personal_data.lastname,
            postal_code=personal_data.postal_code,
        )
        app.checkout_page.continue_click()
        app.overview_page.finish_click()
        assert app.complete_page.get_subheader_text() == Finish.FINISH
        assert app.complete_page.get_header_text() in Finish.COMPLETE_HEADER
        assert app.complete_page.get_complete_text() == Finish.COMPLETE_TEXT
