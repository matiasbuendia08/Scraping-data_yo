# Scraping_data 🕷️

Tarea 1: Proyecto de Web Scraping y consumo de API REST desarrollado en Python.

## Tarea 1 — Web Scraping UNMSM

### ¿Qué hace?
Extrae automáticamente los resultados del examen de admisión de la Universidad Nacional Mayor de San Marcos, carrera por carrera, y los consolida en un archivo Excel.

### ¿Cómo instalar las dependencias?
```bash
pip install selenium openpyxl pandas
```

### ¿Cómo ejecutar el script?
```bash
python scraper.py
```

### ¿Qué contiene el output?
El archivo `output/resultados_sanmarcos.xlsx` contiene todos los postulantes de todas las carreras con su información completa.


## Tarea 2 — API REST RAWG

### ¿Qué hace?
Consume la API de RAWG para extraer, analizar y comparar datos de videojuegos. Incluye exploración general, análisis por categorías, comparaciones entre plataformas y géneros, y exportación de datos a CSV.

### ¿Cómo instalar las dependencias?
```bash
pip install requests pandas
```

### ¿Cómo ejecutar el notebook?
Abrir el archivo `api/tarea_rawg_api.ipynb` en Jupyter Notebook.

### ¿Qué contiene el output?
El archivo `api/output/top20_rawg.csv` contiene los 20 mejores juegos de todos los tiempos con su nombre, rating, metacritic, fecha de lanzamiento y género principal.
