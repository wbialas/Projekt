import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.relative_locator import locate_with

# DANE TESTOWEf8f
email = "test1@test.pl"
invalid_email = "test.pl"
password = "ABCabc123?"
invalid_password_short = "Abcd1@@"
invalid_password_nonumber = "Abcde###"
invalid_password_nolowercase = "ABCD111@"
invalid_password_nouppercase = "abcd111@"
invalid_password_nosign = "Abcd1234"


class NewUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.maxizoo.pl/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//button[@class="button button--secondary"][@type="button"]').click()
        self.driver.implicitly_wait(20)

    def testInvalidEmail(self):
        account_button = self.driver.find_element(By.XPATH, '//li[@class="item item--account"]')
        account_button.click()
        register_button = self.driver.find_element(By.XPATH, '//button[@data-id="panelRegistrationTeaser-register"]')
        register_button.click()
        email_input = self.driver.find_element(By.ID, 'register-userData-email')
        email_input.send_keys(invalid_email)
        password_input = self.driver.find_element(By.ID, 'register-userData-password')
        password_input.send_keys(password)
        checkbox = self.driver.find_element(By.XPATH, '//label[@class="checkbox"]')
        checkbox.click()
        register_account_btn = self.driver.find_element(By.XPATH, '//button[@data-id="register-userData-submit"]')
        register_account_btn.click()

        # 1. sprawdzenie, czy treść komunikatu się zgadza
        email_error = self.driver.find_element(By.XPATH, '//div[@class="em-content"]')
        self.assertEqual("Proszę podać prawidłowy adres e-mail.", email_error.text, "Błędny komuniukat")
        # 2. sprawdzenie, czy komunikat jest zlokalizowany pod polem tekstowym emaila
        error_locator = locate_with(By.XPATH, '//div[@class="em-content"]').below(email_input)
        error_location = self.driver.find_element(error_locator)
        self.assertEqual(email_error.id, error_location.id)
        sleep(2)

    def testInvalidPasswordShort(self):
        account_button = self.driver.find_element(By.XPATH, '//li[@class="item item--account"]')
        account_button.click()
        register_button = self.driver.find_element(By.XPATH, '//button[@data-id="panelRegistrationTeaser-register"]')
        register_button.click()
        email_input = self.driver.find_element(By.ID, 'register-userData-email')
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.ID, 'register-userData-password')
        password_input.send_keys(invalid_password_short)
        checkbox = self.driver.find_element(By.XPATH, '//label[@class="checkbox"]')
        checkbox.click()
        register_account_btn = self.driver.find_element(By.XPATH, '//button[@data-id="register-userData-submit"]')
        register_account_btn.click()

        # 1. sprawdzenie, czy treść komunikatu się zgadza
        password_error_short = self.driver.find_element(By.XPATH, '//div[@class="em-content"]')
        self.assertEqual("To pole musi zawierać co najmniej 8 znaków.", password_error_short.text, "Błędny komuniukat")
        # 2. sprawdzenie, czy komunikat jest zlokalizowany pod polem tekstowym hasła
        error_locator = locate_with(By.XPATH, '//div[@class="em-content"]').below(password_input)
        error_location = self.driver.find_element(error_locator)
        self.assertEqual(password_error_short.id, error_location.id)
        # 3. sprawdzenie, zaznaczenia poprawnych kryteriów pod polem hasła
        invalid = self.driver.find_element(By.XPATH, '//li[@class="vi-item"]')
        valid = self.driver.find_elements(By.XPATH, '//li[@class="vi-item vi-item--valid"]')
        # - weryfikacja, czy z 5 kryteriów, 4 są poprawne
        self.assertEqual(4, len(valid))
        # - weryfikacja, czy niespełnione kryterium jest niepoprawne
        self.assertEqual("Co najmniej 8 znaków", invalid.text, "Błąd")
        sleep(2)


    def tearDown(self):
        self.driver.quit()