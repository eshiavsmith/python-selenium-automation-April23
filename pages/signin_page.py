from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class SignInPage(Page):
    SEARCH_SIGNIN = (By.XPATH, "//h1[@class='a-spacing-small']")
    SEARCH_EMAIL = (By.ID, 'ap_email')
    def verify_signin(self):
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
        self.verify_element_text('Sign in', *self.SEARCH_SIGNIN)
        self.find_element(*self.SEARCH_EMAIL)