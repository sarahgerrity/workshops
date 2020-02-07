import os
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from utils.exceptions import InputMismatchError, PageInitError


class BasePage:
    PULSE_LOADER = (By.CLASS_NAME, 'SHLoader-loader')

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self):
        """
        Directs browser to page using page object's PAGE_URI
        :param driver: Selenium webdriver
        :type driver: WebDriver
        :return: None
        """
        self.driver.get(os.environ['HOST'] + self.PAGE_URI)
        return self

    def wait_for_page_title_to_contain(self, expected_title):
        """
        Asserts page title contains expected text.
        :param expected_title: Text to assert exists in the page title
        :type expected_title: String
        :return: None
        """
        try:
            WebDriverWait(self.driver, 20).until(EC.title_contains(expected_title))
        except TimeoutException:
            raise PageInitError(f'The page title did not contain {expected_title}')
        return self

    def wait_for_url_to_contain(self, expected_path):
        """
        Asserts the URL contains expected value.
        :param expected_path: Text to assert exists in URL
        :type expected_path: String
        :return: None
        """
        try:
            WebDriverWait(self.driver, 20).until(EC.url_contains(expected_path))
        except TimeoutException:
            raise PageInitError(f'The url did not contain {expected_path}')
        return self

    def get_element_with_wait(self, selector, parent_element=None):
        """
        Gets element after waiting for for it to become visible.
        :param selector: Find by type and find by value
        :type selector: Tuple
        :param parent_element: Element to search in, defaults to entire DOM
        :type parent_element: WebElement
        :return: WebElement which is visible and matches the selector
        :rtype: WebElement
        """
        if not parent_element:
            parent_element = self.driver
        return WebDriverWait(parent_element, 10).until(EC.visibility_of_element_located(selector))

    def get_elements_with_wait(self, selector, parent_element=None):
        """
        Gets elements after waiting for all matching elements to be visible.
        :param selector: Find by type and find by value
        :type selector: Tuple
        :param parent_element: Element to search in, defaults to entire DOM
        :return: All visible web elements that match your selector
        :rtype: List of WebElements
        """
        if not parent_element:
            parent_element = self.driver
        return WebDriverWait(parent_element, 10).until(EC.visibility_of_all_elements_located(selector))

    def get_select(self, select_element, parent_element=None):
        """
        Return the select object found by select_element
        :param select_element: Select element
        :type select_element: WebElement
        :param parent_element: Element to search in, defaults to entire DOM
        :type parent_element: WebElement
        :return: Select object
        :rtype: Select
        """
        if not parent_element:
            parent_element = self.driver
        return Select(WebDriverWait(parent_element, 10).until(EC.element_to_be_clickable(select_element)))

    def wait_for_elements(self, selector):
        """
        Wait until elements are visible before continuing.
        :param selector: Find by type and find by value
        :type selector: Tuple
        :return: None
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(selector))

    def wait_for_element_to_exist(self, selector, timeout=10, swallow_timeout=False):
        """
        Warning: slow method - Only use this method when necessary!
        Waits until an element exists
        :param timeout: Number of seconds to wait before returning False
        :type timeout: Integer
        :param selector: Find by type and find by value
        :type selector: Tuple
        :param swallow_timeout: Swallows TimeoutException and returns False
        :type swallow_timeout: Boolean
        :return: True if element exists before timeout is hit
        :rtype: Boolean
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(selector))
            return True
        except TimeoutException:
            if swallow_timeout:
                return False
            else:
                raise

    def wait_for_url_to_change(self):
        WebDriverWait(self.driver, 10).until(EC.url_changes)

    def wait_for_element_to_stop_existing(self, selector):
        """
        Waits for an element to stop existing or become invisible.
        :param selector: Find by type and find by value
        :type selector: Tuple
        :return: None
        """
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(selector))

    def wait_for_element_and_click2(self, selector, parent_element=None, timeout=10):
        if not parent_element:
            parent_element = self.driver
        if bool(os.environ.get('MOBILE', False)):
            action = TouchActions(self.driver)
            action.tap(self.get_element_with_wait(selector, parent_element)).perform()
        else:
            WebDriverWait(parent_element, timeout).until(EC.element_to_be_clickable(selector)).click()

    def wait_for_element_and_click(self, selector, parent_element=None, timeout=10, shift_retries=0, intercept_retries=0):
        """
        Waits for element to be clickable then clicks it
        :param timeout: timeout value
        :param parent_element: Element to search in, defaults to entire DOM
        :param selector: Find by type and find by value
        :type selector: Tuple
        :param shift_retries: Number of current retries for non-equal captures
        :type shift_retries: Integer
        :param intercept_retries: Number of current retries for click intercepts exceptions
        :type intercept_retries: Integer
        :return: None
        """
        if not parent_element:
            parent_element = self.driver
        while True:
            try:
                capture1 = WebDriverWait(parent_element, timeout).until(EC.element_to_be_clickable(selector))
                # Explicit sleep to allow elements to shift if they are still reprocessing
                time.sleep(0.25)
                capture2 = WebDriverWait(parent_element, timeout).until(EC.element_to_be_clickable(selector))
                if capture1 == capture2:
                    capture1.click()
                    break
                else:
                    if shift_retries >= 10:
                        raise Exception('Elements shifted too many times')
                    else:
                        print(f"Elements have shifted!  Retrying attempt: {shift_retries}")
                        self.wait_for_element_and_click(selector, parent_element, shift_retries+1, intercept_retries)
            except ElementClickInterceptedException:
                if intercept_retries >= 5:
                    raise
                else:
                    print(f"Click intercept happened!  Retrying attempt: {intercept_retries}")
                    self.wait_for_element_and_click(selector, parent_element, shift_retries, intercept_retries + 1)

    def element_exists(self, selector):
        """
        Determines if element exists with no wait.
        :param selector: Find by type and find by value
        :type selector: Tuple
        :return: True if element exists
        :rtype: Boolean
        """
        try:
            self.driver.find_element(*selector)
        except NoSuchElementException:
            return False
        return True

    def format_partial_selector(self, selector, *args):
        """
        Use this to format selector values that have a partial values (placeholders).
        :param selector: Find by type and find by value
        :type selector: Tuple
        :param args: Arguments to use for string formatting
        :type args: Collection
        :return: Find by type and find by value
        :rtype: Tuple
        """
        return (selector[0], selector[1].format(*args))

    def switch_to_window_by_index(self, window_index):
        """
        Switch the window by the index of the window_handles
        :param window_index: window_handle index
        :type: Integer
        :return: None
        """
        self.driver.switch_to.window(self.driver.window_handles[window_index])
        return self

    def switch_to_active_window(self):
        """
        Switches to the last window opened
        :return: None
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self

    def append_text(self, text_input_selector, text_value, validate_input=True):
        """
        Appends a string to the input field value and ensures it is entered.
        :param validate_input: Boolean used when we don't want to validate the field.
        iframe with multiple fields such as credit card info
        :param text_input_selector: Selector for the text input
        :type text_input_selector: Tuple of the selector
        :param text_value: String that is entered in the text input
        :type text_value: String
        :return: None
        """
        text_input = self.get_element_with_wait(text_input_selector)
        text_input.send_keys(text_value)
        if validate_input and text_value not in text_input.get_attribute("value"):
            raise InputMismatchError("The value added to the input is not in the element's value attribute")

    def enter_text(self, text_input_selector, text_value, validate_input=True):
        """
        Clears the input field and enters a string ensuring it was successfully entered.
        :param validate_input: Boolean used when we don't want to validate the field
        iframe with multiple fields such as credit card info
        :param text_input_selector: Selector for the text input
        :type text_input_selector: Tuple of the selector
        :param text_value: String value to enter in the input
        :type text_value: String
        :return: None
        """
        text_input = self.get_element_with_wait(text_input_selector)
        text_input.clear()
        text_input.send_keys(text_value)
        if validate_input and text_input.get_attribute("value") != text_value:
            raise InputMismatchError("The value sent to the input does not match the element's value attribute")