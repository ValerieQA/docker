from selenium import webdriver
import unittest
import time
import homePage
import constants
import testdata


class HubDockerHomePageTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(constants.HomePageConstants.URL_HOMEPAGE)

    def tearDown(self):
        self.driver.quit()

    def test_sign_up(self):
        home_page = homePage.HomePage(self.driver)
        # define unique user identifier
        identifier = str(time.time()).replace('.', '')
        # set user identifier in the field
        home_page.set_sign_up_identifier(identifier)
        # define email basing on identifier
        email = identifier + testdata.HomePageTestData.EMAIL_DOMAIN
        # set user email in the field
        home_page.set_sign_up_email(email)
        # define password
        password = testdata.HomePageTestData.USER_PASSWORD
        # set user password in the field
        home_page.set_sign_up_password(password)
        # click Sign Up button
        home_page.click_sign_up_button()
        # verify successful sign up message
        assert home_page.is_successful_sign_up_message_shown()

    def test_search_in_hub_docker(self):
        home_page = homePage.HomePage(self.driver)
        home_page.set_search_phrase(testdata.HomePageTestData.SEARCH_WORD)
        search_results_page = home_page.submit_search()
        assert constants.SearchResultsPageConstants.TEXT_SEARCH_RESULT in search_results_page.get_search_results()
        print "Search results equal to: " + search_results_page.get_search_results()

    def test_search_filter(self):
        home_page = homePage.HomePage(self.driver)
        filter_name = testdata.HomePageTestData.FILTER_WORD
        home_page.set_search_phrase(testdata.HomePageTestData.SEARCH_WORD)
        search_results_page = home_page.submit_search()
        filter_result = search_results_page.set_filter(filter_name)
        assert constants.SearchResultsPageConstants.TEXT_SEARCH_FILTER_RESULT in filter_result
        assert constants.SearchResultsPageConstants.TEXT_SEARCH_RESULT in search_results_page.get_search_results()
        print "Search results equal to: " + search_results_page.get_search_results()


class LoginPageTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(constants.HomePageConstants.URL_HOMEPAGE)

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        home_page = homePage.HomePage(self.driver)
        # open log in page
        log_in_page = home_page.click_log_in_button()
        # define identifier
        identifier = testdata.LogInPageTestData.IDENTIFIER_VALID
        # set user identifier
        log_in_page.set_log_in_identifier(identifier)
        # define password
        password = testdata.LogInPageTestData.USER_PASSWORD
        # set user password
        log_in_page.set_log_in_password(password)
        # submit login
        home_user_page = log_in_page.click_log_in_button()
        assert home_user_page.is_successful_log_in_message_shown()
        print "You are logged in"

    def test_unsuccessful_login(self):
        home_page = homePage.HomePage(self.driver)
        # open log in page
        log_in_page = home_page.click_log_in_button()
        # define identifier
        identifier = testdata.LogInPageTestData.IDENTIFIER_INVALID
        # set user identifier
        log_in_page.set_log_in_identifier(identifier)
        # define password
        password = testdata.LogInPageTestData.USER_PASSWORD
        # set user password
        log_in_page.set_log_in_password(password)
        # submit login
        home_user_page = log_in_page.click_log_in_button_expecting_failure()
        assert home_user_page == constants.LogInPageConstants.TEXT_MESSAGE_UNSUCCESSFUL_LOGIN
        print "You are NOT logged in"

homepage = HubDockerHomePageTestCases
loginpage = LoginPageTestCases

if __name__ == "__main__":
    unittest.main()


