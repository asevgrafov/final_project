import allure
import pytest
from pytest_testrail.plugin import pytestrail


class TestProduct:
    @allure.story("Product")
    @allure.severity("minor")
    @pytestrail.case("")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_move_to_cart(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Проверить нахождение на странице товара
        """
        product_name = app.main_page.get_product_name()
        app.main_page.move_to_product_click()
        assert product_name == app.product_page.get_name_text()

    @allure.story("Product")
    @allure.severity("minor")
    @pytestrail.case("")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_back_to_main(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Перейти обратно с помощью кнопки Back
        4. Проверить нахождение на главной странице
        """
        app.main_page.move_to_product_click()
        app.product_page.back_click()
        assert app.main_page.is_products_present() is True

    @allure.story("Product")
    @allure.severity("minor")
    @pytestrail.case("")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_add_to_cart_button_click(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Проверить добавление товара в корзину
        """
        app.main_page.move_to_product_click()
        app.product_page.add_to_cart_click()
        assert app.main_page.is_element_present() is True
        app.product_page.remove_click()

    @allure.story("Product")
    @allure.severity("minor")
    @pytestrail.case("")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_remove_button_click(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Проверить добавление товара в корзину
        5. Убрать товар из корзины
        6. Проверить удаление товара из корзины
        """
        app.main_page.move_to_product_click()
        app.product_page.add_to_cart_click()
        assert app.main_page.is_element_present() is True
        app.product_page.remove_click()
        assert app.main_page.is_element_present() is False
