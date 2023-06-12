import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# DANE TESTOWE
text = "karma"
text2 = "internet"

class SearchFunction(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.maxizoo.pl/")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//button[@class="button button--secondary"][@type="button"]').click()
        self.driver.implicitly_wait(20)

    ### WYSZUKIWANIE Z POWODZENIEM ###
    def testSearchingByText(self):

        search_button = self.driver.find_element(By.ID, 'formSearch-input')
        search_button.send_keys(text)
        search_button.send_keys(Keys.ENTER)
        sleep(2)

        # 1. Sprawdzenie, czy następuje przekierowanie na poprawny adres URL
        if self.driver.current_url == "https://www.maxizoo.pl/search/?text=karma":
            print("Correct URL")
        else:
            print("Wrong URL")
        # 2. Weryfikacja, czy wyświetla się lista wyników
        try:
            self.driver.find_element(By.XPATH, '//div[@class="grid-container product-grid"]')
        except NoSuchElementException:
            self.driver.get_screenshot_as_file("no_results.png")
        # 3. Sprawdzenie, czy widnieje 48 wyników składających się z grafiki, opisu i dodatkowej treści
        results_image = self.driver.find_elements(By.XPATH, '//div[@class="pt-figure"]')
        self.assertEqual(48, len(results_image))
        results_desc = self.driver.find_elements(By.XPATH, '//div[@class="pt-content"]')
        self.assertEqual(48, len(results_desc))
        results_add = self.driver.find_elements(By.XPATH, '//div[@class="pt-footer"]')
        self.assertEqual(48, len(results_add))
        sleep(2)

    ### WYSZUKIWANIE BEZ POWODZENIA ###
    def testSearchFail(self):

            search_button = self.driver.find_element(By.ID, 'formSearch-input')
            search_button.send_keys(text2)
            search_button.send_keys(Keys.ENTER)
            sleep(2)

            # 1. Sprawdzenie, czy wyświetla się grafika
            self.driver.find_element(By.XPATH, '//div[@class="grid-item grid-item--12 grid-item--m--6"]/div/img').is_displayed()
            # 2. Sprawdzenie, czy wyświetla się komunikat o braku wyników, ze wskazaniem wpisanej frazy
            self.driver.find_element(By.XPATH, '//p[text()="Niestety nie udało się znaleźć produktów dla zapytania "]').is_displayed()
            no_results_error = self.driver.find_element(By.XPATH, '//div[@class="grid-item grid-item--12 grid-item--m--6"]/div/div/div[2]/p')
            self.assertIn("internet", no_results_error.text, "Wrong information")
            # 3. Weryfikacja widoczności informacji o wskazówkach oraz samych wskazówek odnośnie wyszukiwania
            self.driver.find_element(By.XPATH, '//*[contains(text(),"Wskazówki dotyczące wyszukiwania")]').is_displayed()
            tip1 = self.driver.find_element(By.XPATH, '//ul[@class="list list--unstyled list--icons list--spaced"]/li[1]/span')
            self.assertEqual("Prosimy sprawdzić, czy hasło na pewno zostało wpisane poprawnie.", tip1.text, "Wrong information")
            tip2 = self.driver.find_element(By.XPATH, '//ul[@class="list list--unstyled list--icons list--spaced"]/li[2]/span')
            self.assertEqual("Wyszukiwanie pojedynczych pojęć zwiększa liczbę trafnych wyników.", tip2.text, "Wrong information")
            tip3 = self.driver.find_element(By.XPATH, '//ul[@class="list list--unstyled list--icons list--spaced"]/li[3]/span')
            self.assertEqual("Zalecamy stosowanie jak najbardziej ogólnych pojęć, a następnie poprawę wyników wyszukiwania", tip3.text, "Wrong information")
            sleep(2)

    def tearDown(self):
        self.driver.quit()
