import os
import pickle
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

# 1️⃣ Devi aprire il dominio pulito, senza query string
driver.get("https://www.saucedemo.com/")

# 2️⃣ Percorso del file cookies.pkl
script_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(script_dir)
cookies_path = os.path.join(root_dir, "Smoke Tests", "Coockies", "cookies.pkl")

# 3️⃣ Carica i cookie
with open(cookies_path, "rb") as f:
    cookies = pickle.load(f)

# 4️⃣ Aggiungi i cookie
for cookie in cookies:
    # Selenium richiede che non ci sia il campo 'sameSite' in alcuni casi
    cookie.pop('sameSite', None)
    driver.add_cookie(cookie)

# 5️⃣ Ricarica la pagina con sessione attiva
driver.refresh()

print("Titolo pagina:", driver.title)

sleep(5)
driver.quit()