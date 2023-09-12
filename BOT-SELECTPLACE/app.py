from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración inicial
url = "https://soysocio.bocajuniors.com.ar/comprar_plano_general.php?eNid=655"

# Inicializar el navegador (asegúrate de tener el driver adecuado, como ChromeDriver)
driver = webdriver.Chrome()

# Cargar la página de inicio de sesión
driver.get("https://soysocio.bocajuniors.com.ar/index.php")

# Encontrar y presionar el enlace que te lleva al campo de inicio de sesión por ID
enlace = driver.find_element("id", "loginButton2")
enlace.click()

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

# Recorrer la tabla por fila y columna
tabla = driver.find_element("class", "secmap")  # Reemplaza con la clase de la tabla
filas = tabla.find_elements(By.TAG_NAME, "tr")
for fila in filas:
    celdas = fila.find_elements(By.TAG_NAME, "td")
    for celda in celdas:
        print(celda.text)  # Hacer algo con el contenido de la celda


# Cerrar el navegador al finalizar
driver.quit()
