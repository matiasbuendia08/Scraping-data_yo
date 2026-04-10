import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


url = "https://admision.unmsm.edu.pe/Website20262/A/A.html"
driver.get(url)
time.sleep(3)

links = driver.find_elements(By.CSS_SELECTOR, "a[href]")

carreras = []
for link in links:
    href = link.get_attribute("href")
    nombre = link.text.strip()
    if href and "/Website20262/" in href and nombre:
        carreras.append({"nombre": nombre, "url": href})

print("Carreras encontradas:", len(carreras))

todos = []

for carrera in carreras:
    print("Extrayendo:", carrera["nombre"])
    
    try:
        driver.get(carrera["url"])
        time.sleep(2)

        try:
            selector = driver.find_element(By.CSS_SELECTOR, "select[name*='length']")
            Select(selector).select_by_value("-1")
            time.sleep(2)
        except:
            pass

        filas = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        
        for fila in filas:
            celdas = fila.find_elements(By.TAG_NAME, "td")
            datos = [celda.text for celda in celdas]
            if datos:
                datos.insert(0, carrera["nombre"])
                todos.append(datos)

    except Exception as e:
        print("Error en", carrera["nombre"], ":", e)

# Guardar a Excel
df = pd.DataFrame(todos)
df.to_excel("output/resultados_sanmarcos.xlsx", index=False)
print("Archivo guardado!")

driver.quit()
    
