from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

NAME = (By.CSS_SELECTOR, "a.card-information__text.h4")
IMAGE = (By.CSS_SELECTOR, "lazy-image.image-animate.media.media--portrait")
PRICE = (By.CSS_SELECTOR, "div.price.price--on-sale")
@given('Open cureskin page')
def open_cureskin(context):
    context.driver.get('https://shop.cureskin.com/search?q=cure')


@then('Verify name, image and prices')
def verify_items(context):
    items = context.driver.find_elements(*NAME), context.driver.find_elements(*IMAGE), context.driver.find_elements(*PRICE)

    for i in range(len(items)):
        name_items = context.driver.find_elements(*NAME), context.driver.find_elements(*IMAGE), context.driver.find_elements(*PRICE)[i]
        search_items = name_items

        print((context.driver.find_elements(*NAME)), (context.driver.find_elements(*IMAGE)), (context.driver.find_elements(*PRICE)))
        assert search_items, f'Expected {search_items}, but got {name_items}'

sleep(4)