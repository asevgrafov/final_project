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
    PRODUCT_LABEL = (By.XPATH, '//*[@class="product_label"]')


class BurgerButtonLocators:
    ALL_ITEMS = (By.XPATH, '//*[@id="inventory_sidebar_link"]')
    ABOUT = (By.XPATH, '//*[@id="about_sidebar_link"]')
    LOGOUT = (By.XPATH, '//*[@id="logout_sidebar_link"]')
    RESET_APP_STATE = (By.XPATH, '//*[@id="reset_sidebar_link"]')


class MainLocators:
    ADD_TO_CART = (By.XPATH, '//*[@class="btn_primary btn_inventory"]')
    REMOVE = (By.XPATH, '//*[@class="btn_secondary btn_inventory"]')
    PRODUCT = (By.XPATH, '//*[@id="item_0_title_link"]')
