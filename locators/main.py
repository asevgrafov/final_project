from selenium.webdriver.common.by import By


class MainFooterLocators:
    TWITTER = (By.XPATH, '//*[@class="social_twitter"]')
    FACEBOOK = (By.XPATH, '//*[@class="social_facebook"]')
    LINKEDIN = (By.XPATH, '//*[@class="social_linkedin"]')
    FOOTER_COPY = (By.XPATH, '//*[@class="footer_copy"]')


class MainHeaderLocators:
    CART = (By.XPATH, '//*[@data-icon="shopping-cart"]')
    BURGER_BUTTON = (By.XPATH, '//*[@class="bm-burger-button"]')
    SORT_CONTAINER = (By.XPATH, '//*[@class="product_sort_container"]')
