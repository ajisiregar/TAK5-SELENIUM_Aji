import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class Demowebshop(unittest.TestCase):

    def setUp(self):
        # Create an instance of ChromeOptions
        chrome_options = Options()

        # If Chrome is installed in a non-default location, specify the path to the browser
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Adjust this path if necessary

        # Create a Service object for the chromedriver
        service = Service(ChromeDriverManager().install())

        # Initialize WebDriver (Make sure the WebDriver is installed and added to PATH)
        self.browser = webdriver.Chrome(service=service, options=chrome_options)
        # Specify path if necessary
        self.browser.maximize_window()

    def test_locked_user(self):
        browser = self.browser
        self.browser.get('https://www.saucedemo.com/')
        browser.find_element(By.ID, 'user-name').send_keys('locked_out_user')
        browser.find_element(By.ID, 'password').send_keys('secret_sauce')
        browser.find_element(By.ID, 'login-button').click()

if __name__ == '__main__':
    unittest.main()