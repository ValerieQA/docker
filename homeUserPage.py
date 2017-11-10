from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import constants
import locators


class HomeUserPage(object):
    def __init__(self, driver):
        self.driver = driver
        while self.driver.execute_script('return document.readyState;') != 'complete':
            pass
        WebDriverWait(self.driver, 20).until(expected_conditions.title_is(constants.HomeUserPageConstants.TITLE))

    def is_successful_log_in_message_shown(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (By.XPATH, locators.HomeUserPageLocators.MESSAGE_WELCOME_TO_DOCKER)))
        return self.driver.find_element_by_xpath(locators.HomeUserPageLocators.MESSAGE_WELCOME_TO_DOCKER)
