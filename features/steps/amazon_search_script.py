from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#
# @given('Open Amazon page')
# #def open_amazon(context):
#  #   context.driver.get('http://www.amazon.com/')
#
# AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# CLICK_SEARCH_OPTION = (By.ID, 'nav-search-submit-button')
#
# #@when('Input text coffee')
# # @when('Input text {search_word}')
# # def input_search_word(context, search_word):
# #     #context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
# #     context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)
# @when('Click on search button')
# def click_search(context):
#     context.driver.find_element(CLICK_SEARCH_OPTION).click()
#
# #@then('Verify that text "coffee" is shown')
# #@then('Verify that text {expected_result} is shown')
#
#
# driver.quit()
