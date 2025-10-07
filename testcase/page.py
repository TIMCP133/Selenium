from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"

class GoButtonElement(BasePageElement):
    locator = "go"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()
    go_button = GoButtonElement()
    
    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON) # *เอาค่าข้างใน tuple เช่น (1,2) จะได้ 1,2
        element.click()

class SearchResultsPage(BasePage):

    def is_results_found(self):
        # Probably should include some more validation
        return "No results found." not in self.driver.page_source
