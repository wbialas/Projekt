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

#4. Przejscie do logowania
login_button = driver.find_element('id','main-header_login-link')
login_button.click()
login_button2 = driver.find_element('xpath','//*[@id="site"]/div[2]/div/div/div[1]/div/div/ul/li[2]/a')
login_button2.click()

#5. Wprowadzenie danych do logowania i zalogowanie
login_field = driver.find_element('name','j_username')
login_field.send_keys('wbialas_test')
password_field = driver.find_element('name','j_password')
password_field.send_keys('Kontotestowe123')

time.sleep(2)
login_button3 = driver.find_element('xpath','//*[@id="loginForm"]/div[2]/ul/li[1]/button')
login_button3.click()

#6. Przejście do swojego konta
time.sleep(2)
account_button = driver.find_element('xpath','//*[@id="userHeaderButton"]/a[2]/span/span')
account_button.click()

#7. Sprawdzenie poprawności linku poprzez asercję i zamknięcie przeglądarki

try:
    assert driver.current_url == 'https://www.filmweb.pl/user/wbialas_test'
except:
    driver.get_screenshot_as_file('screenshot1.png')
finally:
    print('Po asercji')
    driver.quit()

