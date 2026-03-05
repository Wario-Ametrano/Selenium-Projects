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

CHARVEL_LINK = "https://www.charvel.com/"

chrome_driver = ChromeDriverManager().install()
driver = Chrome(service=Service(chrome_driver))
driver.maximize_window()
driver.get(CHARVEL_LINK)

wait = WebDriverWait(driver, 10)

sleep(2)#Attende 2 secondi per assicurarsi che la pagina sia completamente caricata prima di interagire con gli elementi

driver.find_element(By.CLASS_NAME, "osano-cm-accept-all").click() #Accetta i cookie
sleep(2)
driver.find_element(By.CLASS_NAME, "close-button").click() #Chiude la finestra di iscrizione alla newsletter
sleep(2)

driver.find_element(By.XPATH, "//a[contains(text(),'Guitar')]").click() #Clicca su Guitar
# clicca View All
view_all = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View All"))) #Aspetta che il link "View All" sia cliccabile e poi clicca
view_all.click()
driver.execute_script("window.scrollBy(0, 500);")

# trova il bottone della pagina 2
page2 = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "2")))
# scroll fino all'elemento
driver.execute_script("arguments[0].scrollIntoView();", page2)
# clicca il bottone
page2.click()

driver.execute_script("window.scrollBy(0, 500);") #Scrolla di 500 pixel verso il basso per visualizzare più prodotti

elemento = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, '2966051557_cha_ins_frt_1_rr.png')]"))) #Aspetta che l'immagine del prodotto "Pro-Mod So-Cal" sia cliccabile e poi clicca
elemento.click() #Clicca sul prodotto "Pro-Mod So-Cal"
sleep(2)

driver.find_element(By.XPATH,"//div[@class='product-color-chips']//a[contains(text(),'Snow White')]").click() #Clicca sulla variante "Snow White" del prodotto
sleep(2)

elementoGallery = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, '2966251576_cha_ins_frt_1_rr.png')]")))
elementoGallery.click() #Clicca sull'immagine del prodotto nella galleria per visualizzarla in dettaglio
sleep(5)
driver.find_element(By.CLASS_NAME, "lb-close").click()#Chiude la visualizzazione in dettaglio dell'immagine del prodotto


input() #Mantiene la finestra aperta finché non viene premuto invio


# comando per avviare il test: python charvel_automation.py