from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.search_result_comp import SearchResultComp


class SearchResultsPage(BasePage):
    SEARCH_RESULT_ROW = (By.XPATH, "(//div[contains(@class,'SpotListItemRow')])[{}]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_search_result(self, result_index):
        row_selector = self.format_partial_selector(self.SEARCH_RESULT_ROW, result_index)
        row_element = self.get_element_with_wait(row_selector)
        return SearchResultComp(self.driver, row_element)


