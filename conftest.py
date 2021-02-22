import os
import allure
import pytest
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    headless = request.config.getoption("--headless")
    app = Application(headless, url)
    yield app
    app.browser_close()


@pytest.fixture(scope="function")
def auth(request, app):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_main_page()
    app.authorization.auth(username, password)


@pytest.fixture(scope="function")
def auth_pg(request, app):
    username = request.config.getoption("--username_pg")
    password = request.config.getoption("--password")
    app.open_main_page()
    app.authorization.auth(username, password)


@pytest.fixture(scope="function")
def product_in_cart(request, app):
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_main_page()
    app.authorization.auth(username, password)
    app.main_page.move_to_product_click()
    app.product_page.add_to_cart_click()
    app.product_page.cart_icon_click()


@pytest.fixture(scope="function")
def product_in_cart_pg(request, app):
    username = request.config.getoption("--username_pg")
    password = request.config.getoption("--password")
    app.open_main_page()
    app.authorization.auth(username, password)
    app.main_page.move_to_product_click()
    app.product_page.add_to_cart_click()
    app.product_page.cart_icon_click()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode):
                if "app" in item.fixturenames:
                    web_driver = item.funcargs["app"]
                else:
                    print("Fail to take screen-shot")
                    return
            allure.attach(
                web_driver.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print("Fail to take screen-shot: {}".format(e))


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://www.saucedemo.com/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="standard_user",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="secret_sauce",
        help="enter password",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default=False,
        help="launching browser without gui",
    ),
    parser.addoption(
        "--username_pg",
        action="store",
        default="performance_glitch_user",
        help="launching browser without gui",
    ),
