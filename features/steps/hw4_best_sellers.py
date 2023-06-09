from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Bestsellers page')
def open_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers/')


@then('Verify 5 Bestseller links')
def verify_bs_links(context):
    links_count = len(context.driver.find_elements(By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a")) #will count the 5 links
    print(context.driver.find_elements(By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a"))
    assert links_count == 5, f'Expected 5 links but got {links_count} links'

sleep(4)