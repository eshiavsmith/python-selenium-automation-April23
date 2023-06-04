from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)


# init (opens) driver
driver = webdriver.Chrome(service=service)


# maximize the window size
driver.maximize_window()


# open the url
# driver.get('https://www.google.com/')


# Selenium command to open the url
driver.get('https://www.amazon.com/')

# Find amazon logo (tag.class)
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Find Create account name (tag.class)
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Find You name (tag#id)
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')

# Find Email (tag#id)
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')

# Find Password field (tag#id)
driver.find_element(By.CSS_SELECTOR, 'input#ap_password')

# Find Password text (tag[attribute=value])
driver.find_element(By.CSS_SELECTOR, 'div.a-alert-inline-info')

# Find Re-enter Password (tag#id)
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')

# Finds continue button (tag#id)
driver.find_element(By.CSS_SELECTOR, 'input#continue')

# Finds contiue of use (tag[attribute=value])
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use?ie']")

# Finds Privacy Notice (tag[attribute=value])
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice?ie']")

# Finds Privacy Notice (tag.class)
driver.find_element(By.CSS_SELECTOR, "a[href*='ap/signin?openid']")
