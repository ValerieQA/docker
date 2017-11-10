from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import homeUserPage
import locators
import constants


class LogInPage(object):
    def __init__(self, driver):
        self.driver = driver
        while self.driver.execute_script('return document.readyState;') != 'complete':
            pass
        WebDriverWait(self.driver, 20).until(expected_conditions.title_is(constants.LogInPageConstants.TITLE))

    def set_log_in_identifier(self, identifier):
        identifier_field = self.driver.find_element_by_id(locators.LogInPageLocators.FIELD_USER_NAME)
        identifier_field.send_keys(identifier)

    def set_log_in_password(self, password):
        password_field = self.driver.find_element_by_id(locators.LogInPageLocators.FIELD_PASSWORD)
        password_field.send_keys(password)

    def click_log_in_button(self):
        login_button = self.driver.find_element_by_id(locators.LogInPageLocators.BUTTON_SUBMIT)
        login_button.click()
        WebDriverWait(self.driver, 20).until_not(expected_conditions.visibility_of_element_located(
            (By.ID, locators.LogInPageLocators.BUTTON_SUBMIT)))
        return homeUserPage.HomeUserPage(self.driver)

    def click_log_in_button_expecting_failure(self):
        login_button = self.driver.find_element_by_id(locators.LogInPageLocators.BUTTON_SUBMIT)
        login_button.click()
        text_message = constants.LogInPageConstants.TEXT_MESSAGE_UNSUCCESSFUL_LOGIN
        text_message_locator = locators.LogInPageLocators.MESSAGE_UNSUCCESSFUL_LOGIN % text_message
        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, text_message_locator)))
        return self.driver.find_element_by_xpath(text_message_locator).text
