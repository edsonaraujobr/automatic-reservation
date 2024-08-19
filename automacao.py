from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
import os


load_dotenv()

# Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument("--headless")  # Executar em modo headless (sem abrir o navegador)

driver = webdriver.Chrome(options=chrome_options)

# Acesse o site da academia
driver.get("https://app.condomob.net/")
driver.implicitly_wait(10)
try:
    driver.find_element(By.XPATH, "//button[text()='Agora não']").click()
    driver.find_element(By.XPATH, "//button[text()='Continue with Google']").click()
    time.sleep(2)

    windows = driver.window_handles

    driver.switch_to.window(windows[1])

    email = driver.find_element(By.ID, "identifierId")
    email.send_keys(os.getenv('email'))
    driver.find_element(By.CSS_SELECTOR, "button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ").click()

    password = driver.find_element(By.XPATH, "//input[@type='password' and contains(@class, 'whsOnd') and contains(@class, 'zHQkBf')]")
    password.send_keys(os.getenv('password'))
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf").click()
    time.sleep(2)

    driver.switch_to.window(windows[0])
    ap = os.getenv('ap')
    driver.find_element(By.XPATH, "//button[strong[text()='{ap}']]").click()

    print("Horário marcado com sucesso!")

except Exception as e:
    print(f"Erro ao marcar o horário: {e}")

finally:
    driver.quit()
