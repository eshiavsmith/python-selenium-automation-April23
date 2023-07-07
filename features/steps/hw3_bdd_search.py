from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

# SEARCH_SIGNIN = (By.XPATH, "//h1[@class='a-spacing-small']")
# SEARCH_EMAIL = (By.ID, 'ap_email')
@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    # aggregate this function to the application in pages
    context.app.main_page.open_main_page()

@when('Click Orders button')
def click_orders(context):
    # context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
    context.app.header_page.click_orders()


@then('Verify Sign-In Page opened')
def verify_signin(context):
    # expected_results = "Sign in"
    # actual_results = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    # assert actual_results == expected_results, f'Expected {actual_results}'
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
    #reference the application in Pages
    context.app.signin_page.verify_signin()

    # context.driver.find_element(*SEARCH_EMAIL)

@when('Click Cart button')
def click_cart(context):
    # context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite').click()
    context.app.header_page.click_cart()
@then('Verify Amazon Cart Empty')
def verify_cart(context):
    # expected_cart = "Your Amazon Cart is empty"
    # cart_results = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']").text
    # assert expected_cart == cart_results, f'Expected {expected_cart} but got actual {cart_results}'
    context.app.cart_page.verify_cart()
