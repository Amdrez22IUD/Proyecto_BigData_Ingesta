import requests
import sqlite3
import pandas as pd
import os

# Configuración de URLs y Rutas (Basado en estructura exigida) [cite: 108]
API_URL = "https://jsonplaceholder.typicode.com/todos"
DB_PATH = "src/db/ingestion.db"
LOG_PATH = "src/static/auditoria/ingestion.txt"
XLSX_PATH = "src/xlsx/ingestion.xlsx"

def asegurar_directorios():
    """Crea las carpetas necesarias si no existen."""
    for ruta in [DB_PATH, LOG_PATH, XLSX_PATH]:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)

def extraer_datos(url):
    """Lectura de datos desde un API[cite: 26]."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al conectar con la API: {response.status_code}")

def guardar_en_db(datos):
    """Almacenamiento en SQLite[cite: 28]."""
    asegurar_directorios()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Diseño de tabla [cite: 30]
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_comments (
            id INTEGER PRIMARY KEY,
            userId INTEGER,
            title TEXT,
            completed BOOLEAN
        )
    ''')

    for item in datos:
        cursor.execute('''
            INSERT OR REPLACE INTO tb_comments (id, userId, title, completed)
            VALUES (?, ?, ?, ?)
        ''', (item['id'], item['userId'], item['title'], str(item['completed'])))

    conn.commit()
    conn.close()

def generar_evidencias(data_api):
    """Generación de archivos Pandas y Auditoría[cite: 32]."""
    conn = sqlite3.connect(DB_PATH)
    # Lectura desde DB con Pandas [cite: 74]
    df_db = pd.read_sql_query("SELECT * FROM tb_comments", conn)
    conn.close()

    # 1. Archivo Excel (Muestra de datos) [cite: 34]
    df_db.head(10).to_excel(XLSX_PATH, index=False)

    # 2. Archivo de Auditoría .txt [cite: 35]
    registros_api = len(data_api)
    registros_db = len(df_db)

    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        f.write("RESUMEN DE AUDITORÍA\n")
        f.write("====================\n")
        f.write(f"Registros extraídos de la API: {registros_api}\n")
        f.write(f"Registros guardados en la DB: {registros_db}\n")

        if registros_api == registros_db:
            f.write("\nESTADO: Sincronización Exitosa.\n")
        else:
            f.write("\nESTADO: Discrepancia detectada.\n")

if __name__ == "__main__":
    print("Iniciando proceso de ingesta...")
    datos = extraer_datos(API_URL)
    guardar_en_db(datos)
    generar_evidencias(datos)
    print(f"Proceso completado. Archivos generados en 'src/'")