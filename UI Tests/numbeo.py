import os

# Disabilita la verifica SSL per webdriver-manager
os.environ["WDM_SSL_VERIFY"] = "0"

from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

NUMBEO_LINK = "https://it.numbeo.com/"

chrome_driver = ChromeDriverManager().install()
driver = Chrome(service=Service(chrome_driver))
driver.maximize_window()
driver.get(NUMBEO_LINK)
driver.find_element(By.ID, "city_selector_menu_city_id").send_keys("Florianopolis")
sleep(1)
driver.find_element(By.CLASS_NAME, "ui-menu-item").click()

driver.find_element(
    By.XPATH, '//span[contains(@class,"nobreak")]/a[text()="Inquinamento"]'
).click()

indice_tr = driver.find_element(
    By.XPATH, '//td[text()="Insoddisfazione per la Nettezza Urbana"]/parent::tr'
)

input()
