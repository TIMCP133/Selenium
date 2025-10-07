import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
import re
import page

output = subprocess.run(
    ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--version"],
    capture_output=True,
    text=True
).stdout.strip()

version_match = re.search(r"(\d+\.\d+\.\d+)", output)  # first three numbers only
if version_match:
    chrome_version = version_match.group(1)
    print("✅ Detected Chrome version:", chrome_version)
else:
    raise Exception("❌ Could not detect Chrome version")


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("Setup")
        service = Service(ChromeDriverManager(driver_version=chrome_version).install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://www.python.org")

    # def test_example(self):
    #     print("Test")
    #     assert False

    def test_example(self):
        print("Test")
        assert True

    # def test_title(self):
    #     mainPage = page.MainPage(self.driver)
    #     assert mainPage.is_title_matches(), "title doesn't match"

    def not_a_test(self):
        print("this wont print")

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches(), "title doesn't match"
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), "No results found"


    def tearDown(self):
        #self.driver.close() 
        self.driver.quit()  # Proper cleanup - Better than .close() (closes browser + ends driver)

if __name__ == "__main__":
    unittest.main()