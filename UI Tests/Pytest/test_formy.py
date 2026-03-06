import os
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Disabilita la verifica SSL per webdriver-manager
os.environ["WDM_SSL_VERIFY"] = "0"

# --- FIXTURE ---
@pytest.fixture
def driver():
    # Inizializza il driver correttamente con Service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    # Il driver si chiude solo dopo la fine del test
    driver.quit()

# --- TEST ---
def test_form(driver):
    # Definiamo 'wait' all'inizio, così è disponibile per tutto il test
    wait = WebDriverWait(driver, 10)
    
    driver.get("https://formy-project.herokuapp.com/")
    
    # 1. Trova e clicca Autocomplete
    autocomplete = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Autocomplete")))
    driver.execute_script("arguments[0].scrollIntoView();", autocomplete)
    autocomplete.click()

    # 2. Compilazione campi (Corretti i selettori CSS)
    # Aspetta l'indirizzo principale
    address_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter address']")))
    address_field.send_keys("Verona, Italia", Keys.ENTER)

    # Street address
    driver.find_element(By.ID, "street_number").send_keys("Via Roma 1")
    # Street address 2 (Corretto il selettore che era rotto)
    driver.find_element(By.ID, "route").send_keys("Via Fasulla 123")
    # City
    driver.find_element(By.ID, "locality").send_keys("Verona")
    # State
    driver.find_element(By.ID, "administrative_area_level_1").send_keys("VR")
    # Zip code
    driver.find_element(By.ID, "postal_code").send_keys("37121")
    # Country
    driver.find_element(By.ID, "country").send_keys("Italy")

    sleep(2) 
    driver.back()
    sleep(2) 

    # Verifica che siamo tornati indietro (opzionale)
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Autocomplete")))
    print("Test completato con successo!")

def test_datepicker(driver):
    wait = WebDriverWait(driver, 10)
    
    driver.get("https://formy-project.herokuapp.com/datepicker")

    wait.until(EC.element_to_be_clickable((By.ID, "datepicker"))).click()


    sleep(5) 

    print("Test completato con successo!")
   #PER ESEGUIRE UN SINGOLOTEST: pytest "UI Tests\Pytest\test_formy.py::test_datepicker"


# Nota: Se usi Pytest, l'input() finale non serve perché Pytest gestisce la chiusura.
# Se vuoi vederlo fermo, lascia lo sleep più lungo.

#comando per avviare il test: pytest "UI Tests\Pytest\test_formy.py" -v