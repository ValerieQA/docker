from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import locators
import constants


class SearchResultsPage(object):
    def __init__(self, driver):
        self.driver = driver
        while self.driver.execute_script('return document.readyState;') != 'complete':
            pass
        WebDriverWait(self.driver, 20).until(expected_conditions.title_is(constants.SearchResultsPageConstants.TITLE))

    def get_search_results(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, locators.SearchResultsPageLocators.RESULTS)))
        return self.driver.find_element_by_class_name(locators.SearchResultsPageLocators.RESULTS).text

    def set_filter(self, filter_name):
        # select drop down list
        select = Select(self.driver.find_element_by_xpath(locators.SearchResultsPageLocators.DROP_DOWN_LIST))
        # select item by word/text
        select.select_by_visible_text(filter_name)
        # find sorted result
        locator = locators.SearchResultsPageLocators.LABEL_SORTED_RESULTS
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, locator)))
        return self.driver.find_element_by_xpath(locator).text
