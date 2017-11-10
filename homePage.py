from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

import constants
import logInPage
import locators
import searchResultsPage


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        while self.driver.execute_script('return document.readyState;') != 'complete':
            pass
        WebDriverWait(self.driver, 20).until(expected_conditions.title_is(constants.HomePageConstants.TITLE))
    
    def click_log_in_button(self):
        login_button = self.driver.find_element_by_id(locators.HomePageLocators.BUTTON_LOG_IN)
        login_button.click()
        WebDriverWait(self.driver, 20).until_not(expected_conditions.visibility_of_element_located(
            (By.ID, locators.HomePageLocators.BUTTON_LOG_IN)))
        return logInPage.LogInPage(self.driver)

    def set_search_phrase(self, search_phrase):
        # find search field
        search_field = self.driver.find_element_by_xpath(locators.HomePageLocators.FIELD_SEARCH)
        # type search phrase
        search_field.send_keys(search_phrase)

    def submit_search(self):
        # find search field
        search_field = self.driver.find_element_by_xpath(locators.HomePageLocators.FIELD_SEARCH)
        # press Enter button
        search_field.send_keys(Keys.RETURN)
        return searchResultsPage.SearchResultsPage(self.driver)

    def set_sign_up_identifier(self, identifier):
        identifier_field = self.driver.find_element_by_xpath(locators.HomePageLocators.FIELD_IDENTIFIER)
        identifier_field.send_keys(identifier)

    def set_sign_up_email(self, email):
        email_field = self.driver.find_element_by_xpath(locators.HomePageLocators.FIELD_EMAIL)
        email_field.send_keys(email)

    def set_sign_up_password(self, password):
        password_field = self.driver.find_element_by_xpath(locators.HomePageLocators.FIELD_PASSWORD)
        password_field.send_keys(password)

    def click_sign_up_button(self):
        sign_up_button = self.driver.find_element_by_xpath(locators.HomePageLocators.BUTTON_SIGN_UP)
        sign_up_button.click()

    def is_successful_sign_up_message_shown(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.HomePageLocators.MESSAGE_SIGN_UP_SUCCESSFUL)))
        return self.driver.find_element_by_xpath(locators.HomePageLocators.MESSAGE_SIGN_UP_SUCCESSFUL)
