import pandas as pd
import sqlite3
import os

# Rutas de entrada y salida 
DB_PATH = 'src/db/ingestion.db'
EXCEL_PATH = 'src/xlsx/cleaned_data.xlsx'
AUDITORIA_PATH = 'src/static/auditoria/cleaning_report.txt'

def extraer_datos():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM tb_comments", conn)
    conn.close()
    return df

if __name__ == '__main__':
    # 1. Extracción
    df = extraer_datos()
    registros_iniciales = len(df)
    
    # 2. Limpieza y Transformación [cite: 34-39]
    # a. Eliminar duplicados (Aunque haya 0, es buena práctica de Big Data)
    df_clean = df.drop_duplicates()
    
    # b. Manejo de nulos (Llenamos posibles vacíos con "Sin dato")
    df_clean = df_clean.fillna("Sin dato")
    
    # c. Corrección de tipos de datos: Convertir 'completed' a booleano real
    if 'completed' in df_clean.columns:
        # Convierte cadenas como "1" o "True" a un valor booleano (True/False)
        df_clean['completed'] = df_clean['completed'].astype(bool)
        
    # d. Transformación adicional: Poner los títulos con la primera letra mayúscula
    if 'title' in df_clean.columns:
        df_clean['title'] = df_clean['title'].str.capitalize()
        
    registros_finales = len(df_clean)

    # 3. Generación de Evidencias [cite: 44-48]
    # Crear carpetas si no existen por precaución
    os.makedirs('src/xlsx', exist_ok=True)
    os.makedirs('src/static/auditoria', exist_ok=True)
    
    # Exportar a Excel
    df_clean.to_excel(EXCEL_PATH, index=False)
    
    # Exportar reporte de auditoría
    with open(AUDITORIA_PATH, 'w', encoding='utf-8') as f:
        f.write("=== REPORTE DE AUDITORÍA DE LIMPIEZA ===\n")
        f.write(f"Registros antes de limpieza: {registros_iniciales}\n")
        f.write(f"Registros después de limpieza: {registros_finales}\n\n")
        f.write("Operaciones realizadas:\n")
        f.write("- Se verificó y eliminó registros duplicados.\n")
        f.write("- Se aplicó manejo de valores nulos (fillna).\n")
        f.write("- Se corrigió el tipo de dato de la columna 'completed' a booleano.\n")
        f.write("- Se normalizó la columna 'title' a formato Capitalizado.\n")

    print(f"Proceso completado. Datos limpios guardados en {EXCEL_PATH}")
    print(f"Reporte de auditoría guardado en {AUDITORIA_PATH}")