from selenium.webdriver.common.by import By


class MainFooterLocators:
    TWITTER = (By.XPATH, '//*[@class="social_twitter"]')
    FACEBOOK = (By.XPATH, '//*[@class="social_facebook"]')
    LINKEDIN = (By.XPATH, '//*[@class="social_linkedin"]')
    FOOTER_COPY = (By.XPATH, '//*[@class="footer_copy"]')
