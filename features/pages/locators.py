
class HomePageLocators:
    MY_ACCOUNT_OPTION_BUTTON = ("//span[text()='My Account']", 'xpath')
    LOGIN_OPTION_LINK_TEXT = ("Login", 'link')
    SEARCH_BOX_FIELD = ('search', 'name')
    SEARCH_BUTTON = ('//div[@id="search"]//button', 'xpath')
    REGISTER_BUTTON = ('Register', 'link')

class LoginPageLocators:
    EMAIL_ADDRESS = ("input-email", 'id')
    PASSWORD_FIELD = ('input-password', 'id')
    LOGIN_BUTTON = ('//input[@value="Login"]', 'xpath')
    WARNING_MESSAGE = ('alert-danger', 'class')

class AsccountPageLocators:
    EDIT_ACCOUNT_INFORMATION_LINK_TEXT = ('Edit your account information', 'link')

class SearchPageLocators:
    VALID_PRODUCT = ('HP LP3065', 'link')
    MESSAGE_VALIDATION = ('//input[@id="button-search"]/following-sibling::p','xpath')

class RegisterPageLocators:
    INPUT_FIRST_NAME = ('input-firstname', 'id')
    INPUT_LAST_NAME = ('input-lastname', 'id')
    INPUT_EMAIL = ('input-email', 'id')
    INPUT_TELEPHONE = ('input-telephone', 'id')
    INPUT_PASSWORD = ('input-password', 'id')
    INPUT_CONFIRM_PASSWORD = ('input-confirm', 'id')
    PRIVACY_POLICY = ('agree', 'name')
    CONTINUE_BUTTON = ('//input[@value="Continue"]', 'xpath')
    RADIO_BUTTON_YES_OPTION = ('//input[@name="newsletter"][@value="1"]', 'xpath')
    DUPLICATE_EMAIL_WARNING = ('//div[@id="account-register"]/div', 'xpath')

class AccountSuccessPageLocators:
    ACCOUNT_SUCCESS_HEADING = ("//div[@id='content']/h1", 'xpath')
