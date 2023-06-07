from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGiSTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main > .price_color")
    ITEM_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    ADDED_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    ADDED_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert-success")