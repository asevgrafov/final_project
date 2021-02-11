import allure

from common.constants import Users, PersonalData, Finish


class TestE2E:
    @allure.story("E2E")
    @allure.severity("critical")
    def test_full_scenario(self, app):
        app.open_main_page()
        app.authorization.auth(
            username=Users.STANDARD_USERNAME, password=Users.PASSWORD
        )
        app.main_page.move_to_product_click()
        app.product_page.add_to_cart_click()
        app.product_page.cart_icon_click()
        app.cart_page.checkout_click()
        app.checkout_page.input_firstname(firstname=PersonalData.FIRSTNAME)
        app.checkout_page.input_lastname(lastname=PersonalData.LASTNAME)
        app.checkout_page.input_postal_code(postal_code=PersonalData.POSTAL_CODE)
        app.checkout_page.continue_click()
        app.overview_page.finish_click()
        assert app.complete_page.get_subheader_text() == Finish.FINISH
        assert app.complete_page.get_header_text() in Finish.COMPLETE_HEADER
        assert app.complete_page.get_complete_text() == Finish.COMPLETE_TEXT
