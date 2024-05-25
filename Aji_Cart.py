import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Demowebshop(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_Cartcheckout_success(self):
        browser = self.browser
        self.assertIn('',self.browser.title)
        self.browser.get('https://demowebshop.tricentis.com/')
        browser.find_element(By.CLASS_NAME, 'ico-login').click()
        browser.find_element(By.NAME, 'Email').send_keys('ajiiregar@gmail.com')
        browser.find_element(By.NAME, 'Password').send_keys('qwerty123')
        browser.find_element(By.CLASS_NAME, 'button-1.login-button').click()
        browser.find_element(By.CLASS_NAME, 'cart-label').click()
        browser.find_element(By.CLASS_NAME, 'button-1.checkout-button').click()


if __name__ == '__main__':
    unittest.main()