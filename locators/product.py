from selenium.webdriver.common.by import By


class ProductPageLocators:
    BACK = (By.XPATH, '//*[@class="inventory_details_back_button"]')
    PRODUCT_NAME = (By.XPATH, '//*[@class="inventory_details_name"]')
    PRODUCT_DESCRIPTION = (By.XPATH, '//*[@class="inventory_details_desc"]')
    PRODUCT_PRICE = (By.XPATH, '//*[@class="inventory_details_price"]')
    ADD_TO_CART = (By.XPATH, '//*[@class="btn_primary btn_inventory"]')
    REMOVE = (By.XPATH, '//*[@class="btn_secondary btn_inventory"]')
