from selenium import webdriver
import logging

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.authorization_page import AuthorizationPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.complete_page import CompletePage
from pages.main_page import MainPage
from pages.overview_page import OverviewPage
from pages.product_page import ProductPage
from pages.saucelabs_page import SauceLabsPage

logger = logging.getLogger()


class Application:
    def __init__(self, headless, url):
        options: Options = Options()
        if headless:
            options.add_argument("--headless")
        self.url = url
        try:
            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=options
            )
        except ValueError:
            self.driver = webdriver.Chrome(r"C:\chromedriver.exe", options=options)
        self.driver.implicitly_wait(10)
        self.authorization = AuthorizationPage(self)
        self.main_page = MainPage(self)
        self.cart_page = CartPage(self)
        self.saucelabs = SauceLabsPage(self)
        self.product_page = ProductPage(self)
        self.checkout_page = CheckoutPage(self)
        self.overview_page = OverviewPage(self)
        self.complete_page = CompletePage(self)

    def open_main_page(self):
        logger.info("Open authorization page")
        self.driver.get(self.url)

    def open_page(self, url: str):
        self.driver.get(f"{self.url}{url}")

    def browser_close(self):
        self.driver.quit()
