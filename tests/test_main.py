import allure
import pytest

from common.constants import MainFooter


class TestFooterMain:
    @allure.story("Авторизация")
    @allure.severity("minor")
    @pytest.mark.usefixtures("auth")
    def test_footer_data(self, app):
        """
        1. Авторизоваться
        2. Проверить наличие иконок в футере
        """
        assert app.main_page.twitter_text() == MainFooter.TWITTER
        assert app.main_page.facebook_text() == MainFooter.FACEBOOK
        assert app.main_page.linkedin_text() == MainFooter.LINKEDIN
        assert app.main_page.footer_copy_text() == MainFooter.FOOTER_COPY
