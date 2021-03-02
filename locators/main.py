from selenium.webdriver.common.by import By


class MainFooterLocators:
    TWITTER = (By.XPATH, '//*[@class="social_twitter"]')
    TWITTER_HREF = (By.XPATH, '//*[@href="https://twitter.com/saucelabs"]')
    FACEBOOK = (By.XPATH, '//*[@class="social_facebook"]')
    FACEBOOK_HREF = (By.XPATH, '//*[@href="https://www.facebook.com/saucelabs"]')
    LINKEDIN = (By.XPATH, '//*[@class="social_linkedin"]')
    LINKEDIN_HREF = (
        By.XPATH,
        '//*[@href="https://www.linkedin.com/company/sauce-labs/"]',
    )
    FOOTER_COPY = (By.XPATH, '//*[@class="footer_copy"]')


class MainHeaderLocators:
    CART = (By.XPATH, '//*[@data-icon="shopping-cart"]')
    BURGER_BUTTON = (By.XPATH, '//*[@class="bm-burger-button"]')
    SORT_CONTAINER = (By.XPATH, '//*[@class="product_sort_container"]')
    PRODUCT_LABEL = (By.XPATH, '//*[@class="product_label"]')
    COUNT_PRODUCTS_IN_CART = (
        By.XPATH,
        '//*[@class="fa-layers-counter shopping_cart_badge"]',
    )


class BurgerButtonLocators:
    ALL_ITEMS = (By.XPATH, '//*[@id="inventory_sidebar_link"]')
    ABOUT = (By.XPATH, '//*[@id="about_sidebar_link"]')
    LOGOUT = (By.XPATH, '//*[@id="logout_sidebar_link"]')
    RESET_APP_STATE = (By.XPATH, '//*[@id="reset_sidebar_link"]')
    EXIT = (By.XPATH, '//*[@class="bm-cross-button"]')


class MainLocators:
    ADD_TO_CART = (By.XPATH, '//*[@class="btn_primary btn_inventory"]')
    REMOVE = (By.XPATH, '//*[@class="btn_secondary btn_inventory"]')
    PRODUCT = (By.XPATH, '//*[@id="item_0_title_link"]')
    PRODUCTS_NAME = (By.XPATH, '//*[@class="inventory_item_name"]')
    PRODUCTS_PRICE = (By.XPATH, '//*[@class="inventory_item_price"]')
    FILTER = (By.XPATH, '//*[@class="product_sort_container"]')
    FILTER_AZ = (By.XPATH, '//*[@value="az"]')
    FILTER_ZA = (By.XPATH, '//*[@value="za"]')
    FILTER_LOHI = (By.XPATH, '//*[@value="lohi"]')
    FILTER_HILO = (By.XPATH, '//*[@value="hilo"]')
