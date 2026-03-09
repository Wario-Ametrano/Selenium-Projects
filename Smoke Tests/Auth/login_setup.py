import pickle
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# 1️⃣ Apri il dominio pulito
driver.get("https://www.saucedemo.com/")

# 2️⃣ Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# 3️⃣ Aspetta il redirect alla pagina inventario
sleep(2)

# 4️⃣ Path per salvare i cookie
base_dir = Path(__file__).resolve().parent.parent
cookies_dir = base_dir / "Coockies"
cookies_dir.mkdir(exist_ok=True)

cookies_file = cookies_dir / "cookies.pkl"

# 5️⃣ Salva i cookie
with open(cookies_file, "wb") as file:
    pickle.dump(driver.get_cookies(), file)

print("Cookies salvati in:", cookies_file)

driver.quit()
