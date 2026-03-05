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

sleep(2) #Attende 2 secondi per assicurarsi che la pagina sia completamente caricata prima di interagire con gli elementi
# Trova l'elemento
btn = driver.find_element(By.XPATH, "//*[text()='FIND MY CANDY!']")
# CLICCA "DIETRO" IL BANNER (via JavaScript)
driver.execute_script("arguments[0].click();", btn)
sleep(2) 
driver.find_element(By.ID, "popup-widget540-cta").click() #Accetta i cookie












input() #Mantiene la finestra aperta finché non viene premuto invio


#comando per avviare il test:python "UI Tests\candymapper.py"
