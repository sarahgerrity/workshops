from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SearchResultComp(BasePage):
    DETAILS_LINK = (By.CSS_SELECTOR, "button[class*='show-details']")
    BOOK_NOW_BUTTON = (By.CSS_SELECTOR, "a[class*='SpotListItemRow-book-it']")
    PRICE = (By.CLASS_NAME, "price")

    def __init__(self, driver, row_selector):
        super().__init__(driver)
        self.main_body = self.get_element_with_wait(row_selector)

    def click_details_link(self):
        self.get_element_with_wait(self.DETAILS_LINK, self.main_body).click()
        # Map gets replaced with a details ?modal?

    def click_book_now(self):
        self.get_element_with_wait(self.BOOK_NOW_BUTTON, self.main_body).click()
        # Will return checkout page

    def get_price(self):
        return self.get_element_with_wait(self.PRICE, self.main_body).text



