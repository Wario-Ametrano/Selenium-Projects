import os
from time import sleep # Importa il modulo os per gestire le variabili d'ambiente

# Disabilita la verifica SSL per webdriver-manager
os.environ["WDM_SSL_VERIFY"] = "0"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/")


wait = WebDriverWait(driver, 10)#Crea un'istanza di WebDriverWait con un timeout di 10 secondi

autocomplete = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Autocomplete")))#Aspetta che il link "Autocomplete" sia visibile e poi lo seleziona
driver.execute_script("arguments[0].scrollIntoView();", autocomplete)#Scorri fino al link "Autocomplete" per assicurarti che sia visibile prima di cliccarlo
autocomplete.click()



input() #Mantiene la finestra aperta finché non viene premuto invio

#comando per avviare il test:python "UI Tests\formy.py"