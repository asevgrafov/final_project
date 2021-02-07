import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from common.logger import setup

from pages.authorization_page import AuthorizationPage

logger = logging.getLogger()


class Application:
    def __init__(self, headless, url):
        setup("INFO")
        logger.setLevel("INFO")
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

    def open_main_page(self):
        logger.info("Open main page")
        self.driver.get(self.url)

    def open_page(self, url: str):
        self.driver.get(f"{self.url}{url}")

    def browser_close(self):
        self.driver.quit()
