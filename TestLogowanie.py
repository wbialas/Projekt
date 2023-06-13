import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.relative_locator import locate_with

# DANE TESTOWE
email = "ppx30611@student.wsb.poznan.pl"
invalid_email = "ppx30611@student.wsb.poznan.pln"
password = "Kontotest123!"


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.maxizoo.pl/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//button[@class="button button--secondary"][@type="button"]').click()
        self.driver.implicitly_wait(20)

    ### TEST LOGOWANIA DLA POPRAWNYCH DANYCH ###
    def testCorrectLogin(self):
        account_button = self.driver.find_element(By.XPATH, '//li[@class="item item--account"]')
        account_button.click()
        declick = self.driver.find_element(By.XPATH, '//div[@class="he-content"]')
        declick.click()
        email_input = self.driver.find_element(By.ID, 'login-email')
        email_input.click()
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.ID, 'login-password')
        password_input.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, '//button[@data-id="forms-login-button-submit"]')
        login_button.submit()
        sleep(4)

        # 1. Sprawdzenie poprawności adresu URL po zalogowaniu na konto
        URL = self.driver.current_url
        self.assertEqual("https://www.maxizoo.pl/my-account/", URL, "Wrong URL")
        sleep(2)

    ### TEST LOGOWANIA DLA BŁĘDNYCH DANYCH ###
    def testIncorrectLogin(self):
        account_button = self.driver.find_element(By.XPATH, '//li[@class="item item--account"]')
        account_button.click()
        declick = self.driver.find_element(By.XPATH, '//div[@class="he-content"]')
        declick.click()
        email_input = self.driver.find_element(By.ID, 'login-email')
        email_input.click()
        email_input.send_keys(invalid_email)
        password_input = self.driver.find_element(By.ID, 'login-password')
        password_input.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, '//button[@data-id="forms-login-button-submit"]')
        login_button.submit()
        sleep(4)

        # 1. Sprawdzenie poprawności adresu URL po zalogowaniu na konto
        URL = self.driver.current_url
        self.assertNotEqual("https://www.maxizoo.pl/my-account/", URL, "Wrong URL")
        # 2. Weryfikacja, czy treść komunikatu o błędzie jest poprawna
        error = self.driver.find_element(By.XPATH, '//div[@class="action-box action-box--error"]/div[2]')
        self.assertEqual("Adres e-mail lub hasło są nieprawidłowe. Proszę spróbować ponownie.", error.text, "Wrong information")
        # 3. Sprawdzenie, czy komunikat błędu znajduje się nad polem do wpisania adresu e-mail
        error_locator = locate_with(By.XPATH, '//div[@class="action-box action-box--error"]/div[2]').above(email_input)
        error_location = self.driver.find_element(error_locator)
        self.assertEqual(error.id, error_location.id)
        sleep(2)

    ### SPRAWDZENIE WIDOCZNOŚCI PODSTAWOWYCH ZAKŁADEK PO ZALOGOWANIU NA KONTO KLIENTA ###
    def testAccountTabsVisibility(self):
        account_button = self.driver.find_element(By.XPATH, '//li[@class="item item--account"]')
        account_button.click()
        declick = self.driver.find_element(By.XPATH, '//div[@class="he-content"]')
        declick.click()
        email_input = self.driver.find_element(By.ID, 'login-email')
        email_input.click()
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.ID, 'login-password')
        password_input.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, '//button[@data-id="forms-login-button-submit"]')
        login_button.click()

        # 1.Sprawdzenie, czy nagłówek powitalny się wyświetla
        self.driver.find_element(By.XPATH, '//div[@class="section-content"]/h1').is_displayed()
        # 2. Sprawdzenie, czy treść nagłówka powitalnego jest poprawna
        welcome_heading_text = self.driver.find_element(By.XPATH, '//div[@class="section-content"]/h1').get_attribute("innerHTML")
        self.assertIn("Dzień dobry ppx30611@student.wsb.poznan.pl,", welcome_heading_text,"Wrong header")
        # 3. Weryfikacja, czy widocznych jest 6 zakładek
        tabs = self.driver.find_elements(By.XPATH, '//a[@class="action-box action-box--clickable"]')
        self.assertEqual(6, len(tabs))
        # 4. Sprawdzenie czy poszczególne zakładki są widoczne
        self.driver.find_element(By.XPATH, '//a[@class="action-box action-box--clickable"]/div[2]/strong[contains(text(),"Moje zamówienia")]').is_displayed()
        self.driver.find_element(By.XPATH, '//a[@class="action-box action-box--clickable"]/div[2]/strong[contains(text(),"Moje zwierzęta")]').is_displayed()
        self.driver.find_element(By.XPATH, '//a[@class="action-box action-box--clickable"]/div[2]/strong[contains(text(),"Mój Friends rabat")]').is_displayed()
        self.driver.find_element(By.XPATH, '//a[@class="action-box action-box--clickable"]/div[2]/strong[contains(text(),"PAYBACK")]').is_displayed()
        self.driver.find_element(By.XPATH, '//a[@class="action-box action-box--clickable"]/div[2]/strong[contains(text(),"Moje dane")]').is_displayed()
        self.driver.find_element(By.XPATH, '//a[@class="action-box action-box--clickable"]/div[2]/strong[contains(text(),"Wsparcie & FAQ")]').is_displayed()
        sleep(2)

    def tearDown(self):
        self.driver.quit()
