from pages.base_page import Page
from selenium.webdriver.common.by import By

class HeaderPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.CSS_SELECTOR, 'a#nav-orders')
    CART_BTN = (By.CSS_SELECTOR, 'a#nav-cart')
    # def search_for_product(self):
    #     self.input_text('table', *self.SEARCH_FIELD)
    #     self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_cart(self):
        self.click(*self.CART_BTN)