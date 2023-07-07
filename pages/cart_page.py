from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class CartPage(Page):
    CART_EMPTY = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')

    def verify_cart(self):
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/cart/'))
        self.verify_element_text('Your Amazon Cart is empty', *self.CART_EMPTY)