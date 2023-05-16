from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Maximizes the window when open
driver.maximize_window()

# Selenium command to open the url
driver.get('https://www.amazon.com/')

# Finds order link and clicks
driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()

# Looks for Sign in
expected_result = 'Sign in'

# Verifies header is visible.  Find element in the path using XPath
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
print(actual_result, 'header is Visible')

# Verify the expected result with the actual
assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'

sleep(4)
# Verify email was present
email_present = driver.find_element(By.ID, "ap_email")
print(email_present.is_displayed(), 'Email field is Present')

driver.quit()