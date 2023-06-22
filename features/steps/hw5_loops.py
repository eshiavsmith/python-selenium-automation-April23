from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, ".a-unordered-list.a-nostyle.a-button-list.a-declarative li")
CURRENT_COLOR = (By.CSS_SELECTOR, ".a-row .selection")


@given('Open Amazon {products_page} page')
def open_product_page(context, products_page):
    context.driver.get(f'https://www.amazon.com/gp/product/{products_page}')


@then('Verify user can click through')
def verify_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    expected_colors = ['Black', 'Blue Over Dye', 'Dark Blue Vintage', 'Dark Indigo', 'Dark Wash']

    actual_colors = []
    for color_options in colors[:5]:
        color_options.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color: ', current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'