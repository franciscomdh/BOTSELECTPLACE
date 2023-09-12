from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Configuración inicial
url = "https://franciscomdh.github.io/"
# Inicializar el navegador (asegúrate de tener el driver adecuado, como ChromeDriver)
driver = webdriver.Chrome()


# Esperar hasta que el campo de email esté presente
wait = WebDriverWait(driver, 40)
# Función para recargar la página hasta que el botón esté desbloqueado y luego hacer clic en él
def presionar_boton_desbloqueado():
    driver.get(url)
    while True:
        try:
            # Esperar hasta que el botón esté presente y habilitado
            boton_element = wait.until(EC.element_to_be_clickable((By.ID, "I")))
            boton_element.click()
            print("Botón desbloqueado y presionado.")
            break
        except:
            print("Botón bloqueado. Recargando la página...")
            driver.refresh()

# Ejecutar la función para presionar el botón desbloqueado
presionar_boton_desbloqueado()