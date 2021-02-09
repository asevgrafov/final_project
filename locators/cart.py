from selenium.webdriver.common.by import By


class CartLocators:
    YOUR_CART = (By.XPATH, '//*[@class="subheader"]')
    CONTINUE_SHOPPING = (By.XPATH, '//*[@class="btn_secondary"]')
    CHECKOUT = (By.XPATH, '//*[@class="btn_action checkout_button"]')
    REMOVE = (By.XPATH, '//*[@class="btn_secondary cart_button"]')
    QUANTITY = (By.XPATH, '//*[@class="cart_quantity"]')
    ITEM_LABEL = (By.XPATH, '//*[@class="cart_item_label"]')
    ITEM_NAME = (By.XPATH, '//*[@class="inventory_item_name"]')
    ITEM_DESCRIPTION = (By.XPATH, '//*[@class="inventory_item_desc"]')
    ITEM_PRICE = (By.XPATH, '//*[@class="inventory_item_price"]')
