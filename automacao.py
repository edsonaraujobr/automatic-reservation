from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--headless")  # Executar em modo headless (sem abrir o navegador)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://app.condomob.net/")
driver.implicitly_wait(10)
try:
    driver.find_element(By.XPATH, "//button[text()='Agora não']").click()
    driver.find_element(By.XPATH, "//button[@id='adopt-accept-all-button']").click()

    # Login
    driver.find_element(By.XPATH, "//button[text()='Continue with Google']").click()
    time.sleep(1)
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    email = driver.find_element(By.ID, "identifierId")
    email.send_keys(os.getenv('email'))
    driver.find_element(By.CSS_SELECTOR, "button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ").click()
    password = driver.find_element(By.XPATH, "//input[@type='password' and contains(@class, 'whsOnd') and contains(@class, 'zHQkBf')]")
    password.send_keys(os.getenv('password'))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf").click()
    driver.switch_to.window(windows[0])

    # Selecting the apartment
    ap = os.getenv('ap')
    driver.find_element(By.XPATH,f"//button[.//strong[text()='{ap}']]").click()

    #Selecting the gym
    driver.find_element(By.XPATH,"//button[.//p[text()='Space Reservation']]").click()
    driver.find_element(By.XPATH, "//div[@class='sc-hPmGNk dlLSvo']").click()
    driver.find_element(By.XPATH, "//button[@class='sc-jRQBWg fRKbwI']").click()
    driver.find_element(By.XPATH, "//button[text()='yes' and @class='swal2-confirm swal2-styled swal2-default-outline']").click()

    # Making a reservation for today
    today = datetime.today()
    day = today.day
    driver.find_element(By.XPATH, f"//button[.//abbr[text()='{day}']]").click()
    driver.find_element(By.XPATH, "//button[@class='sc-jRQBWg eyIAXi' and .//text()='Request Reservation']").click()

    # Setting the time
    #begin
    hour = driver.find_element(By.XPATH, "(//input[@name='hour24'])[1]")
    hour.send_keys("18")
    minutes = driver.find_element(By.XPATH, "(//input[@name='minute'])[1]")
    minutes.send_keys("00")
    #end
    hour = driver.find_element(By.XPATH, "(//input[@name='hour24'])[2]")
    hour.send_keys("18")
    minutes = driver.find_element(By.XPATH, "(//input[@name='minute'])[2]")
    minutes.send_keys("50")
    driver.find_element(By.XPATH, "//button[@class='sc-jRQBWg fRKbwI' and .//text()='Request Reservation']").click()
    driver.find_element(By.XPATH, "//button[text()='yes' and contains(@class, 'swal2-confirm')]").click()
    time.sleep(10)
    print("Horário marcado com sucesso!")

except Exception as e:
    print(f"Erro ao marcar o horário: {e}")

finally:
    driver.quit()
