from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    RESULT_TEXT = (By.XPATH, "//span[@class = 'a-color-state a-text")

    def verify_search_results(self):
        expected_results = '"table"'