import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.relative_locator import locate_with

# DANE TESTOWE
search = "test"


class SearchFunctionTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.filmweb.pl")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, 'didomi-notice-agree-button').click()
        self.driver.implicitly_wait(20)

    ### Testy sprawdzające poprawność działania wyszukiwarki ###
    def testSearchingByText(self):
        skip_button = self.driver.find_element(By.XPATH, '//button[@class="ws__skipButton"]')
        search_field = self.driver.find_element(By.ID, 'inputSearch')
        if skip_button.is_enabled():
            skip_button.click()
            search_field.click()
        else:
            search_field.click()

        search_field2 = self.driver.find_element(By.XPATH, '//input[contains(@class,"form__input--empty")]')
        search_field2.click()
        search_field2.send_keys(search)
        sleep(2)

        # - sprawdzenie, czy wyświetla się 6 wyników
        results = self.driver.find_elements(By.XPATH, '//span[@class="resultItem__main"]')
        self.assertEqual(6, len(results))
        # - sprawdzenie, czy w wyszukanych wynikach znajduje się wpisana fraza
        result = self.driver.find_element(By.XPATH, '//span[@class="resultItem__main"]')
        self.assertIn("Test", result.text, "Niezgodność tekstu")
        # - sprawdzenie, czy wyniki wyświetlają się w odpowiednim miejscu, czyli pod polem tekstowym z wpisaną frazą
        search_field_text = self.driver.find_element(By.NAME, 'q')
        results_locator = locate_with(By.XPATH, '//span[@class="resultItem__main"]').below(search_field_text)
        results_location = self.driver.find_element(results_locator)
        self.assertEqual(result.id, results_location.id)

    def tearDown(self):
        self.driver.quit()
