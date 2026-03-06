import os

# Disabilita la verifica SSL per webdriver-manager
os.environ["WDM_SSL_VERIFY"] = "0"

from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CANDY_LINK = "https://candymapper.com/"

chrome_driver = ChromeDriverManager().install()
driver = Chrome(service=Service(chrome_driver))
driver.maximize_window()
driver.get(CANDY_LINK)

wait = WebDriverWait(driver, 10)

# Trova l'elemento
btn = driver.find_element(By.XPATH, "//*[text()='FIND MY CANDY!']")
# CLICCA "DIETRO" IL BANNER (via JavaScript)
driver.execute_script("arguments[0].click();", btn)
driver.find_element(By.ID, "popup-widget540-cta").click() #Accetta i cookie
   
driver.find_element(By.XPATH, "//*[@data-ux='ListItemInline']//a[contains(text(),'Halloween Party')]").click() #Clicca su "Halloween Party" tramite data-ux
sleep(1)
driver.find_element(By.CSS_SELECTOR, "a[href='/host-a-party-1']").click() #Clicca su "Hosting a Party" tramite CSS Selector
sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(),'Zombies')]").click() #Clicca su "Halloween Party" tramite data-ux
sleep(1)
driver.execute_script("window.scrollBy(0, 500);") #Scrolla di 500 pixel verso il basso per visualizzare più prodotti
driver.find_element(By.XPATH,"//a[contains(text(),'Find out more')]").click()


input() #Mantiene la finestra aperta finché non viene premuto invio


#comando per avviare il test:python "UI Tests\candymapper.py"
