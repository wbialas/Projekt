from selenium import webdriver
import time

#1. Otwarcie strony internetowej w przegladarce Chrome
driver = webdriver.Chrome()
driver.get('https://www.filmweb.pl')
print ('Nazwa strony to', driver.title)
driver.maximize_window()

#2. Akceptacja plikow cookies
cookies_button = driver.find_element('id','didomi-notice-agree-button')
cookies_button.click()
time.sleep(4)

#3.Przycisk przekierowania na strone
forward_button = driver.find_element('xpath','/html/body/div[1]/div[1]/div/button')
forward_button.click()
time.sleep(4)

#4. Przejscie do rejestracji
login_button = driver.find_element('id','main-header_login-link')
login_button.click()
account_button = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/div/ul/li[5]/a/div')
account_button.click()
time.sleep(3)

#5. Wprowadzenie danych konta cz.1
login_field = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[1]/div/div[1]/div[1]/input')
login_field.send_keys('dowolny login')
email_field = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[1]/div/div[1]/div[2]/input')
email_field.send_keys('dowolny mail')
password_field = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[1]/div/div[1]/div[3]/input')
password_field.send_keys('dowolne hasło')
#haslo musi zawierac jedna wielka litere, co najmniej jedna cyfre i minimum 8 znakow

time.sleep(3)
register1_button = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[1]/div/div[3]/div')
register1_button.click()

#6. Wprowadzenie danych konta cz.2
name_field = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[2]/div/div[1]/div[1]/div[1]/div/input')
name_field.send_keys('Wojciech')
lastname_field = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[2]/div/div[1]/div[1]/div[2]/div/input')
lastname_field.send_keys('Test')
gender_button = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[2]/div/div[1]/div[2]/div/label[1]')
gender_button.click()
date_button = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[2]/div/div[1]/div[3]/div/div/div[1]/button')
date_button.click()
time.sleep(3)
year_button = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[2]/div/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div[2]/button[4]')
year_button.click()
checkbox = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[2]/div/div[1]/div[4]/div[1]/div/div[1]/label[1]/div')
checkbox.click()

#7. Utworzenie konta i przejscie do potwierdzenia przeslania maila aktywacyjnego
register2_button = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/form/fieldset[2]/div/div[2]/button')
register2_button.click()
time.sleep(4)

#8. Potwierdzenie, ze komunikat sie wyswietla (zakonczenie testu)
confirmation = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]')

if confirmation.is_enabled():
    print('OK')

else:
    print('FALSE')

driver.quit()
