from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRIV_NOTE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")


@given('Open Amazon {T_C_page} page')
def open_term_page(context, T_C_page):
    context.driver.get(f'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original:', context.original_window)
    print('All windows:', context.driver.window_handles)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.find_element(*PRIV_NOTE).click()

@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    print('After window opened, all windows:', all_windows)
    context.driver.switch_to.window(all_windows[1])

@then('Verify Amazon Privacy Notice page is opened')
def verify_notice_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))


@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.close()
    all_windows = context.driver.window_handles
    print('After window closed, all windows:', all_windows)
    context.driver.switch_to.window(context.original_window)

