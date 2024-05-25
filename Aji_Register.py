import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Demowebshop(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_register_success(self):
        browser = self.browser
        self.assertIn('',self.browser.title)
        self.browser.get('https://demowebshop.tricentis.com/')
        browser.find_element(By.CLASS_NAME, 'ico-register').click()
        browser.find_element(By.ID, 'gender-male').click()
        browser.find_element(By.NAME, 'FirstName').send_keys('Aji')
        browser.find_element(By.NAME, 'LastName').send_keys('Siregar')
        browser.find_element(By.NAME, 'Email').send_keys('ajiiregar@gmail.com')
        browser.find_element(By.NAME, 'Password').send_keys('qwerty123')
        browser.find_element(By.NAME, 'ConfirmPassword').send_keys('qwerty123')
        browser.find_element(By.ID, 'register-button').click()
 

if __name__ == '__main__':
    unittest.main()