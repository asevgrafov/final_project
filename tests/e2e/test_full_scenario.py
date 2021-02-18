import allure

from common.constants import Users, Finish
from models.fake_data import PersonalInfo


class TestE2E:
    @allure.story("E2E")
    @allure.severity("critical")
    def test_full_scenario(self, app):
        """
        1. Авторизоваться
        2. Перейти на карточку товара
        3. Добавить товар в корзину
        4. Перейти в корзину
        5. Перейти к странице checkout
        6. Заполнить все поля
        7. Перейти к странице overview
        8. Перейти к финишной странице
        9. Проверить нахождение на финишной странице
        """
        personal_data = PersonalInfo.random()
        app.open_main_page()
        app.authorization.auth(
            username=Users.STANDARD_USERNAME, password=Users.PASSWORD
        )
        app.main_page.move_to_product_click()
        app.product_page.add_to_cart_click()
        app.product_page.cart_icon_click()
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
