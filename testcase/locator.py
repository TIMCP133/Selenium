from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")

class SearchResultsPageLocators(object):
    pass