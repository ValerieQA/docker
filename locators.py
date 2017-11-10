class HomePageLocators(object):
    BUTTON_LOG_IN = 'nw_login'
    BUTTON_SIGN_UP = "//button[text()='Sign Up']"
    FIELD_SEARCH = '//*[@placeholder = "Search"]'
    FIELD_IDENTIFIER = '//*[@placeholder = "Choose a Docker ID"]'
    FIELD_EMAIL = '//*[@placeholder = "Email address"]'
    FIELD_PASSWORD = '//*[@placeholder = "Choose a password"]'
    MESSAGE_SIGN_UP_SUCCESSFUL = "//p[text()='Please check your email to activate your account.']"
    MESSAGE_SIGN_UP_SUCCESSFUL_TEMPLATE = r"//p[text()='%s']"


class HomeUserPageLocators(object):
    MESSAGE_WELCOME_TO_DOCKER = "//h1[text()='Welcome to Docker Hub']"


class LogInPageLocators(object):
    FIELD_USER_NAME = 'nw_username'
    FIELD_PASSWORD = 'nw_password'
    BUTTON_SUBMIT = 'nw_submit'
    MESSAGE_UNSUCCESSFUL_LOGIN = "//div[text()='%s']"


class SearchResultsPageLocators(object):
    DROP_DOWN_LIST = "//*[@class='search-results-container']//select"
    LABEL_SORTED_RESULTS = '//*[@class = "undefined"]'
    RESULTS = 'left'
