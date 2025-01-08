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

    def test_Cartcheckout_success(self):
        browser = self.browser
       
        # Open the website
        browser.get('https://www.saucedemo.com/')
        
        # Wait for the page to load and verify the title
        WebDriverWait(browser, 10).until(EC.title_contains('Swag Labs'))
        self.assertIn('Swag Labs', browser.title)
        
        # Login
        browser.find_element(By.ID, 'user-name').click()
        #WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'Email')))
        browser.find_element(By.ID, 'user-name').send_keys('problem_user')
        browser.find_element(By.ID, 'password').send_keys('secret_sauce')
        browser.find_element(By.ID, 'login-button').click()
        

        # Wait for login to complete and verify
        # WebDriverWait(browser, 10).until(EC.title_contains('Swag Labs'))
        # self.assertIn('Swag Labs', browser.title)

        #Click add cart and put it on cart
        browser.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
        
        # Go to Cart and proceed to Checkout
        #WebDriverWait(browser, 10).until(EC.title_contains('All Items'))
        browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        browser.find_element(By.ID, 'checkout').click()

        # Checkout selected items
        browser.find_element(By.ID, 'first-name').click()
        browser.find_element(By.ID, 'first-name').send_keys('Aji')
        browser.find_element(By.ID, 'last-name').click()
        browser.find_element(By.ID, 'last-name').send_keys('Siregar')
        browser.find_element(By.ID, 'postal-code').click()
        browser.find_element(By.ID, 'postal-code').send_keys('16433')
        browser.find_element(By.ID, 'continue').click()

        # Check Error Message
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Error: Last Name is required')))


        # Invoice of Purchasing
        #browser.find_element(By.ID, 'finish').click()

        # Verify Notification
        #WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'checkout_complete_container')))


        #link_element = browser.find_element(By.XPATH, "//a[@href]")
        #href_value = link_element.get_attribute('href')
        #WebDriverWait(browser, 10).until(EC.title_contains('All Items'))

        # You can add assertions or further checks here, e.g., verify the checkout page title

    #def tearDown(self):
        # Clean up and close the browser
       # self.browser.quit()

if __name__ == '__main__':
    unittest.main()