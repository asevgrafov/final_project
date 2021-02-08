import allure
from common.constants import Users, MainFooter


class TestFooterMain:
    @allure.story("Авторизация")
    @allure.severity("minor")
    def test_footer_data(self, app):
        app.open_main_page()
        username = Users.STANDARD_USERNAME
        password = Users.PASSWORD
        app.authorization.auth(username=username, password=password)
        assert app.main_page.twitter_text() == MainFooter.TWITTER
        assert app.main_page.facebook_text() == MainFooter.FACEBOOK
        assert app.main_page.linkedin_text() == MainFooter.LINKEDIN
        assert app.main_page.footer_copy_text() == MainFooter.FOOTER_COPY
