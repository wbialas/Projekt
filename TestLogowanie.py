import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# DANE TESTOWE
username = "Wojtekb321"
invalid_username = "wb"
email = "test1@test.pl"
invalid_email = "test.pl"
password = "ABCabc123"
invalid_password = "abcdabcd"


class RejestracjaNowegoUzytkownika(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.filmweb.pl")
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element(By.ID, 'didomi-notice-agree-button').click()
        self.driver.implicitly_wait(20)

    ### Test z błędną nazwą użytkownika ###
    def testInvalidUsername(self):

        login_button = self.driver.find_element(By.ID, 'main-header_login-link')
        login_button.click()
        create_account_btn = self.driver.find_element(By.XPATH,'//div[contains(@class,"authButton--register")]')
        create_account_btn.click()
        username_input = self.driver.find_element(By.XPATH, '//input[@name="name"]')
        username_input.send_keys(invalid_username)
        email_input = self.driver.find_element(By.XPATH, '//input[@class="materialForm__input "]')
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        password_input.send_keys(password)
        sleep(2)
        register_button = self.driver.find_element(By.XPATH,'//div[@class="authPage__button authButton authButton--complate-registration authButton--next"]')
        register_button.click()
        sleep(2)

        if register_button.is_enabled():
            print('OK')
        else:
            print('FAIL')

    ### Test z błędnym adresem email ###
    def testInvalidEmail(self):

        login_button = self.driver.find_element(By.ID, 'main-header_login-link')
        login_button.click()
        create_account_btn = self.driver.find_element(By.XPATH,'//div[contains(@class,"authButton--register")]')
        create_account_btn.click()
        username_input = self.driver.find_element(By.XPATH, '//input[@name="name"]')
        username_input.send_keys(username)
        email_input = self.driver.find_element(By.XPATH, '//input[@class="materialForm__input "]')
        email_input.send_keys(invalid_email)
        password_input = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        password_input.send_keys(password)
        sleep(2)
        register_button = self.driver.find_element(By.XPATH,'//div[@class="authPage__button authButton authButton--complate-registration authButton--next"]')
        register_button.click()
        sleep(2)

        if register_button.is_enabled():
            print('OK')
        else:
            print('FAIL')

    ### Test z błędnym hasłem ###
    def testInvalidPassword(self):

        login_button = self.driver.find_element(By.ID, 'main-header_login-link')
        login_button.click()
        create_account_btn = self.driver.find_element(By.XPATH,'//div[contains(@class,"authButton--register")]')
        create_account_btn.click()
        username_input = self.driver.find_element(By.XPATH, '//input[@name="name"]')
        username_input.send_keys(username)
        email_input = self.driver.find_element(By.XPATH, '//input[@class="materialForm__input "]')
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        password_input.send_keys(invalid_password)
        sleep(2)
        register_button = self.driver.find_element(By.XPATH,'//div[@class="authPage__button authButton authButton--complate-registration authButton--next"]')
        register_button.click()
        sleep(2)

        if register_button.is_enabled():
            print('OK')
        else:
            print('FAIL')

    def tearDown(self):
        self.driver.quit()