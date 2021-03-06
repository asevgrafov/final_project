from selenium.webdriver.common.by import By


class OverviewPageLocators:
    SUBHEADER = (By.XPATH, '//*[@class="subheader"]')
    ITEM_NAME = (By.XPATH, '//*[@class="inventory_item_name"]')
    ITEM_DESCRIPTION = (By.XPATH, '//*[@class="inventory_item_desc"]')
    ITEM_PRICE = (By.XPATH, '//*[@class="inventory_item_price"]')
    PAYMENT_INFO = (By.XPATH, '//*[@class="summary_value_label"]')
    SHIPPING_INFO = (By.XPATH, '//*[@class="summary_value_label"]')
    FINISH = (By.XPATH, '//*[@class="btn_action cart_button"]')
    CANCEL = (By.XPATH, '//*[@class="cart_cancel_link btn_secondary"]')
    ITEM_TOTAL = (By.XPATH, '//*[@class="summary_subtotal_label"]')
    TAX = (By.XPATH, '//*[@class="summary_tax_label"]')
    TOTAL = (By.XPATH, '//*[@class="summary_total_label"]')
