import allure
import pytest
from pytest_testrail.plugin import pytestrail

from common.constants import MainFooter, Cart, MainHeader, SauceLabs, Title


class TestFooterMain:
    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C9")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_footer_data(self, app):
        """
        1. Авторизоваться
        2. Проверить наличие иконок в футере
        3. Проверить ссылки в href
        """
        assert app.main_page.twitter_is_visible() is True
        assert app.main_page.twitter_href_text() == MainFooter.TWITTER_HREF
        assert app.main_page.facebook_is_visible() is True
        assert app.main_page.facebook_href_text() == MainFooter.FACEBOOK_HREF
        assert app.main_page.linkedin_is_visible() is True
        assert app.main_page.linkedin_href_text() == MainFooter.LINKEDIN_HREF
        assert app.main_page.footer_copy_text() == MainFooter.FOOTER_COPY

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C19")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_twitter_click(self, app):
        """
        1. Авторизоваться
        2. Кликнуть по иконке twitter
        3. Переключить вкладку в браузере
        4. Записать текущий URL
        5. Закрыть текущую вкладку браузера
        6. Сравнить записанный URL со ссылкой в href
        """
        href = app.main_page.twitter_href_text()
        app.main_page.twitter_href_click()
        app.main_page.switch_browser_tab()
        url = app.main_page.get_current_url()
        app.main_page.close_current_tab()
        app.main_page.return_old_tab()
        assert href == url

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytest.mark.skip(reason="Не всегда открывает ссылку однообразно")
    @pytestrail.case("C20")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_facebook_click(self, app):
        """
        1. Авторизоваться
        2. Кликнуть по иконке facebook
        3. Переключить вкладку в браузере
        4. Записать текущий URL
        5. Закрыть текущую вкладку браузера
        6. Сравнить записанный URL со ссылкой в href
        """
        href = app.main_page.facebook_href_text()
        app.main_page.facebook_href_click()
        app.main_page.switch_browser_tab()
        url = app.main_page.get_current_url()
        app.main_page.close_current_tab()
        app.main_page.return_old_tab()
        assert href == url

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytest.mark.skip(reason="Linkedin заблокирован в России")
    @pytestrail.case("C21")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_linkedin_click(self, app):
        """
        1. Авторизоваться
        2. Кликнуть по иконке linkedin
        3. Переключить вкладку в браузере
        4. Записать текущий URL
        5. Закрыть текущую вкладку браузера
        6. Сравнить записанный URL со ссылкой в href
        """
        href = app.main_page.linkedin_href_text()
        app.main_page.linkedin_href_click()
        app.main_page.switch_browser_tab()
        url = app.main_page.get_current_url()
        app.main_page.close_current_tab()
        app.main_page.return_old_tab()
        assert href == url


class TestHeaderMain:
    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C11")
    @pytest.mark.smoke
    @pytest.mark.regression
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
    @pytestrail.case("C12")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_move_to_about(self, app):
        """
        1. Авторизоваться
        2. Кликнуть по бургеру
        3. Кликнуть по about
        4. Проверить Title
        """
        app.main_page.burger_button_click()
        app.main_page.about_click()
        assert app.saucelabs.get_title() == SauceLabs.TITLE

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C13")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_move_to_logout(self, app):
        """
        1. Авторизоваться
        2. Кликнуть по бургеру
        3. Кликнуть по logout
        4. Проверить Title
        """
        app.main_page.burger_button_click()
        app.main_page.logout_click()
        assert app.authorization.get_title() == Title.TITLE

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C14")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_move_to_reset_app(self, app):
        """
        1. Авторизоваться
        2. Перейти к карточке товара
        3. Добавить товар в корзину
        4. Проверить счетчик товаров в корзине на иконке
        5. Кликнуть по бургеру
        6. Кликнуть по reset app state
        7. Закрыть бургер
        8. Проверить что иконки количества товаров нет на значке корзины
        """
        app.main_page.move_to_product_click()
        app.product_page.add_to_cart_click()
        assert app.main_page.products_in_cart_text() == Cart.PRODUCT_IN_CART
        app.main_page.burger_button_click()
        app.main_page.reset_app_click()
        app.main_page.all_items_click()
        assert app.main_page.is_element_present() is False


class TestFilterProducts:
    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C15")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    @pytest.mark.parametrize(
        "expected_result",
        [
            pytest.param(True, id="1. Filter AZ works correctly"),
        ],
    )
    def test_az_filter(self, app, expected_result):
        """
        1. Авторизоваться
        2. Выбрать фильтр A-Z
        3. Сравнить название товаров попарно, начиная с первого и второго
        """
        result = app.main_page.check_found_products_az()
        assert result == expected_result

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C16")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    @pytest.mark.parametrize(
        "expected_result",
        [
            pytest.param(True, id="2. Filter ZA works correctly"),
        ],
    )
    def test_za_filter(self, app, expected_result):
        """
        1. Авторизоваться
        2. Выбрать фильтр Z-A
        3. Сравнить название товаров попарно, начиная с первого и второго
        """
        app.main_page.select_filter_za()
        result = app.main_page.check_found_products_za()
        assert result == expected_result

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C17")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    @pytest.mark.parametrize(
        "expected_result",
        [
            pytest.param(True, id="3. Filter Low-High works correctly"),
        ],
    )
    def test_lh_filter(self, app, expected_result):
        """
        1. Авторизоваться
        2. Выбрать фильтр Low-High
        3. Сравнить цену товаров попарно, начиная с первого и второго
        """
        app.main_page.select_filter_lh()
        result = app.main_page.check_found_product_price_lh()
        assert result == expected_result

    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C18")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    @pytest.mark.parametrize(
        "expected_result",
        [
            pytest.param(True, id="4. Filter High-Low works correctly"),
        ],
    )
    def test_hl_filter(self, app, expected_result):
        """
        1. Авторизоваться
        2. Выбрать фильтр High-Low
        3. Сравнить цену товаров попарно, начиная с первого и второго
        """
        app.main_page.select_filter_hl()
        result = app.main_page.check_found_product_price_hl()
        assert result == expected_result


class TestItemsPresent:
    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C22")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_items_present(self, app):
        """
        1. Авторизоваться
        2. Проверить наличие продуктов на странице
        """
        products = app.main_page.find_products()
        assert len(products) > 0


class TestAddAndRemoveToCart:
    @allure.story("Главная страница")
    @allure.severity("minor")
    @pytestrail.case("C23")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("auth")
    def test_add_and_remove_products(self, app):
        """
        1. Авторизоваться
        2. Добавить товары в корзину
        3. Проверить наличие кнопки Remove, иконки количества товаров в корзине
        и количество добавленных товаров в корзину
        4. Убрать товары из корзины
        5. Проверить наличие кнопки Add to cart и иконки количества товаров в корзине
        """
        app.main_page.click_add_to_cart_buttons()
        remove_buttons = app.main_page.find_remove_buttons()
        product_in_cart = app.main_page.products_in_cart_text()
        assert app.main_page.is_element_present() is True
        assert len(remove_buttons) > 0
        assert str(len(remove_buttons)) == product_in_cart
        app.main_page.click_remove_buttons()
        add_buttons = app.main_page.find_add_to_cart_buttons()
        assert len(add_buttons) > 0
        assert app.main_page.is_element_present() is False
